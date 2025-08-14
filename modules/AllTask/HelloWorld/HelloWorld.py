from modules.AllTask.Task import Task
from modules.utils import logging, istr, CN, EN


class HelloWorld(Task):
    def __init__(self, name: str = "HelloWorld") -> None:
        super().__init__(name)

    def pre_condition(self) -> bool:
        return True

    def on_run(self) -> None:
        logging.info(istr({
            CN: "helloworld",
            EN: "helloworld",
        }))

    def post_condition(self) -> bool:
        return True


