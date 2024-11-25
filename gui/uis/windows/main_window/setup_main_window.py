from . functions_main_window import *
import sys
import os
import script_utils
import threading

from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from .ui_main import *
from .functions_main_window import *

from tkinter import filedialog





class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.browser = None
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Open informations",
            "show_top" : False,
            "is_active" : False
        },
    ]

    add_title_bar_menus = [
    ]


    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    def setup_gui(self):
        self.setWindowTitle(self.settings["app_name"])
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        self.ui.title_bar.set_title(self.settings["app_name"])

        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.btns = []
        def make_btn(text, func, height, layout):
            btn = PyPushButton(
                text=text,
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"]
            )
            btn.setMaximumHeight(height)
            layout.addWidget(btn)
            btn.clicked.connect(func)

            self.btns.append(btn)


        def btn_1_clicked():
            self.browser = script_utils.init_browser(self.line_edit.get_text(), port=9998)
            print("启动" + self.line_edit.get_text())

        make_btn("启动托管浏览器", btn_1_clicked, 40, self.ui.load_pages.btn_layout)

        def btn_2_clicked():
            script_utils.work(self.browser)

        make_btn("开始托管", btn_2_clicked, 40, self.ui.load_pages.btn_layout)

        def btn_3_clicked():
            file_path = filedialog.askopenfilename(title='选择要托管的浏览器', filetypes=[('浏览器', '.exe .ink')])
            if file_path != '':
                self.line_edit.setText(file_path)
                print(file_path)
                with open("browser_path.txt", "w") as f:
                    f.write(file_path)

        make_btn("选择托管浏览器", btn_3_clicked, 40, self.ui.load_pages.edit_layout)

        if os.path.isfile("browser_path.txt"):
            with open("browser_path.txt", "r") as f:
                browser_path = f.read()
        else:
            browser_path = ''

        self.line_edit = PyLineEdit(
            text=browser_path,
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )



        self.ui.load_pages.edit_layout.addWidget(self.line_edit)



    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)