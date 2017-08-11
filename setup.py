from setuptools import setup

setup(
    name='jinja2-lint',
    description='pre-commit hook for linting Jinja2 templates.',
    url='https://github.com/bdellegrazie/jinja2-lint',
    version='0.0.1',

    author='Brett Delle Grazie',
    author_email='brett.dellegrazie@gmail.com',

    classifiers=[
        'License :: OSI Approved :: DBAD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    py_modules=['j2_lint'],
    install_requires=[
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'jinja2-lint = j2_lint:main',
        ],
    },
)
