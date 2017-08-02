import sys
from setuptools import setup, find_packages

if sys.version_info < (3,5):
    sys.exit('Sorry, Python < 3.5 is not supported')

setup(name='gym_tictactoe',
      version='0.0.1',
      insatll_required=['gym', 'numpy', 'click', 'tqdm'],
      packages=find_packages()
      )
