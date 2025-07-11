# FE-Core

# 面子工程核心

## 项目简介

这是一个基于 PyQt5 实现的高斯模糊和透明效果的核心库，主要用于 Windows 平台。

## 安装

从源代码安装：

```bash
git clone https://github.com/Jimmy32767255/FE-Core.git
ren FE-Core fe_core
cd fe_core
pip install .
```

## 使用

以下是一个简单的使用示例：

```python
import sys
from PyQt5.QtWidgets import QApplication
from fe_core.window import BlurredWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlurredWindow()
    window.show()

    # 示例：设置窗口标题
    window.set_window_title("测试窗口")

    # 示例：禁用模糊效果
    # window.set_blur_effect(False)

    # 示例：设置窗口图标 (需要提供一个有效的图标文件路径)
    # window.set_window_icon("path/to/your/icon.png")

    # 示例：应用自定义模糊样式
    # from fe_core import apply_blur_style, BLUR_STYLE
    # apply_blur_style(window, BLUR_STYLE)

    sys.exit(app.exec_())
```

## 许可证

本项目使用 MIT 许可证。详情请参阅 `LICENSE` 文件。


## 许可证
[MIT License](LICENSE)