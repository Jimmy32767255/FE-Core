#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现高斯模糊透明效果的窗口
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from .custom_title_bar import CustomTitleBar
from .background_effect import BackgroundEffect
from .blur_style import apply_blur_style, BLUR_STYLE


class BlurredWindow(QMainWindow):
    """
    带有高斯模糊透明效果的窗口
    """
    def __init__(self):
        super().__init__()
        self.old_pos = None  # CustomTitleBar 会使用这个属性
        self.init_ui()
        
    def init_ui(self):
        """
        初始化UI界面
        """
        self._setup_window_properties()
        self._create_title_bar()
        self._setup_central_widget_and_layout()
        self._setup_content_area()
        self._initialize_background_effect()
        self._connect_signals() # 添加信号连接方法

    def _connect_signals(self):
        """
        连接UI元素的信号到槽函数。
        """
        # 示例：如果标题栏有最小化、最大化、关闭按钮，可以在这里连接它们的信号
        # self.title_bar.minimize_button.clicked.connect(self.showMinimized)
        # self.title_bar.maximize_button.clicked.connect(self.toggle_maximize)
        # self.title_bar.close_button.clicked.connect(self.close)
        pass

    def _setup_window_properties(self):
        """
        设置窗口的基本属性。
        """
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 启用透明背景
        self.setFixedSize(800, 500)  # 固定窗口大小
        apply_blur_style(self)  # 应用模糊样式

    def _create_title_bar(self):
        """
        创建并设置自定义标题栏。
        """
        self.title_bar = CustomTitleBar(self)
        self.title_bar.set_title("Demo")

    def _setup_central_widget_and_layout(self):
        """
        创建中央部件和主布局，并将标题栏添加到主布局。
        """
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_v_layout = QVBoxLayout(central_widget)
        main_v_layout.setContentsMargins(0, 0, 0, 0)
        main_v_layout.setSpacing(0)
        main_v_layout.addWidget(self.title_bar)
        self.main_v_layout = main_v_layout # 保存引用以便后续添加内容区域

    def _setup_content_area(self):
        """
        创建内容区域部件和布局，并添加标签和按钮。
        """
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(20, 20, 20, 20)

        version_label = QLabel("Test")
        version_label.setStyleSheet("color: #FFFFFF; font-size: 24px; font-weight: bold;")
        content_layout.addWidget(version_label, alignment=Qt.AlignBottom | Qt.AlignLeft)

        start_button = QPushButton("Test")
        start_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.01);
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.01);
            }
        """)
        content_layout.addWidget(start_button, alignment=Qt.AlignBottom | Qt.AlignRight)

        self.main_v_layout.addWidget(content_area)

    def _initialize_background_effect(self):
        """
        初始化背景模糊效果。
        """
        self.effect = BackgroundEffect(self)  # 启用背景模糊效果

    def set_blur_effect(self, enable: bool) -> bool:
        """
        启用或禁用窗口的模糊效果。
        :param enable: True 为启用，False 为禁用。
        :return: 操作是否成功
        """
        return self.effect.enable(enable)

    def set_window_title(self, title: str) -> None:
        """
        设置窗口的标题。
        :param title: 窗口的新标题。
        """
        self.title_bar.set_title(title)
        self.setWindowTitle(title)

    def set_window_icon(self, icon_path: str) -> bool:
        """
        设置窗口的图标。
        :param icon_path: 图标文件的路径。
        :return: 操作是否成功
        """
        try:
            success = self.title_bar.set_icon(icon_path)
            if success:
                self.setWindowIcon(QIcon(icon_path))
            return success
        except Exception as e:
            return False
        
    def set_blur_radius(self, radius: int):
        """
        设置模糊效果半径
        :param radius: 模糊半径 (仅当使用QGraphicsBlurEffect时有效)
        """
        self.effect.set_blur_radius(radius)
        
    def set_window_size(self, width: int, height: int):
        """
        设置窗口大小
        :param width: 窗口宽度
        :param height: 窗口高度
        """
        self.setFixedSize(width, height)
        
    def set_content_margins(self, left: int, top: int, right: int, bottom: int):
        """
        设置内容区域边距
        :param left: 左边距
        :param top: 上边距
        :param right: 右边距
        :param bottom: 下边距
        """
        self.centralWidget().layout().setContentsMargins(left, top, right, bottom)
        
    def set_window_opacity(self, opacity: float):
        """
        设置窗口透明度
        :param opacity: 透明度值 (0.0-1.0)
        """
        self.setWindowOpacity(opacity)