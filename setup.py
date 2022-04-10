from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

setup(
    name='parse-helper',
    version='0.1.22',
    description='Helpers to fetch & parse text on pages with requests, lxml, & beautifulsoup4',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/parse-helper',
    download_url='https://github.com/kenjyco/parse-helper/tarball/v0.1.22',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    entry_points={
        'console_scripts': [
            'ph-ddg=parse_helper.scripts.ddg:main',
            'ph-download-file-as=parse_helper.scripts.download_file_as:main',
            'ph-download-files=parse_helper.scripts.download_files:main',
            'ph-soup-explore=parse_helper.scripts.soup:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Utilities',
    ],
    keywords=['parse', 'requests', 'duckduckgo', 'cli', 'command-line', 'download', 'soup', 'beautifulsoup', 'lxml', 'helper', 'kenjyco']
)
