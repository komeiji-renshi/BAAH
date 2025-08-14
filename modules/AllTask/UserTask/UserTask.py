from modules.AllTask.Task import Task
from modules.AllTask.SubTask.ExecCode import ExecCode

from modules.utils import config, logging, istr, CN, EN

class UserTask(Task):
    def __init__(self, name="UserTask") -> None:
        super().__init__(name)

     
    def pre_condition(self) -> bool:
        return True
    
     
    def on_run(self) -> None:
        content = config.userconfigdict["USER_DEF_TASKS"]
        runCode = ExecCode(content)
        runCode.run()
        if runCode.status == Task.STATUS_SUCCESS:
            logging.info(istr({
                CN: "自定义任务执行成功",
                EN: "Defined task success",
            }))
        elif runCode.status == Task.STATUS_ERROR:
            logging.error(istr({
                CN: "自定义任务执行错误，尝试返回游戏主页",
                EN: "Defined task error, try to return to the game homepage",
            }))
            # 非特定游戏，尽量不做强耦合的页面恢复

     
    def post_condition(self) -> bool:
        return True