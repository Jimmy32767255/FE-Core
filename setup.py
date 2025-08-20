"""
FE-Core 包安装配置文件

此文件定义了Python包的元数据、依赖关系和安装配置。
使用setuptools作为构建工具，支持PyPI发布和本地安装。
"""
from setuptools import setup, find_packages

# 主配置函数，定义包的所有元数据和依赖关系
setup(
    # 基础包信息
    name='fe_core',  # 包的名称，用于pip安装和导入
    version='0.1.0',  # 包的版本，遵循语义化版本规范
    packages=find_packages(),  # 自动查找项目中的所有Python包
    
    # 依赖管理
    install_requires=[  # 包的依赖列表，pip会自动安装这些依赖
        'PyQt5==5.15.10'  # PyQt5库，指定版本以确保兼容性
    ],
    author='Jimmy32767255',  # 作者名称
    author_email='Jimmy32767255@outlook.com',  # 作者邮箱
    description='A core library for Gaussian blur and transparency effects with PyQt5',  # 包的简短描述
    long_description=open('README.md', encoding='utf-8').read(),  # 包的详细描述，从 README.md 读取
    long_description_content_type='text/markdown',  # 详细描述的内容类型
    url='https://github.com/Jimmy32767255/FE-Core',  # 项目的 URL
    classifiers=[  # 分类器列表，用于描述包的元数据
        'Programming Language :: Python :: 3',  # 编程语言为 Python 3
        'License :: OSI Approved :: MIT License',  # 许可证为 MIT License
        'Operating System :: Microsoft :: Windows',  # 操作系统为 Windows
    ],
    python_requires='>=3.6',  # 要求的 Python 版本
)