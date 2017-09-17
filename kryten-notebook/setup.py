import os
from distutils.util import convert_path

from pip.req import parse_requirements
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


# ========================================
# Parse requirements for all configuration
# ========================================
install_reqs = parse_requirements(filename=os.path.join('.', 'requirements.txt'), session='update')
reqs = [str(ir.req) for ir in install_reqs]
# ========================================
# Readme
# ========================================
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
# ========================================
# Version parsing
# ========================================
main_ns = {}
ver_path = convert_path('notebook/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


setup(
    name='kryten-notebook',
    version=main_ns['__version__'],
    packages=find_packages(),
    include_package_data=True,
    license='Apache License',  # example license
    description='Kryten Notebook is a simple Django app to display and execute Jupyter notebooks.',
    long_description=README,
    url='http://github.com/lordoftheflies/kryten-notebook',
    author='László Hegedűs',
    author_email='laszlo.hegedus@cherubits.hu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=reqs,
    private_repository="https://pypi.cherubits.hu"
)
