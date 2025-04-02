import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "mlop-project"
Author_USER_NAME = "tripti882"
SRC_REPO ="mlop"
Author_EMAIL ="triptij910@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_USER_NAME, 
    author_email=Author_EMAIL,
    description="A small python package for nlp app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker": f"https://github.com/{Author_USER_NAME}/{REPO_NAME}/issues",

},
package_dir={"": "src"},
packages=setuptools.find_packages(where="src")
)

