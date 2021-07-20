# Risk of Rain 2 Run Parser

RunParser is a Python library for parsing and reading save data from Risk of Rain 2.

```python
>>> from runparser import RunParser
>>> rp = RunParser('tests/files/runs/', 'tests/files/profiles')    
>>> rp.parse_runs()
>>> rp.runs[0].guid
'1e610e1c-08f9-4321-af86-31fa772d9cd6'
>>> rp.runs[0].players[0].name
'Azure'
```

![Unit Test Status](https://github.com/Azure-Agst/ror2_run_parser/actions/workflows/unittest.yml/badge.svg?branch=main)

## Installing

At the moment, the module is not uploaded to pypi, so importing as a submodule is your best bet.

```bash
$ git submodule add https://github.com/Azure-Agst/ror2_run_parser/
```

## Testing

```bash
# activate virtual env
python3 -m venv venv
./venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run unit tests
python3 -m unittests -v tests
```

## Contributing

It's welcome! Just follow the rules in [CONTRIBUTING.md](https://github.com/Azure-Agst/ror2_run_parser/blob/main/CONTRIBUTING.md) and we'll be good to go!
