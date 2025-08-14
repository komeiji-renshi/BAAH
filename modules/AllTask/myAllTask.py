from enum import Enum
from modules.AllTask import Task, UserTask, EnterApp, HelloWorld, ClickLoginButton

from modules.utils.log_utils import logging, istr, CN, EN
from modules.configs.MyConfig import config

class TaskName():
    """
    配置文件里的task任务名称，此类下的属性可作为task标识符
    """
    LOGIN_GAME = "登录游戏"
    # 仅保留通用入口任务与自定义任务
    CUSTOM = "自定义任务"
    HELLOWORLD = "helloworld"
    CLICK_LOGIN = "点击登陆按钮进入游戏"

class TaskInstance:
    """
    连接配置文件里的task任务名称与i18n包里对应的翻译文字key

    task_config_name: 
        配置文件里的task任务名称
    i18n_key_name:
        i18n包里的翻译文字key
    task_module:
        该task对应模块
    task_params:
        该task对应模块入参
    """
    def __init__(self, task_config_name: str, i18n_key_name: str, task_module: Task, task_params: dict):
        self.task_config_name = task_config_name
        self.i18n_key_name = i18n_key_name
        self.task_module = task_module
        self.task_params = task_params

class TaskInstanceMap:
    """
    可执行任务列表 包含所有脚本可以执行的一级任务
    """
    def __init__(self):
        self.taskmap = {
            TaskName.LOGIN_GAME:
                TaskInstance(
                    task_config_name=TaskName.LOGIN_GAME,
                    i18n_key_name="task_login_game",
                    task_module=EnterApp,
                    task_params={}
                ),
            TaskName.HELLOWORLD: TaskInstance(
                task_config_name=TaskName.HELLOWORLD,
                i18n_key_name="helloworld",
                task_module=HelloWorld,
                task_params={}
            ),
            TaskName.CLICK_LOGIN: TaskInstance(
                task_config_name=TaskName.CLICK_LOGIN,
                i18n_key_name="click_login",
                task_module=ClickLoginButton,
                task_params={}
            ),
            TaskName.CUSTOM: TaskInstance(
                task_config_name=TaskName.CUSTOM,
                i18n_key_name="task_user_def_task",
                task_module=UserTask,
                task_params={}
            ),
        }
        # 生成config task name到i18n task name的映射表
        self.task_config_name_2_i18n_name =  {conname: config.get_text(self.taskmap[conname].i18n_key_name) for conname in self.taskmap}


task_instances_map = TaskInstanceMap()

class AllTask:

    # 单例
    def __init__(self) -> None:
        pass
        
    def parse_task(self) -> None:
        """
        从config里解析任务列表，覆盖原有的任务列表
        """
        self.taskpool = []
        if config.userconfigdict["OPEN_GAME_APP_TASK"]:
            self.add_task(EnterApp())
        # GUI为了显示TaskName也会导入此文件，从而创建AllTask的实例，这边判断下如果config没有解析json就跳过
        if "TASK_ORDER" in config.userconfigdict and "TASK_ACTIVATE" in config.userconfigdict:
            # 把config的任务列表转换成任务实例列表
            for i in range(len(config.userconfigdict['TASK_ORDER'])):
                task_name = config.userconfigdict['TASK_ORDER'][i]
                if task_name not in task_instances_map.taskmap:
                    logging.error({
                        CN: f"任务名:<{task_name}>无法解析, 已知的任务名有: {list(task_instances_map.taskmap.keys())}",
                        EN: f"Task name : {task_name} can not be parsed, please check it is one of: {list(task_instances_map.taskmap.keys())}"
                    })
                    raise Exception("Task Name can not be recognized and parsed")
                # 如果任务对应的TASK_ACTIVATE为False，则不添加任务
                if config.userconfigdict['TASK_ACTIVATE'][i] == False:
                    continue
                self.add_task(task_instances_map.taskmap[task_name].task_module(**task_instances_map.taskmap[task_name].task_params))
        else:
            logging.warn({"zh_CN": "配置文件无TASK_ORDER和TASK_ACTIVATE解析", "en_US":"NO TASK_ORDER and TASK_ACTIVATE in config file"})
        # PostAllTask（统计资源）依赖特定游戏UI，已移除
        
        
    
    def run(self):
        """
        运行任务
        """
        # 运行任务前解析需要执行的任务内容，适应config的不同解析导致的config本身的更改
        self.parse_task()
        # 解析上次运行到第几个任务了，默认这个下标值是-1，如果是continue run的话会是发生报错时的任务下标。
        last_do_task_index = config.sessiondict["CURRENT_PERIOD_TASK_INDEX"]
        if last_do_task_index != -1:
            logging.warn(istr({
                CN: f"CURRENT_PERIOD_TASK_INDEX = {last_do_task_index}，继续运行",
                EN: f"CURRENT_PERIOD_TASK_INDEX = {last_do_task_index}, continue run"
            }))
        for i,task in enumerate(self.taskpool):
            if i < last_do_task_index and task.name not in ("EnterGame", "EnterApp"):
                # 跳过已经完成的任务（保留登录游戏任务）
                continue
            # 运行任务，更新正在运行的任务下标
            config.sessiondict["CURRENT_PERIOD_TASK_INDEX"] = i
            task.run()
    
    def add_task(self, task:Task) -> None:
        """
        添加任务
        """
        self.taskpool.append(task)


my_AllTask = AllTask()