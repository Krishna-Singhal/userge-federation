import re
import setuptools

with open("userge_fed/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

setuptools.setup(
    name="userge_fed",
    version=version,
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
    # package_data={"userge_fed": ["__init__.py", "client.py", "errors.py"]},
    packages=['userge_fed'],
    python_requires=">=3.6",
)
