from setuptools import setup, find_packages

setup(
    name='flowcleanser',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    entry_points={
        'console_scripts': [
            'flowcleanser=flowcleanser.main:main',
        ],
    },
    author='Daniil Mishchenko',
    author_email='dany.mishchenko@gmail.com',
    description='A tool for removing industrial process launches GitHub Actions',
    keywords='github actions api delete',
    url='git@github.com:MishchenkoDaniil/FlowCleanser.git',
)
