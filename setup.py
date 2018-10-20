try: 
    from setuptools import setup
except ImortError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "author name here...",
    "url": "url to get it at",
    "download_url": "Where to download it",
    "author_email": "email here...",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["Demos"],
    "scripts": [],
    "name": "Demos"
}

setup(**config)
