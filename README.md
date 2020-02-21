# e-Attestations CLI

A set of Python scripts that build the e-Attestations CLI

```python
'''
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.     ║
║  e-Attestations.com  - Third-Party Management Solutions & Services                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.      ║
║  All right reserved/Tous droits réservés                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓,       ║
║                  _   _            _        _   _                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓,     ▓  ║
║             /\  | | | |          | |      | | (@)                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.     ▓▓  ║
║  ___       /  \ | |_| |_ ___  ___| |_ __ _| |_ _  ___  _ __  ___   ___ ___  _ __ ___    ▓▓▓▓▓▓▓▓▓▓▓▓▓,      ▓▓▓  ║
║ / _ \  __ / /\ \| __| __/ _ \/ __| __/ _` | __| |/ _ \| '_ \/ __| / __/ _ \| '_ ` _ \   ▓▓▓▓▓▓▓▓▓▓▓▓,     .▓▓▓▓  ║
║|  __//__ / ____ \ |_| ||  __/\__ \ || (_| | |_| | (_) | | | \__ \| (_| (_) | | | | | |   .▓▓▓▓▓▓▓▓▓.     ,▓▓▓▓▓  ║
║ \___/   /_/    \_\__|\__\___||___/\__\__,_|\__|_|\___/|_| |_|___(_)___\___/|_| |_| |_|      .▓▓▓▓▓      ,▓▓▓▓▓▓  ║
║                                                                                                .,      .▓▓▓▓▓▓▓  ║
║                                                                                         ▓,           ,▓▓▓▓▓▓▓▓▓  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
:: e-Attestations.com (https://www.e-attestations.com) :: \ö/ ★★★★ 😎
'''
```

We're sharing here few of our Python scripts that helps us every day.

Enjoy !

Each sub directory contains a specific Python module with one or few scripts that are most of the time CLI script (using Click lib).

## Prerequisites 

- Python3 : is the mandatory language level since Python 2.x is no longer supported
- pip : is used to build a python module (checkout setup.py)
- virtualenv : is the also needed for Python env isolation for each module when you develop

If you want to learn more about this practicies :

[Check out this article](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


## Upgrade your setuptools belt

```sh
(.venv) $ deactivate
$ source 

```

## Develop

First, Go to the directory/module of your choice.

### Install a virtualenv

```sh
(.another-venv)$ cd address
(.another-venv)$ deactivate # if any already installed virtualenv active
$ virtualenv .venv --python=python3
$ source .venv/usr/local/bin/activate
(.venv) $ python -m pip install --upgrade pip setuptools wheel
```

### Install the module setup

```sh
pip install --editable .
```

Then, enjoy the simplicyty of launching your module by calling it on the command line:

```sh
$ address search --help

Usage: address search [OPTIONS] [FRAGMENT]

  Send a request to Open API Address and format the responses The error is
  accessible through the verbose mode

Options:
  --help  Show this message and exit.
```
