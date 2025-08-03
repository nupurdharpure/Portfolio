from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',       # or your specific version
        'gunicorn',          # required for deployment
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [],
    },
)
