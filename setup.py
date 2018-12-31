from setuptools import setup

setup(name='pdm',
      version='1.2.0',
      description='Python framework for personal data (name, address, phone number) management',
      url='https://github.com/biniow/pdm',
      author='Wojciech Biniek',
      author_email='wojtek.biniek@gmail.com',
      license='MIT',
      packages=['pdm', 'pdm.data_processors'],
      scripts=['bin/pdm-cli'],
      zip_safe=False)
