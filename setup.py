import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__versioon__="0.0.0"

REPO_NAME="Text_Summarizer_Project"
AUTHOR_USER_NAME="poojagrawal1915"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="poojagrawal1915@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__versioon__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)