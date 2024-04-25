# Import necessary functions from setuptools
from setuptools import setup, find_packages

# Call the setup function to start defining the metadata and other details about your package
setup(
    # The name of the package. This is how users will install it via pip (e.g., pip install name_of_your_package)
    name='name_of_your_package',
    
    # The current version of your package. Change this number as you release new versions.
    version='0.0.1',
    
    # Automatically find all sub-packages within the package directory so they can be included in the distribution
    packages=find_packages(),
    
    # List of other Python packages required by your package. Users will have these installed automatically when they install your package.
    install_requires=[
        'pandas==2.2.2',  # Specifying an exact version of pandas that your package depends on
    ],
    
    # Metadata: The name of the author of the package
    author='',
    
    # Metadata: The email address of the author
    author_email='',
    
    # Metadata: A short, one-line description of the package
    description='',
    
    # Metadata: A long description of the package. This is typically detailed and can be the contents of README.md
    long_description=open('README.md').read(),
    
    # Metadata: Specifying the type of the long description. Since README.md is usually in Markdown, the type is 'text/markdown'
    long_description_content_type='text/markdown',
)
