from setuptools import setup, find_packages

setup(
    name='wodpy',
    version='1.5.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A parser for the WOD data format, described in http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/IQuOD/wodpy',
    author='Simon Good, Bill Mills',
    author_email='mills.wj@gmail.com'
)
