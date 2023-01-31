'''
Copyright 2023 Paolo Smiraglia <paolo.smiraglia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from setuptools import find_packages, setup

from cmdbuild import version


def get_requirements():
    requirements = []
    with open('requirements.txt', 'r') as fp:
        requirements = [line.strip() for line in fp.readlines()]
        fp.close()

    if not requirements:
        emsg = 'Unable to obtain requirements list'
        raise Exception(emsg)

    return requirements


def long_description():
    with open('README.md', 'r') as fp:
        lines = fp.readlines()
        fp.close()
    return ''.join(lines)


setup(
    name='cmdbuild',
    version=version,
    python_requires='>=3.6',

    author='Paolo Smiraglia',
    author_email='paolo.smiraglia@gmail.com',
    description='CMDBuild Python SDK',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/psmiraglia/python-cmdbuild',

    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements()
)
