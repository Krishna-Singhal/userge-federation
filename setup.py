import re
import setuptools
from UsergeAntiSpamApi import __version__

setuptools.setup(
    name="UsergeAntiSpamApi",
    version=__version__,
    author="Krishna-Singhal",
    author_email="ylikehits3@gmail.com",
    description="wrapper for https://api.userge.tk",
    url="https://github.com/Krishna-Singhal/userge-federation",
    project_urls={
        "Bug Tracker": "https://github.com/Krishna-Singhal/userge-federation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=['UsergeAntiSpamApi'],
    python_requires=">=3.6",
)
