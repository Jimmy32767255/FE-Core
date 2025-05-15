#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
主程序入口
"""

import sys
from loguru import logger
from PyQt5.QtWidgets import QApplication
from window import BlurredWindow


def setup_logger():
    """
    配置日志记录器
    """
    logger.remove()  # 移除默认处理程序
    logger.add(
        "app.log",
        rotation="10 MB",
        retention="1 week",
        level="INFO",
        encoding="utf-8",
    )
    logger.add(sys.stderr, level="INFO")  # 同时输出到控制台


def main():
    """
    程序主入口
    """
    setup_logger()
    logger.info("应用程序启动")
    
    app = QApplication(sys.argv)
    window = BlurredWindow()
    window.show()
    
    exit_code = app.exec_()
    logger.info("应用程序退出，退出码: {}", exit_code)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())