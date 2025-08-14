from nicegui import ui
from gui.components.edit_team_strength import edit_the_team_strength_of_this_config
from gui.components.fast_run_task_buttons import show_fast_run_task_buttons, TaskName

def set_explore(config, real_taskname_to_show_taskname, logArea):
    ui.label(config.get_text("setting_explore")).style('font-size: x-large')
    ui.label(config.get_text("desc_team_strength"))
    # 注：探索相关设置为游戏定制内容，通用化后隐藏此页面核心交互，仅保留占位
    ui.label("Explore page is disabled in generic mode").style('color: gray')
        
    