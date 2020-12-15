from setuptools import setup, find_packages
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setup(
  name='manhattandistance',
  version='0.0.1',
  description='Calculates the Manhattan Distance of two places',
  long_description=open('README.md').read() +  open('CHANGELOG.txt').read(),
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
  keywords='distance', 
  packages=find_packages(),
  python_requires='>=3.6',
)