from setuptools import setup, find_packages

setup(
    name='linkcounter',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.26.0',
        'beautifulsoup4==4.9.3',
        'tk==0.1.0'
    ],
    entry_points={
        'console_scripts': ['linkcounter=linkcounter_project.linkcounter:main',
                            'linkcounter_gui=linkcounter_project.gui:main'],
    },
)