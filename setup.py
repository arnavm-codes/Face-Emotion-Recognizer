import setuptools

# if in future, to publish as pypi package
# reads README.md description and write it to the pypi package page
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Face-Emotion-Recognizer"
AUTHOR_USER_NAME = "arnavm-codes"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "forarnavm2004@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="small python package for cnn app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"}
)
    