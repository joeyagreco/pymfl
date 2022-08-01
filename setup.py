import setuptools

from _version import __version__ as version

with open("README.md") as f:
    read_me = f.read()

with open("LICENSE") as f:
    license_ = f.read()

setuptools.setup(
    name="pymfl",
    version=version,
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Python wrapper for the myfantasyleague API.",
    long_description_content_type="text/markdown",
    long_description=read_me,
    license=license_,
    include_package_data=True,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["setuptools"]
)
