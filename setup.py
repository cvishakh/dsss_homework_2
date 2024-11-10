from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Name of the package
    version='2.1',  # Version of your package
    packages=find_packages(),  # Automatically find all packages
    install_requires=[],  # List any dependencies here (e.g., 'numpy', 'requests')
    entry_points={  # Define entry points for command-line scripts
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Command to run your math quiz
        ],
    },
)
