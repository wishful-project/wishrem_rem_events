from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='rem_events',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/wishful-project/wishrem_rem_events',
    license='Apache 2.0',
    author='Daniel Denkovski, Valentin Rakovic',
    author_email='{danield, valentin}@feit.ukim.edu.mk',
    description='REM events for sensing and rrm activities',
    long_description='REM events for sensing and rrm activities',
    keywords='sensing, rrm, events',
    #install_requires=['pyric', 'pyshark']
)
