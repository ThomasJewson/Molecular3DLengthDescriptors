import setuptools

with open("README.md", encoding="utf8") as readme_file:
    long_description = readme_file.read()

requirements = ["pandas>=0.2", "numpy>=1", "matplotlib>=3"]

setuptools.setup(
    name='Molecular3DLengthDescriptors',
    version="1.0.0",
    author='Thomas Jewson',
    py_modules=['Molecular3DLengthDescriptors.Molecular3DLengthDescriptors'],
    author_email="t.jewson1@gmail.com",
    description='A 3D conformational based molecular descriptor set.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasJewson/Molecular3DLengthDescriptors",
    packages=setuptools.find_packages(),
    install_requires= requirements,
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
],  
)
