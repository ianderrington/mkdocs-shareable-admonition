from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='mkdocs-shareable-admonition',
    version='0.1.1',
    description='An MkDocs plugin to create shareable admonitions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown',
    url='https://github.com/ianderrington/mkdocs-shareable-admonition',  # Update this URL
    author='Your Name',  # Update with your name
    author_email='ian.derrington@example.com',  # Update with your email
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'shareable_admonition = shareable_admonition:ShareableAdmonitionPlugin'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
