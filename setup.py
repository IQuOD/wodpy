from setuptools import setup, find_packages

setup(
    name='wodpy',
    version='1.6.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    long_description='See https://github.com/IQuOD/wodpy',
    description='A parser for the WOD data format, described in http://data.nodc.noaa.gov/woa/WOD/DOC/wodreadme.pdf',
    install_requires=['numpy', 'pandas'],
    url='https://github.com/IQuOD/wodpy',
    author='Simon Good, Bill Mills',
    author_email='mills.wj@gmail.com'
)
