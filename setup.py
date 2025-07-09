from setuptools import setup, find_packages

setup(
    name='fe_core',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'loguru==0.7.2',
        'PyQt5==5.15.10',
    ],
    author='Jimmy32767255',
    author_email='Jimmy32767255@outlook.com',
    description='A core library for Gaussian blur and transparency effects with PyQt5',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jimmy32767255/FE-Core',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)