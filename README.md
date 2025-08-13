# 碧蓝档案爱丽丝助手 (BAAH)

<div style="display:flex;justify-content:space-around"><img src="./docs/static/aris.png" style="width:48%"/><img src="./docs/static/kei.png" style="width:48%"/></div>

---

BAAH可以帮助你在模拟器内自动完成碧蓝档案（国际服，日服，国服）的每日任务111

BAAH can help you finish daily tasks of BlueArchive (Global server, Japan server, CN server) in emulator automatically.

---

[ :tada: 全新的项目官网上线啦 | Project website is deployed :tada: ](https://baah.sanmusen.top/)

---

[项目文档 | Project Document](./README.md) <-- You are here | 你在这里

如何使用请见使用文档 / Get to know how to use BAAH by reading usage documents

[中文使用文档](./docs/README_cn.md) | [English Usage Document](./docs/README_en.md)

[中文开发文档](./docs/README_dev.md) | [English Dev Document](./docs/README_dev_en.md)

---

<img src="./docs/static/GUI_CN.png" />
<img src="./docs/static/GUI_EN.png" />
<img src="./docs/static/GUI_JP.png" />


# Support

支持的操作系统/Systems supported:

- Windows (executable file, source code)
- MacOS (source code)
- Linux (source code, docker)
- Android Termux (source code, proot, experimental)

支持的BA游戏服务器/Supported BA servers：

- 国际服 Global Server 
- 日服 Japanese Server 
- 国服 CN Server 
- B服 Bilibili Server 

# Functions

支持的功能:

- 自动打开模拟器，自动执行，自定义添加启动加速器任务，自动关闭模拟器
- 领取（咖啡馆产出/邀请/摸头，社团签到，每日任务奖励，邮件，活动，战术大赛，总力战）
- 消耗体力/票卷进行扫荡（课程表，普通关，困难关，活动关，悬赏通缉，特殊任务，学院交流会，战术大赛，总力战）
- 购买（每日商店购买，竞技场商店购买）
- 探索（清桃信红点，推普通关卡，推困难关卡，推活动关卡，推主线剧情）
- 自动更新游戏（游戏包体，资源包）

Supported Functions：

- Auto open emulator
- Collect (Cafe Rewards, Invite in Cafe, Touch Head, Club Sign in, Daily Task Rewards, MailBox，Event Rewards，Tactical Challenge Rewards, Total Assault Rewards)
- Spend tickets/power to raid (Timetable, Normal, Hard, Event, Bounty, Commissions, Scrimmage, Tactical Challenge, Total Assault)
- Buy (Normal Shop，Tactical Challenge Shop)
- Explore (Momotalk, Normal, Hard, Event, Episode)
- Update game (Game Package, Resource Package)

# Star

如果觉得本项目对你有帮助，请点一点网页右上角的Star⭐ / Please star⭐ if you like it, ^ ^.

[![Stargazers over time](https://starchart.cc/sanmusen214/BAAH.svg?variant=adaptive)](https://starchart.cc/sanmusen214/BAAH)

# Thank

## Contributors

<a href="https://github.com/sanmusen214/BAAH/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sanmusen214/BAAH" />
</a>

Icons from [@dada008](https://space.bilibili.com/23726244?spm_id_from=333.337.0.0)

Release notification bot support [@xiaofeiTM233](https://github.com/xiaofeiTM233)

## Packages

[opencv-python](https://github.com/opencv/opencv)

[pponnxcr](https://github.com/hgjazhgj/pponnxcr)

[nicegui](https://github.com/zauberzeug/nicegui)

[MaaTouch](https://github.com/MaaAssistantArknights/MaaTouch)

[Aria2](https://github.com/aria2/aria2)

# 1.BAAH自动化测试项目本身

这个项目（BAAH）是一个较为复杂的自动化或辅助工具项目，目录结构和文件内容显示它有较多的功能模块，支持多语言，包含图形界面（GUI）、自动化任务、配置管理等。下面我将对主要目录和文件进行分析，说明它们的内容和作用：

## 1. 根目录主要文件

- **main.py**入口文件，通常负责启动整个程序，初始化配置、界面或主流程。
- **BAAH.py**体积较大（564行），很可能是主业务逻辑或核心控制器，负责调度各个模块。
- **package.py**可能与打包、分发或安装相关，或者是某些功能的集合。
- **update.py**负责程序的更新逻辑，比如检查新版本、下载和替换文件等。
- **jsoneditor.py**体积较小，可能是用于编辑JSON配置文件的工具脚本。
- **requirements.txt**Python依赖包列表，说明项目依赖的第三方库。
- **README.md**项目说明文档，介绍项目用途、安装方法、使用说明等。
- **Dockerfile / Dockerfile.CN / docker-compose.yml**支持容器化部署，方便在不同环境下快速搭建和运行。

## 2. 主要目录

### DATA/

- **assets/**存放图片资源（如按钮、页面、弹窗等），用于界面显示或图像识别。
- **assets_cn/**、**assets_global_en/**、**assets_jp/**多语言资源文件夹，分别存放中文、英文、日文的图片资源。
- **CONFIGS/**存放临时或持久化的配置文件（如temp.json）。
- **grid_solution/**可能是某种关卡、任务或网格类问题的解决方案数据（json文件）。
- **i18n****/**多语言文本资源（如en_US.json、zh_CN.json等），用于界面或日志的国际化。
- **icons/**存放程序图标。
- **touch.zip**可能是某些资源的压缩包。

### gui/

- **components/**各种界面组件（如按钮、编辑区、任务池等），用于构建GUI。
- **pages/**各种设置页面（如Setting_Assault.py、Setting_BuyAP.py等），每个文件对应一个功能设置界面。
- **refactor_pages/**重构后的页面模块，可能是对旧页面的优化或替换。

### modules/

- **AllPage/**页面相关的逻辑。
- **AllTask/**自动化任务相关的模块，按功能细分（如AutoAssault、AutoStory、BuyAP等），每个子目录下有具体的任务实现。
- **configs/**配置管理相关代码（如defaultSettings.py、MyConfig.py等）。
- **utils/**工具类代码（如adb_utils.py、log_utils.py、image_processing.py等），为主程序提供通用功能。

## 3. 其他

- **BAAH_CONFIGS/**可能是用户自定义或导出的配置文件夹。
- **docs/**项目文档，包括多语言的开发文档、用户手册、界面截图等。
- **.github/**GitHub相关配置，如CI/CD、Issue模板等。
- **.gitignore**Git忽略文件列表。

## 4. 项目作用推测

结合目录和文件名，推测本项目是一个针对某款游戏或应用的自动化辅助工具，具备以下特性：

- **自动化任务执行**：如自动刷关、自动收集奖励、自动购买等（见AllTask目录）。
- **多语言支持**：支持中、英、日三种语言，适配不同地区用户。
- **图形界面**：有丰富的GUI组件和设置页面，方便用户配置和操作。
- **配置灵活**：支持多种配置文件和自定义设置。
- **可扩展性****强**：任务和页面模块化，便于后续扩展新功能。
- **容器化****部署**：支持Docker，方便在服务器或云端运行。

## 5. 总结

本项目是一个功能丰富、结构清晰的自动化辅助工具，适用于需要批量、自动化操作的场景（如手游脚本、数据收集等）。其核心在于任务自动化、界面友好和多语言适配，适合有一定技术基础的用户使用和二次开发。

如果你有具体想了解的模块或文件，可以告诉我，我可以进一步详细分析其实现和作用。

# 2.目前这个项目的执行流和入口

## 1. 入口文件

### 主入口（自动化脚本/命令行模式）

- **入口文件：****`main.py`**
- 启动方式：  
  - 命令行运行：`python main.py 配置文件名.json`
  - 或通过批处理：`pythonrun.bat`（内部调用`main.py`）

#### 主要执行流程

1. **配置****环境**：将当前目录加入`sys.path`。
2. **解析配置**：导入`modules.configs.MyConfig`，加载用户指定的配置文件（如未指定则交互式选择）。
3. **日志记录**：输出当前目录和可用配置文件。
4. **加载主流程**：导入`BAAH.py`中的`BAAH_core_process`。
5. **执行主流程**：调用`BAAH_core_process()`，正式开始自动化任务。

### GUI入口（图形界面模式）

- **入口文件：****`jsoneditor.py`**
- 启动方式：  
  - 命令行运行：`python jsoneditor.py`
  - 或打包后运行`BAAH_GUI.exe`

#### 主要执行流程

1. **多****进程****支持**：调用`multiprocessing.freeze_support()`。
2. **参数解析**：通过`gui.components.exec_arg_parse.parse_args()`获取GUI参数（如host、port等）。
3. **启动****GUI**：用`nicegui`启动Web界面，供用户配置和操作。

## 2. 主业务流程（以main.py为例）

### 详细执行流

```Plain
flowchart TD
    A[main.py] --> B[解析命令行参数/选择配置文件]
    B --> C[导入并解析配置]
    C --> D[调用BAAH_core_process()]
    D --> E[初始化日志、环境]
    E --> F[导入myAllTask等任务模块]
    F --> G[执行BAAH_main()]
    G --> H[按配置顺序依次执行任务]
    H --> I[任务完成，清理、发送通知等]
```

#### 关键代码流

- `main.py` → `BAAH.py:BAAH_core_process()` → `BAAH_main()` → `myAllTask.run()` → 各种Task（自动化任务）

## 3. 任务调度与执行

- **`modules/AllTask/myAllTask.py`**负责解析配置文件中的任务列表，为每个任务创建Task实例，并顺序执行。
- **`modules/AllTask/`**各种自动化任务的具体实现（如登录、收菜、刷关等）。

## 4. 其他入口

- **`update.py`**负责程序自更新，通常不直接作为主入口，只有在需要更新时才会被调用。

## 5. 总结

- **命令行****/自动化模式入口**：`main.py`
- **图形界面入口**：`jsoneditor.py`
- **主流程**：main.py → 解析配置 → BAAH_core_process → BAAH_main → myAllTask.run → 各种自动化任务
- **配置文件**：位于`BAAH_CONFIGS/`，决定自动化任务内容和顺序

如需更详细的某一部分执行流（如某个Task的执行细节），可以进一步指定模块或文件，我可以帮你画出更细致的流程图或代码调用关系。

# 3.项目的关键技术选型

### 关键技术选型一览

- **语言与运行时**
  - Python 3.10（Windows/macOS/Linux/Docker 兼容）
- **GUI** **与后端框架**
  - **NiceGUI**：Web GUI（`jsoneditor.py` 启动），内置基于 Starlette 的 ASGI
  - **FastAPI/Starlette + Uvicorn**：NiceGUI 底座与接口承载
  - **Socket.IO**：任务运行过程的实时通信（`fastapi-socketio`/`python-socketio`）
  - 可选嵌入：`pywebview`（原生窗体壳）
- **计算机视觉****与** **OCR**
  - **OpenCV +** **NumPy**：模板匹配、图像处理、屏幕区域提取
  - **ONNX Runtime + pponnxcr**：轻量 OCR 推理（不依赖重型框架）
  - 几何与后处理：`shapely`、`pyclipper`
- **安卓/模拟器自动化**
  - **ADB**：通过 `subprocess` 执行 tap/swipe/screencap 等；自动连端口、开关 App、截图管道解码
  - 贴图驱动的 UI 识别（`DATA/assets*` 模板）+ ADB 注入形成“无侵入式自动化”
  - README 致谢提到 **MaaTouch**（精确触控支持，按需集成）
- **配置与****国际化**
  - **Pydantic v2**：配置数据模型与校验
  - **PyYAML / orjson / dotenv**：配置解析与高性能 JSON 处理
  - 多语言资源：`DATA/i18n/*.json` + 自定义 `I18nstr`
- **网络与通信**
  - `requests`、`httpx`、`websockets`、`fastapi-socketio`：更新、通知、长连接
  - `markdown2`、`Jinja2`：文本/模板渲染（主要被 GUI 生态使用）
- **打包与部署**
  - **PyInstaller**：Windows 可执行程序打包（打包内置 `pponnxcr`、ADB）
  - **Docker**（`python:3.10-slim`）：容器化运行 GUI（`jsoneditor.py --no-show` 暴露端口）
  - `docker-compose.yml`：一键编排
- **日志与监控**
  - 标准 `logging` + `coloredlogs`：多语言日志输出
  - `watchfiles`：开发期热重载（GUI/服务）
- **平台互操作（Windows）**
  - `pythonnet`、`clr-loader`、`pywin32-ctypes`：与 Windows/.NET 环境对接（按需）

### 架构与策略选型要点

- **数据驱动的自动化**：以模板图片+OCR 识别驱动任务，避免侵入式 Hook，兼容多服多语言 UI。
- **GUI****/无头双入口**：GUI（NiceGUI）便于配置；命令行入口（`main.py`）便于计划任务与无人值守。
- **轻量** **OCR** **推理**：ONNX Runtime + pponnxcr，体积小、跨平台、部署简单。
- **可移植与易分发**：PyInstaller 打包 + Docker 镜像，覆盖桌面与服务器场景。

目前还缺失的一个功能：具体的分析报告！也就是测试报告结果！

# 4.通用化重构可行性分析

### 结论

- 可行性：高。该项目已有清晰的“设备/视觉/调度/日志通知”分层，核心能力基本通用；定制化主要集中在任务层与资源层。
- 预计成本：中等到偏高，取决于是否保留 GUI 和是否引入任务 DSL。仅提取 CLI 通用内核约 1–2 周；连同 GUI 插件化与蓝档适配回归验证约 2–3 周/人。

### 哪些可复用（通用内核）

- 设备与输入输出（几乎通用）
  - `modules/utils/adb_utils.py`：ADB 连接、截图、tap/swipe、前台 App 检测、进程控制、MaaTouch 支持。
- 计算机视觉与 OCR（通用）
  - `modules/utils/image_processing.py`：模板匹配、颜色匹配、局部 OCR（`pponnxcr` + `onnxruntime`）、截图裁切工具。
- 框架能力（通用）
  - 调度与生命周期：`BAAH.py` 内的启动/收尾流程、前后置命令、错误处理、自动退出、邮件/HTTP 通知。
  - 日志与报告：`modules/utils/log_utils.py`（可落盘日志和异常全量日志）、`modules/utils/notification.py`。
  - 配置骨架：`modules/configs/MyConfig.py`、默认设置与 i18n 机制本身。

### 哪些强绑定“碧蓝档案”（需去定制化）

- 任务层耦合较重
  - `modules/AllTask/Task.py` 直接依赖 `DATA/assets/PageName/ButtonName/PopupName` 与 `modules/AllPage/Page`，内置返回主页、清弹窗、自动编队等“蓝档 UI 流程”。
  - `modules/AllTask/myAllTask.py` 任务注册、`TaskName` 枚举、任务编排和参数均为蓝档语义。
- 资源层完全专用
  - `DATA/assets*`、`DATA/grid_solution`、`DATA/i18n` 大量游戏模板与策略数据。
- GUI 配置页
  - `gui/pages/*` 基本是蓝档任务与术语；需要改为动态生成或插件化。

### 去定制化重构思路（建议架构）

- 抽出“通用自动化内核”（engine）
  - 设备层 API：screenshot、tap、swipe、wait、open_app/close_app。
  - 视觉层 API：match_template、match_pixel、ocr_region。
  - 调度层 API：任务注册表、执行器、重试/超时、错误恢复、前后置钩子。
  - 通知/日志：无改动或轻改动即可复用。
- 任务与 UI 解耦
  - 将 `Task` 基类改为只依赖抽象接口，例如 `UiContext`/`Screen`：
    - `screen.match(selector)`、`screen.click(selector|coords)`、`screen.wait(selector)`；
    - selector 支持图片、OCR 条件、颜色范围，资源由“适配器”提供。
  - 回到主页/清弹窗等逻辑做成“策略/Hook”，由适配器注入，而非写死在 `Task`。
- 适配器（plugin）机制
  - 每个目标项目提供一组 selector、页面模型、任务实现与资源包；在运行时动态注册进调度器。
  - 现有“碧蓝档案”代码改造成一个官方适配器，用于回归验证。
- 配置与 GUI
  - 配置改为通用 schema + 适配器扩展字段；任务列表改为“插件任务 ID 列表 + 参数”。
  - GUI 通过插件自描述（schema/表单）动态生成配置页；先保 CLI，GUI 可分阶段改造。

### 工作量评估（保守估算）

- 通用内核提取（设备/视觉/调度/日志通知复用，剥离蓝档引用）：2–3 天
- `Task` 抽象与适配器接口定义（去掉对 `PageName/ButtonName/PopupName/Page` 的直引）：2–4 天
- 任务注册中心与插件加载（入口、注册、发现）：1 天
- 将现有蓝档实现迁移为插件（验证等价功能）：2–4 天
- 配置重构（通用 + 插件扩展）、CLI 完整跑通：1–2 天
- GUI 动态化（可选，投入较大）：3–6 天
- 测试与文档：2–3 天
- 合计：核心 CLI 方案 1–2 周；含 GUI 插件化与蓝档回归 2–3 周/人

### 风险与难点

- 任务层耦合重：`Task.back_to_home/clear_popup/set_auto_team` 等均强依赖蓝档 UI，需要抽象为“页面策略 Hook”。
- 资源与选择器迁移量大：图片模板、坐标、颜色阈值等需移至插件包并规范化命名。
- GUI 复杂度：现有页面都是硬编码的蓝档任务项，改为插件自描述需要额外设计与实现。
- OCR 语言/字体差异：目标项目如 UI 风格差异大，需重新标定阈值与模板。

### 渐进式落地路线

- 第一步（最小可用）：提取 CLI 通用内核 + 任务抽象 + 插件注册；蓝档作为首个插件验证。
- 第二步：配置通用化 + 插件扩展字段；提供简易 YAML/JSON 任务流（无需 GUI）。
- 第三步（可选）：GUI 动态表单与任务选择由插件自描述驱动。
- 第四步：为其他项目编写“示例适配器”（含少量图片模板与 selector），验证泛化能力。

如果你打算现在开始，我可以：

- 先出一版“Task 抽象接口 + 选择器与页面策略接口”的草案，并改造 1–2 个典型任务作为示例；
- 给出新的配置 schema 与一个最小插件脚手架，帮助你把蓝档迁移成独立插件。
