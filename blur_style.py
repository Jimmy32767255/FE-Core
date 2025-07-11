#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
为应用程序提供高斯模糊透明效果的样式表
"""

from PyQt5.QtWidgets import QWidget

# 主样式表 - 适用于模糊背景
BLUR_STYLE = """
/* 主窗口样式 */
QMainWindow {
    background-color: rgba(255, 255, 255, 0.01); /* 半透明深色背景 */
    color: #FFFFFF; /* 白色字体 */
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.01);
}

/* 标签控件样式 */
QLabel {
    color: #FFFFFF; /* 白色字体 */
    background-color: transparent; /* 确保背景透明 */
}

/* 列表控件样式 */
QListWidget, QTreeWidget {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF; /* 白色字体 */
    border: 1px solid rgba(255, 255, 255, 0.01);
    border-radius: 4px;
}

QListWidget::item, QTreeWidget::item {
    color: #FFFFFF; /* 确保列表项也是白色 */
}

/* 标签页样式 */
QTabWidget::pane {
    background-color: rgba(255, 255, 255, 0.01);
    border: none;
    border-radius: 4px;
}

QTabBar::tab {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF;
    padding: 8px 16px;
    margin: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF;
}

QTabBar::tab:hover:!selected {
    background-color: rgba(255, 255, 255, 0.01);
}

/* 按钮样式 */
QPushButton {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF;
    border: none;
    border-radius: 4px;
    padding: 6px 12px;
}

QPushButton:hover {
    background-color: rgba(255, 255, 255, 0.01);
}

QPushButton:pressed {
    background-color: rgba(255, 255, 255, 0.01);
}

/* 输入框样式 */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF;
    border: 1px solid rgba(255, 255, 255, 0.01);
    border-radius: 4px;
    padding: 4px;
}

/* 下拉框样式 */
QComboBox {
    background-color: rgba(255, 255, 255, 0.01);
    color: #FFFFFF;
    border: 1px solid rgba(255, 255, 255, 0.01);
    border-radius: 4px;
    padding: 4px;
}

/* 滚动条样式 */
QScrollBar:vertical {
    background-color: rgba(255, 255, 255, 0.01);
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: rgba(255, 255, 255, 0.01);
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background-color: rgba(255, 255, 255, 0.01);
}
"""

def apply_blur_style(widget: QWidget) -> bool:
        """
        应用高斯模糊透明效果的样式到指定部件
        
        :param widget: 要应用样式的部件
        :return: 操作是否成功
        """
        try:
            widget.setStyleSheet(BLUR_STYLE)
            return True
        except Exception as e:
            return False