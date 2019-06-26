from setuptools import setup

setup(
    name="Snapshotalyzer-30000",
    version="0.1",
    author="Aaron Banks",
    author_email="yeah_right@rabbithole.my",
    description="Snapshotalyzer-30000 is a tool to manage AWS EC2 snaphots",
    licence="GPLv3+",
    packages=["shotty"],
    url="https://github.com/VanntheRed/snapshotalyzer-30000",
    install_requires=[
        "click",
        "boto3"
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
