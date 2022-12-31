from setuptools import setup

setup(
    name="walking_girl",
    version="0.0.1",
    packages=["walking_girl"],
    entry_points={
        "console_scripts": [
            "walking_girl = walking_girl.__main__:main"
        ]
    },
    install_requires=["pygame"]
)