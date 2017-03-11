from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

setup(
    name='parse-helper',
    version='0.1.1',
    description='Helpers to fetch & parse text on pages with requests, lxml, & beautifulsoup4',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/parse-helper',
    download_url='https://github.com/kenjyco/parse-helper/tarball/v0.1.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'lxml',
        'beautifulsoup4',
    ],
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '' : ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
    ],
    keywords = ['parse', 'soup', 'beautifulsoup', 'lxml', 'helper']
)
