# quadruped
Design and simulation of a quadruped from a passive dynamic walker

## Getting started
I use pipenv for library management, but [drake](https://drake.mit.edu/python_bindings.html#using-the-python-bindings) doesn't support pip.

To use drake with pip we first need to follow the instructions [here](https://drake.mit.edu/python_bindings.html#using-the-python-bindings)
```
# Setup drake, and run prerequisites.
curl -o drake.tar.gz https://drake-packages.csail.mit.edu/drake/nightly/drake-latest-xenial.tar.gz
mkdir -p .venv
tar -xvzf drake.tar.gz -C .venv --strip-components=1
# - You may need `sudo` here.
.venv/share/drake/setup/install_prereqs

# Setup a virtualenv over the drake install.
python2 -m virtualenv -p python2 .venv --system-site-packages
```

Then we run `export PIPENV_VENV_IN_PROJECT="enabled"` in order to mak

Then cd to the project directory and run:

```pipenv install```

Make sure drake is there with `python -c 'import pydrake; print(pydrake.__file__)'`


