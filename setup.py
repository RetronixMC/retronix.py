import setuptools as st
with open("README.md", "r") as f:
    ld = f.read()
import retronix as r
st.setup(
    name="retronix.py-benfosterdev",
    version=r.__version__,
    author="Ben Foster",
    author_email="ben@benfoster.dev",
    description="A Python library for the interaction with the Retronix public API",
    long_description=ld,
    long_description_content_type="text/markdown",
    url="https://github.com/retronixmc/retronix.py",
    packages=st.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant"
    ],
    python_requires='>=3.7'
)