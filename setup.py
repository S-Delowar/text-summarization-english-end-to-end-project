import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_desc = f.read()

__version__ = '0.0.0'
REPO_NAME = 'text-summarization-english-end-to-end-project'
AUTHOR_USERNAME = 'S-Delowar'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'sayed.buet97@gmail.com'

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USERNAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for NLP",
    long_description= long_desc,
    long_description_content_type= 'text/markdown',
    url= f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages= setuptools.find_packages(where='src')
)
