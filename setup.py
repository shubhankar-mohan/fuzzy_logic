import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzy_logics",
    version="0.1.2",
    author="Shubhankar Mohan",
    author_email="mohanshubhankar@gmail.com",
    description="The library provides functions for fuzzy string matching, fuzzy round-off for floats and a fuzzy "
                "function of dividing a integer into a integer distribution according to given percentage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhankar-mohan/fuzzy_logic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
      ],
    python_requires='>=3.5',
    include_package_data=True,
)
