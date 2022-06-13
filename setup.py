from setuptools import setup, find_packages


setup(
    name='sydneyscript',
    version='0.6',
    license='MIT',
    author="Pooria Ahmadi",
    author_email='pooriababak444@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pooriaahmadi/sydneyscript',
    keywords='language interpreter sydney script',
    install_requires=[
    ],

)
