import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RedisModelBroker",
    version="0.0.1",
    author="James Truxon",
    author_email="james@modeic.com",
    description="Python tool for loading and coordinating multiple pre-trained deep neural net models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtruxon/RedisModelBroker",
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Windows",
        "Framework :: Robot Framework",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Programming Language :: Python :: 3.5",
    ),
    keywords=['neural network',],
    test_suite='test',
    install_requires=['flask-restplus', 'tensorflow','pandas','aioredis'],
)
