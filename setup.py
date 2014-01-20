
from distutils.core import setup

setup(name='pyLight',
      version='0.1',
      description='BSE enhancement tool',

      author='Jake Ross',
      author_email='jirhiker@gmail.com',
      scripts=['pylight'],
      packages=['src'],
      package_data={'src':['icons/*.png']}
      )

