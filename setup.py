from setuptools import setup

setup(
    name="pysv",
    version="0.1.0",
    packages=["pysv"],
    install_requires=["prompt_toolkit", "click", "pyperclip"],
    entry_points={"console_scripts": ["pysv = pysv.__main__:main"]},
)
