import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='scrapy-scraperapi-middleware',
    version='0.1',
    license='MIT',
    description='Middleware to easily implement ScraperAPI in Scrapy projects',
    long_description_content_type='text/markdown',
    long_description=README,
    python_requires='>=3',
    project_urls={
        "Source": "https://github.com/patkle/scrapy-scraperapi-middleware",
    },
    keywords='scrapy middleware proxy ScraperAPI',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    author='Patrick Klein',
    packages=['scrapy_scraperapi_middleware'],
    install_requires=[
        'importlib-metadata ~= 1.0 ; python_version < "3.8"',
        'scrapy'
    ]
)
