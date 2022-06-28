from setuptools import setup, find_packages

with open('README.md', 'r') as readmefile:
    readme = readmefile.read()

setup(
    name='pylocalstorage',
    version='1.0.0',
    author='David Ferreira',
    author_email='ferreirad08@gmail.com',
    description='A package to store data on hard disk (HD) and make it available to all Python applications running in parallel!',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ferreirad08/pylocalstorage',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.6',
)
