from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='sydneyscript',
    version='0.6.4',
    license='MIT',
    author="Pooria Ahmadi",
    author_email='pooriababak444@gmail.com',
    packages=['sydneyscript'],
    url='https://github.com/pooriaahmadi/sydneyscript',
    keywords='language interpreter sydney script',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'sydneyscript = sydneyscript:main'
        ],
    },

)
