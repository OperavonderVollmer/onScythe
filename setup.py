from setuptools import setup, find_packages

setup(
    name="onScythe",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
    ],
    python_requires=">=3.7",
    author="Opera von der Vollmer",
    description="OnScythe is an automated visual recognition and clicking script that detects specified images on-screen and interacts with them dynamically. It is designed for efficiency, incorporating configurable delays, randomized clicking, and robust error handling to ensure precise automation. Can be used standalone or as a module for other projects.",
    url="https://github.com/OperavonderVollmer/OnScythe", 
    license="MIT",
)
