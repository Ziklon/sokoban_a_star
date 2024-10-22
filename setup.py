from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import unittest

class CustomTestCommand(TestCommand):
    
    def run(self):
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

setup(
    name='sokoban',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'sokoban=app.main:main',
        ],
    },
    extras_require={
        'dev': ['pytest', 'flake8', 'unittest'],  # Development dependencies (e.g., testing, linting)
    },
    cmdclass={
        'test': CustomTestCommand,
    },
    author='Wilber Torres',
    description='A brief description of the project',
    license='MIT',
)