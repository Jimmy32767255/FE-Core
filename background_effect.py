#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现背景效果，例如高斯模糊，优先尝试 Windows 原生模糊。
"""

import ctypes
from ctypes import wintypes
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGraphicsBlurEffect

# Windows API definitions for blur
ACCENT_DISABLED = 0
ACCENT_ENABLE_GRADIENT = 1
ACCENT_ENABLE_TRANSPARENTGRADIENT = 2
ACCENT_ENABLE_BLURBEHIND = 3  # 使用这个状态
ACCENT_ENABLE_ACRYLICBLURBEHIND = 4 # Windows 10 1803+
ACCENT_INVALID_STATE = 5

class ACCENTPOLICY(ctypes.Structure):
    _fields_ = [
        ("AccentState", wintypes.DWORD),
        ("AccentFlags", wintypes.DWORD),
        ("GradientColor", wintypes.DWORD),
        ("AnimationId", wintypes.DWORD)
    ]

class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
    _fields_ = [
        ("Attribute", wintypes.DWORD),
        ("Data", ctypes.POINTER(ACCENTPOLICY)),
        ("SizeOfData", wintypes.ULONG)
    ]

# Function pointers
SetWindowCompositionAttribute = ctypes.windll.user32.SetWindowCompositionAttribute
SetWindowCompositionAttribute.argtypes = (wintypes.HWND, ctypes.POINTER(WINDOWCOMPOSITIONATTRIBDATA))
SetWindowCompositionAttribute.restype = wintypes.BOOL

class BackgroundEffect:
    """
    为窗口部件应用背景效果，例如高斯模糊。
    优先尝试使用 Windows 原生模糊效果。
    """
    def __init__(self, widget: QWidget, blur_radius: int = 25):
        """
        初始化背景效果。

        :param widget: 要应用效果的窗口部件 (通常是顶层窗口)。
        :param blur_radius: QGraphicsBlurEffect 的模糊半径 (备用方案)。
        """

        self.widget = widget
        self.hwnd = int(widget.winId())

        if not self._try_apply_native_blur():
            self.blur_effect_fallback = QGraphicsBlurEffect()
            self.blur_effect_fallback.setBlurRadius(blur_radius)
            self.widget.setGraphicsEffect(self.blur_effect_fallback)
            self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 0.01);")
        
    def _try_apply_native_blur(self) -> bool:
        """尝试应用 Windows 原生模糊效果。"""
        try:
            accent_policy = ACCENTPOLICY()
            # 尝试 ACCENT_ENABLE_BLURBEHIND
            accent_policy.AccentState = ACCENT_ENABLE_BLURBEHIND 
            accent_policy.AccentFlags = 0 # 保持简单
            accent_policy.GradientColor = 0 # 对于 BLURBEHIND 通常不使用颜色

            data = WINDOWCOMPOSITIONATTRIBDATA()
            data.Attribute = 19  # WCA_ACCENT_POLICY
            data.Data = ctypes.pointer(accent_policy)
            data.SizeOfData = ctypes.sizeof(accent_policy)

            success = SetWindowCompositionAttribute(self.hwnd, ctypes.pointer(data))
            if success:
                self.widget.update() # 强制重绘
                return True
            else:
                error_code = ctypes.get_last_error()
                return False
        except Exception as e:
            return False

    def set_blur_radius(self, radius: int): # Only relevant for QGraphicsBlurEffect fallback
        """
        设置 QGraphicsBlurEffect 的模糊半径 (仅当原生模糊失败时使用)。
        """
        if hasattr(self, 'blur_effect_fallback') and self.blur_effect_fallback:
            self.blur_effect_fallback.setBlurRadius(radius)

    def enable(self, enable: bool = True) -> bool: # Primarily for QGraphicsBlurEffect fallback
        """
        启用或禁用模糊效果。
        """
        if hasattr(self, 'blur_effect_fallback') and self.blur_effect_fallback:
            self.blur_effect_fallback.setEnabled(enable)
            status = "启用" if enable else "禁用"
            return True
        elif enable:
            return self._try_apply_native_blur()
        elif not enable: # Attempt to disable native blur
            try:
                accent_policy = ACCENTPOLICY()
                accent_policy.AccentState = ACCENT_DISABLED
                data = WINDOWCOMPOSITIONATTRIBDATA()
                data.Attribute = 19
                data.Data = ctypes.pointer(accent_policy)
                data.SizeOfData = ctypes.sizeof(accent_policy)
                return bool(SetWindowCompositionAttribute(self.hwnd, ctypes.pointer(data)))
            except Exception as e:
                return False
        return True