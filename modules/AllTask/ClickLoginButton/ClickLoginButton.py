from modules.AllTask.Task import Task
from modules.AllPage.Page import Page
from modules.utils import match, page_pic, button_pic, popup_pic, click, screenshot, logging, istr, CN, EN, sleep, check_app_running, open_app, config


class ClickLoginButton(Task):
    """
    通用：在“登录界面”上点击“Login”按钮。

    资源约定（均放在 config.PIC_PATH 指向目录下）：
    - PAGE/PAGE_LOGIN.png       用于识别登录页（建议裁切稳定区域）
    - BUTTON/BUTTON_LOGIN.png   用于匹配“Login”按钮区域
    """

    def __init__(self, name: str = "点击登陆按钮进入游戏", pre_times: int = 1, post_times: int = 1) -> None:
        super().__init__(name, pre_times, post_times)

    def pre_condition(self) -> bool:
        # # 确保应用在前台
        # if not check_app_running(config.userconfigdict['ACTIVITY_PATH']):
        #     open_app(config.userconfigdict['ACTIVITY_PATH'])
        #     sleep(2)
        # # 唤醒界面，避免 UI 隐藏
        # click(Page.MAGICPOINT, sleeptime=0.5)
        # screenshot()
        # # 优先使用页面模板识别，再退化到按钮识别；显式降低阈值以适配通用资源
        # in_login_page = (
        #     match(page_pic("PAGE_LOGIN"), threshold=0.7)
        #     or match(button_pic("BUTTON_LOGIN"), threshold=0.7)
        # )
        # if not in_login_page:
        #     logging.info(istr({CN: "未检测到登录界面，跳过该任务", EN: "Login page not detected, skip this task"}))
        # return in_login_page
        return True

    def on_run(self) -> None:
        # 先尝试点击“Continue”类弹窗按钮，清理前置弹窗
        def has_continue():
            screenshot()
            return match(button_pic("BUTTON_CONTINUE"), threshold=0.75) or match(popup_pic("POPUP_CONTINUE"), threshold=0.75)

        for _ in range(5):
            if has_continue():
                click(button_pic("BUTTON_CONTINUE"), sleeptime=1.0, threshold=0.75) or click(popup_pic("POPUP_CONTINUE"), sleeptime=1.0, threshold=0.75)
                sleep(2.0)
            else:
                break

        # 尝试多次点击 Login 按钮，直到离开登录页或按钮消失
        def try_click():
            if match(button_pic("BUTTON_LOGIN"), threshold=0.7):
                click(button_pic("BUTTON_LOGIN"), sleeptime=10.0, threshold=0.7)
                logging.info(istr({CN: "已点击Login按钮，等待页面跳转", EN: "Clicked Login button, waiting for page jump"}))
            else:
                # 轻点魔法点，促使界面刷新
                click(Page.MAGICPOINT, sleeptime=0.5)

        def left_login_page():
            screenshot()
            still_login_ui = match(page_pic("PAGE_LOGIN"), threshold=0.8) or match(button_pic("BUTTON_LOGIN"), threshold=0.8)
            return not still_login_ui

        # 最多尝试 6 次（约 9 秒）
        Task.run_until(try_click, left_login_page, times=6, sleeptime=1.0)

    def post_condition(self) -> bool:
        # 认为离开登录页或按钮消失即成功
        screenshot()
        return not (match(page_pic("PAGE_LOGIN"), threshold=0.8) or match(button_pic("BUTTON_LOGIN"), threshold=0.8))


