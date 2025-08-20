#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
自定义窗口标题栏
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class CustomTitleBar(QWidget):
    """
    自定义标题栏部件
    """
    def __init__(self, parent=None, window_title="", window_icon_path=""):
        super().__init__(parent)
        self.parent_window = parent
        self.init_ui()
        self.set_title(window_title)
        self.set_icon(window_icon_path)

    def init_ui(self):
        """
        初始化UI界面
        """
        self._setup_title_bar_properties()
        layout = self._setup_layout()
        self._add_icon_and_title(layout)
        self._add_control_buttons(layout)
        self._connect_buttons() # 添加按钮信号连接方法

    def _connect_buttons(self):
        """
        连接控制按钮的信号到槽函数。
        """
        self.minimize_button.clicked.connect(self.minimize_window)
        self.maximize_button.clicked.connect(self.maximize_restore_window)
        self.close_button.clicked.connect(self.close_window)

    def _setup_title_bar_properties(self):
        """
        设置标题栏的基本属性，如高度和样式。
        """
        self.setFixedHeight(30)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.01);")

    def _setup_layout(self):
        """
        设置标题栏的布局。
        """
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 5, 0)
        layout.setSpacing(0)
        return layout

    def _add_icon_and_title(self, layout):
        """
        添加窗口图标和标题标签到布局。
        """
        self.icon_label = QLabel(self)
        layout.addWidget(self.icon_label)
        layout.addSpacing(5)

        self.title_label = QLabel("", self)
        self.title_label.setStyleSheet("color: #FFFFFF; font-size: 10pt; font-weight: bold;")
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        layout.addStretch()

    def _add_control_buttons(self, layout):
        """
        添加最小化、最大化/还原和关闭按钮到布局。
        """
        self.minimize_button = self._create_button("-", self.minimize_window, "12pt", "bold")
        layout.addWidget(self.minimize_button)

        self.maximize_button = self._create_button("□", self.maximize_restore_window, "10pt")
        layout.addWidget(self.maximize_button)

        self.close_button = self._create_button("X", self.close_window, "12pt", "bold", is_close_button=True)
        layout.addWidget(self.close_button)

    def _create_button(self, text, font_size, font_weight="normal", is_close_button=False):
        """
        创建并返回一个标准化的标题栏按钮。
        """
        button = QPushButton(text, self)
        button.setFixedSize(30, 30)
        style_sheet = f"""
            QPushButton {{
                border: none;
                background-color: transparent;
                font-size: {font_size};
                font-weight: {font_weight};
            }}
            QPushButton:hover {{
                background-color: {'#e74c3c; color: white;' if is_close_button else 'rgba(255, 255, 255, 0.01);'}
            }}
        """
        button.setStyleSheet(style_sheet)
        return button

    def set_title(self, title: str) -> None:
        """
        设置窗口标题
        :param title: 窗口标题
        """
        self.title_label.setText(title)
        self.title_label.adjustSize()
        self.update()

    def set_icon(self, icon_path: str) -> bool:
        """
        设置标题栏的图标。
        :param icon_path: 图标文件的路径。
        :return: 操作是否成功
        """
        try:
            icon = QIcon(icon_path)
            if icon.isNull():
                return False
            icon_pixmap = icon.pixmap(QSize(16, 16))
            self.icon_label.setPixmap(icon_pixmap)
            self.icon_label.setFixedSize(16, 16)
            self.update()
            return True
        except Exception as e:
            return False

    def minimize_window(self):
        """
        最小化窗口
        """
        if self.parent_window:
            self.parent_window.showMinimized()

    def maximize_restore_window(self):
        """
        最大化或还原窗口
        """
        if self.parent_window:
            if self.parent_window.isMaximized():
                self.parent_window.showNormal()
                self.maximize_button.setText("□") # 还原状态图标
            else:
                self.parent_window.showMaximized()
                self.maximize_button.setText("▣") # 最大化状态图标 (可以用两个方块表示)

    def close_window(self):
        """
        关闭窗口
        """
        if self.parent_window:
            self.parent_window.close()

    def mousePressEvent(self, event):
        """
        鼠标按下事件，用于实现窗口拖动
        """
        # 只在标题栏区域响应拖动
        title_bar_rect = self.rect()
        if event.button() == Qt.LeftButton and self.parent_window and title_bar_rect.contains(event.pos()):
            self.parent_window.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件，用于实现窗口拖动
        """
        if hasattr(self.parent_window, 'old_pos') and self.parent_window.old_pos and self.parent_window:
            delta = event.globalPos() - self.parent_window.old_pos
            self.parent_window.move(self.parent_window.x() + delta.x(), self.parent_window.y() + delta.y())
            self.parent_window.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """
        鼠标释放事件，用于实现窗口拖动
        """
        if event.button() == Qt.LeftButton and self.parent_window:
            self.parent_window.old_pos = None