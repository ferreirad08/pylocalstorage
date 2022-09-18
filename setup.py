from setuptools import setup, find_packages

with open('README.md', 'r') as readmefile:
    readme = readmefile.read()

setup(
    name='pylocalstorage',
    version='1.2.0',
    author='David Ferreira',
    author_email='ferreirad08@gmail.com',
    description='A package to store data on the hard disk (HD) and make it available to all Python applications running locally!',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ferreirad08/pylocalstorage',
    packages=find_packages(','),
    install_requires=['SQLAlchemy'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    project_urls={
        "Source": "https://github.com/ferreirad08/pylocalstorage",
    }
)
