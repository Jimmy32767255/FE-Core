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

或者，作为子模块安装：

```bash
git submodule add https://github.com/Jimmy32767255/FE-Core ./fe_core
```

## 使用方法

```python
from fe_core.window import BlurredWindow

# 创建窗口
window = BlurredWindow()

# 设置窗口标题
window.set_window_title("我的应用")

# 设置窗口图标
window.set_window_icon("path/to/icon.png")

# 设置窗口大小
window.set_window_size(1024, 768)

# 设置内容边距
window.set_content_margins(20, 20, 20, 20)

# 设置模糊效果
window.set_blur_effect(True)  # 启用模糊效果
window.set_blur_radius(30)    # 设置模糊半径

# 设置窗口透明度
window.set_window_opacity(0.95)

# 显示窗口
window.show()
```

## 许可证

本项目使用 MIT 许可证，详情请参阅[MIT License](LICENSE)。

## 已知问题

1. 在Windows11 Insider Preview Canary上高斯模糊效果失效，这个是微软的问题我无法修复，正式版Windows11上没有此问题。