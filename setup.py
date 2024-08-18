from setuptools import setup, find_packages

setup(
    name='MockOrderDataStructured',
    version='1.1.0',
    description='A package for structuring and test data.',
    author='eventually',
    author_email='ferry792351742@gmail.com',
     url='https://github.com/eventually11/MockOrderDataStructured',
    packages=find_packages(where="src"),
    package_dir={"": "src"},  
    entry_points={
        'console_scripts': [
            'run_script=scripts.run_script:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)