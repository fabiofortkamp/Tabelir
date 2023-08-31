# Tabelir

[![PyPI](https://img.shields.io/pypi/v/Tabelir.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/Tabelir.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/Tabelir)][python version]
[![License](https://img.shields.io/pypi/l/Tabelir)][license]

[![Read the documentation at https://Tabelir.readthedocs.io/](https://img.shields.io/readthedocs/Tabelir/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/fabiofortkamp/Tabelir/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/fabiofortkamp/Tabelir/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/Tabelir/
[status]: https://pypi.org/project/Tabelir/
[python version]: https://pypi.org/project/Tabelir
[read the docs]: https://Tabelir.readthedocs.io/
[tests]: https://github.com/fabiofortkamp/Tabelir/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/fabiofortkamp/Tabelir
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Overview

In many Engineering simulations, engineers need _fluid tables_ of various thermophysical
properties tabulated by pressure and temperature. In even more specific situations,
properties should be tabulated by pressure and _enthalpy_, allowing them to be extracted
from the solution of momentum and energy equations.

Tabelir is a fluid tables generator that performs this task. You invoke it with:

```shell
tabelir "Methane"
```

and a new folder called `Methane` is created in the working directory, with lots
of CSV tables named like this:

- `temperature_GAS_density.csv`
- `enthalpy_MIXTURE_cp.csv`
- `temperture_equivLIQUID_viscosity.csv`

where:

- the first string denotes the other parameter (in addition to pressure);
- the second string denotes the phase (where `equivLIQUID` is an equivalent, lumped
  liquid phase)
- the third string denotes the property that is being tabulated

The table looks like this:

```csv
pressure/temperature,T1,T2,T3
P1,value11,value12,value13
P2,value21,value22,value23
```

Beware that, if a folder called `Methane` (or whatever you passed in the command line)
exists, it will be overwritten!

## Features

- [CoolProp](http://www.coolprop.org) as the data source

## TODO

- [ ] Generate enthalpy-based tables
- [ ] Customize range
- [ ] Make possible to customize output directory
- [ ] Add guard against existing directory

## Installation

Tabelir is tested with Python versions 3.8-3.11.

You can install _Tabelir_ via [pip] from [PyPI]:

```console
$ pip install Tabelir
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Tabelir_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/fabiofortkamp/Tabelir/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/fabiofortkamp/Tabelir/blob/main/LICENSE
[contributor guide]: https://github.com/fabiofortkamp/Tabelir/blob/main/CONTRIBUTING.md
[command-line reference]: https://Tabelir.readthedocs.io/en/latest/usage.html
