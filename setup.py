import setuptools

setuptools.setup(
    name="sfs",
    version="0.2.0",
    packages=setuptools.find_packages(where="sfs"),
    install_requires=[
        "statsmodels>=0.12.2",
        "pandas>=1.2.4",
        "numpy>=1.20.0",
        "scipy>=1.6.0",
        "joblib",
        "tqdm",
        "streamlit",
        "stqdm"
    ],
    python_requires=">=3.7.9",
    classifiers=[
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
        "Programming Language :: Python :: 3.9"
    ],
)
