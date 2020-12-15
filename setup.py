from setuptools import setup, find_packages
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setup(
  name='manhattandistance',
  py_modules=["utils"],
  version='1.1.1',
  description='Calculates the Manhattan Distance of two places',
  long_description=open('README.md').read() + "\n\n" + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='http://packages.python.org/manhattandistance',  
  author='Dionysios Rigatos',
  author_email='dion.rigatos@gmail.com',
  license='MIT License', 
  classifiers=[
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
              ],
  packages=find_packages(),
  keywords='distance', 
)