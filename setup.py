from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='sydneyscript',
    version='0.6.1',
    license='MIT',
    author="Pooria Ahmadi",
    author_email='pooriababak444@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pooriaahmadi/sydneyscript',
    keywords='language interpreter sydney script',
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': ['src=sydneyscript:main'],
    },

)
