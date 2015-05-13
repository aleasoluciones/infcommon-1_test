from setuptools import setup, find_packages

setup(name='common',
      version='0.0.1',
      author='Bifer Team',
      description ='felix platform commonlib',
      platforms = 'Linux',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests'])
      )

