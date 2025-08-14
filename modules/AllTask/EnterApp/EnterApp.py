from modules.AllTask.Task import Task
from modules.utils import *

class EnterApp(Task):
    def __init__(self, name: str = "EnterApp", pre_times: int = 1, post_times: int = 1) -> None:
        super().__init__(name, pre_times, post_times)

    def pre_condition(self) -> bool:
        # 通用化：不做与特定应用UI相关的判断
        return True

    def on_run(self) -> None:
        # 通用化：启动应用已由核心流程负责（BAAH_open_target_app），此处不额外处理
        logging.info(istr({CN: "等待4秒后进入游戏", EN: "Wait 4 seconds to enter the game"}))
        sleep(4.0)
        pass

    def post_condition(self) -> bool:
        return True


