from setuptools import setup

setup(
    name='mex',
    version='1.2.4',
    packages=[
        'mex'
    ],
    package_dir={'': 'src'},
    install_requires = [
        'nwae.utils'
    ],
    url='',
    license='',
    author='nwae',
    author_email='m5251@naver.com',
    description='Match Expression'
)
