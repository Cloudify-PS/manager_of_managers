from setuptools import setup, find_packages

setup(
    name='cloudify-manager-of-managers',
    version='2.0.2',
    author='Cloudify',
    author_email='hello@cloudify.co',
    packages=find_packages(include='cmom*'),
    description='Cloudify Manager of Managers plugin',
    install_requires=[
        'cloudify-common==4.5'
    ],
)
