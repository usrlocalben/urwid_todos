from os.path import abspath, dirname, join
from setuptools import setup, find_packages

INIT_FILE = join(dirname(abspath(__file__)), 'urwid_todos', '__init__.py')

def get_version():
    with open(INIT_FILE) as fd:
        for line in fd:
            if line.startswith('__version__'):
                version = line.split()[-1].strip('\'')
                return version
        raise AttributeError('Package does not have a __version__')

setup(
    name='urwid_todos',
    description='Urwid Components using the Pydux state container',
    long_description=open('README.rst').read(),
    url="http://github.com/benjamin9999/urwid_todos/",
    version=get_version(),
    author='Benjamin Yates',
    author_email='benjamin@rqdq.com',
    packages=[
        'urwid_todos',
        'urwid_todos.actions',
        'urwid_todos.components',
        'urwid_todos.containers',
        'urwid_todos.reducers',
    ],
    install_requires=['urwid_pydux>=0.2.0'],
    scripts=['bin/urwid_todos'],
    license='MIT',
)
