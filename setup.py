from setuptools import setup, find_packages

setup(
    name='wordcounter',
    version="0.1",
    packages=['wordcounter'],
    include_package_data=True,
    setup_requires=[
        'flask',
        'click'
    ],
    entry_points={
        'console_scripts': ['wordctr=wordcounter.app:main']
    }
)
