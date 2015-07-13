#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = """Library to interact with the Packet API"""

if os.path.isfile("README.md"):
    with open('README.md') as file:
        long_description = file.read()

setup(
    name='packet-python',
    version='1.0',
    description='Library to interact with the Packet API',
    author='Aaron Welch ( https://www.packet.net/about/team/aaron-welch/ )',
    author_email='"welch@packet.net',
    url='https://github.com/packethost/packet-python',
    packages=['packet'],
    install_requires=['requests'],
    license='GNU Lesser General Public License',
    long_description=long_description
)
