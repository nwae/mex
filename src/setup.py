from setuptools import setup

setup(
    name='mex',
    version='1.5.3',
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
    author_email='mapktah@ya.ru',
    description='Match Expression'
)
