from setuptools import setup

setup(
    name='mex',
    version='1.0.1',
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
    author_email='705270564@qq.com',
    description='Match Expression'
)
