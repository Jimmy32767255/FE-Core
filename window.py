#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现高斯模糊透明效果的窗口
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from .custom_title_bar import CustomTitleBar
from .background_effect import BackgroundEffect
from .blur_style import apply_blur_style, BLUR_STYLE
from loguru import logger


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
        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 启用透明背景
        self.setFixedSize(800, 500)  # 固定窗口大小
        apply_blur_style(self) # 应用模糊样式
        
        # 创建自定义标题栏
        self.title_bar = CustomTitleBar(self)
        self.title_bar.set_title("Demo")

        # 创建中央部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # 主布局 (用于中央部件)
        main_v_layout = QVBoxLayout(central_widget)
        main_v_layout.setContentsMargins(0, 0, 0, 0)
        main_v_layout.setSpacing(0)
        
        main_v_layout.addWidget(self.title_bar)

        # 内容区域部件
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # 添加标签到内容布局
        version_label = QLabel("Test")
        version_label.setStyleSheet("color: #FFFFFF; font-size: 24px; font-weight: bold;")
        content_layout.addWidget(version_label, alignment=Qt.AlignBottom | Qt.AlignLeft)
        
        # 添加按钮到内容布局
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
        
        main_v_layout.addWidget(content_area)
        
        self.effect = BackgroundEffect(self) # 启用背景模糊效果
        logger.info("窗口UI已初始化完成")

    def set_blur_effect(self, enable: bool):
        """
        启用或禁用窗口的模糊效果。
        :param enable: True 为启用，False 为禁用。
        """
        if enable:
            self.effect.enable(True)
            logger.info("窗口模糊效果已启用")
        else:
            self.effect.enable(False)
            logger.info("窗口模糊效果已禁用")

    def set_window_title(self, title: str):
        """
        设置窗口的标题。
        :param title: 窗口的新标题。
        """
        self.title_bar.set_title(title)
        logger.info(f"窗口标题已设置为: {title}")

    def set_window_icon(self, icon_path: str):
        """
        设置窗口的图标。
        :param icon_path: 图标文件的路径。
        """
        self.title_bar.set_icon(icon_path)
        logger.info(f"窗口图标已设置为: {icon_path}")
        
    def paintEvent(self, event):
        """
        绘制窗口背景 - 简化版
        """
        pass # 最小化 paintEvent 的影响
        
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