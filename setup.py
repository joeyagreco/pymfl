import setuptools

pkg_vars = dict()
with open("pymfl/_version.py") as f:
    exec(f.read(), pkg_vars)

with open("README.md") as f:
    read_me = f.read()

setuptools.setup(
    name="pymfl",
    version=pkg_vars["__version__"],
    author="Joey Greco",
    author_email="joeyagreco@gmail.com",
    description="Python wrapper for the myfantasyleague API.",
    long_description_content_type="text/markdown",
    long_description=read_me,
    license="MIT",
    include_package_data=True,
    packages=setuptools.find_packages(exclude=("test", "docs")),
    install_requires=["setuptools",
                      "configparser",
                      "requests"]
)
