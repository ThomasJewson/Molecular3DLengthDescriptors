#import setuptools
#
#with open("README.md", encoding="utf8") as readme_file:
#    long_description = readme_file.read()
#
#requirements = ["pandas>=0.2", "numpy>=1", "matplotlib>=3"]
#
#setuptools.setup(
#    name='Molecular3DLengthDescriptors',
#    version="1.0.0",
#    author='Thomas Jewson',
#    py_modules=['Molecular3DLengthDescriptors.Molecular3DLengthDescriptors'],
#    author_email="t.jewson1@gmail.com",
#    description='A 3D conformational based molecular descriptor set.',
#    long_description=long_description,
#    long_description_content_type="text/markdown",
#    url="https://github.com/ThomasJewson/Molecular3DLengthDescriptors",
#    packages=setuptools.find_packages(),
#    install_requires= requirements,
#    python_requires='>=3',
#    classifiers=[
#        "Programming Language :: Python :: 3",
#        "License :: OSI Approved :: MIT License",
#],  
#)
from distutils.core import setup
setup(
  name = 'Molecular3DLengthDescriptors',         # How you named your package folder (MyLib)
  packages = ['Molecular3DLengthDescriptors'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A 3D conformational based molecular descriptor set.',   # Give a short description about your library
  author = 'Thomas Jewson',                   # Type in your name
  author_email = 't.jewson1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ThomasJewson/Molecular3DLengthDescriptors',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ThomasJewson/Molecular3DLengthDescriptors/archive/refs/tags/1.0.0.tar.gz',    # I explain this later on
  keywords = ['Molecular', 'Descriptor', '3D', 'Length', 'RDKit'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    "Programming Language :: Python :: 3",
  ],
)
