# PDM - Personal Data Manager
This repository contains Python framework for personal data (name, address, phone number) management. 

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Example usage in script](#example-usage-in-script)
- [Command Line Interface](#cli)
- [API](#api)
- [Jenkinsfile](#jenkinsfile)
- [Tests](#tests)
- [License](#license)
- [Contact](#contact)

## Overview
Main idea behind this project is to allow users to easily transform their personal contact databases between dirrefent data formats. `pdm` is fully flexible and can be extended in any way by any data format. 

![overview](https://user-images.githubusercontent.com/25990328/50550463-c0620d80-0c71-11e9-972a-c8a9d8285db6.png)

It is all about the 'plugin' architecture, which allows to register any type of reader/writer for any data format. `pdm` supports itself at this moment CSV and JSON as the input formats and HTML and text as the output formats, but it can be easily extended by user's defined functions compatibile with [API](#api)

![detailed](https://user-images.githubusercontent.com/25990328/50550478-f4d5c980-0c71-11e9-90c6-a668e9f39c6b.png)

Registartation in plugins registry is very easy process. Configuration is split into two sections `INPUT_FORMATS` and `OUTPUT_FORMATS`. First level of configuration's data structure defines supported formats. Moreover each format can has defined alternate readers and writers which point to callable functions, but it is important, that every format should support ***defult*** reader/writer.

```python
from pdm.data_processors import csv, json, html, text

INPUT_FORMATS = {
    'csv': {
        'default': csv.read_csv
    },
    'json': {
        'default': json.read_json
    }
}

OUTPUT_FORMATS = {
    'text': {
        'default': text.write_text_output
    },
    'html': {
        'default': html.write_html_table
    }
}
```
Let's say we would like to add new input format 'xml' and add alternative reader for 'json format'. 
> Of course we assume, that 'pdm.data_processors.xml' module exists with 'read_xml' function which can handle xml parsing process. The same about 'read_json_with_better_engine' function in 'pdm.data_processors.json' module!!! 

Our plugins register should now look like that:
```python
from pdm.data_processors import csv, json, html, text, xml

INPUT_FORMATS = {
    'csv': {
        'default': csv.read_csv
    },
    'json': {
        'default': json.read_json
        'better_engine': json.read_json_with_better_engine
    }
    'xml': {
        'default': xml.read_xml
    }
}

OUTPUT_FORMATS = {
    'text': {
        'default': text.write_text_output
    },
    'html': {
        'default': html.write_html_table
    }
}
```

## Prerequisites
- Python 3.7.0 (should support without any problems older version)
- Will work on any OS (tested only on ArchLinux with kernel 4.18.10)

## Installation
You can install `pdm` using precompiled .whl package or by cloning source code of this repository. In both cases you need to make sure that `setuptools` package is already installed in you Python environment. You can check that by executing command (works only in linux/osx shell - for windows you need to find substitute of `grep` command):
```shell
$ pip list | grep setuptools
```
If there no output from above command, please install `setuptools` by typing:
```shell
$ pip install setuptools
```
After that, you can install 
- **.whl package directly...**
```shell
$ pip install /path/to/package.whl
```
- **or clone source code of this repository:**
```shell
$ git clone https://github.com/biniow/pdm
$ cd pdm
$ pip install .
```
Now `pdm` should be available in your Python PATH. Moreover `pdm-cli` should be available in your shell.

## Example usage in script
Plase take a look below at interactive Python session with `pdm`. It is so easy and great!
```python
>>> import pdm
>>> data_manager = pdm.PersonalDataManager.read_from('json', '/home/wojtek/data.json')
>>> data_manager.data_records
{_PersonalData(name='Mark', address='Australia', phone_number='+610000000'), _PersonalData(name='Bob', address='USA', phone_number='+100000000000')}
>>> data_manager.write_to('text', '/home/wojtek/out.txt', verbose=True)
Name: Mark
Address: Australia
Phone number: +610000000
====================
Name: Bob
Address: USA
Phone number: +100000000000
```

## CLI
`pdm` provides command line interfece in form of `pdm-cli` script which is automatically added to your path after installation.  You can us it in following way:
```
usage: pdm-cli [-h] [-l] [-s SPEC_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -l, --list-supported-formats
                        Prints currently supported formats
  -s SPEC_FILE, --spec-file SPEC_FILE
                        Path to file with input/output details specification
  -v, --verbose         Defines if verbose mode
```
* **-l** - prints currently supported formats and end script execution with status 0
* **-s** - it is something like a batch mode. You can define set of operations in SPEC FILE (json's structured) and run it automatically. It can be useful when you need to run the same set of operations on different data sets periodically. Example of SPEC file:
* **-v** - turns on verbose mode. All data processed by script will be printed on the screen
```json
[
        {
                "input_format": "json",
                "input_args": {
                        "input_file_path": "data.json"
                },
                "output_format": "html",
                "output_args": {
                        "output_file_path": "output.html"
                }
        },
        {
                "input_format": "csv",
                "input_args": {
                        "input_file_path": "data.csv"
                },
                "output_format": "text",
                "output_args": {
                        "output_file_path": "output.txt"
                }
        }
]
```
* in case when no option provided **interactive mode** starts. Moreover scripts show result of interactive session content in SPECFILE format, which can be saved for further usage. Example of interactive mode session:
```
wojtek@probook -> pdm-cli
How many data operation would you like to perform?: 2
========> Input data details
Select data format: json
Select method for json [default]: 
Absolute path to input file: /home/wojtek/data.json
========> Output data details
Select data format: html
Select method for html [default]: 
Absolute path to output file: /home/wojtek/out.html
========> Input data details
Select data format: csv
Select method for csv [default]: 
Absolute path to input file: /home/wojtek/data.csv
========> Output data details
Select data format: text
Select method for text [default]: 
Absolute path to output file: /home/wojtek/out.txt
For further executions you can use specfile with following content:
[{"input_format": "json", "input_args": {"method": "default", "input_file_path": "/home/wojtek/data.json"}, "output_format": "html", "output_args": {"method": "default", "output_file_path": "/home/wojtek/out.html"}}, {"input_format": "csv", "input_args": {"method": "default", "input_file_path": "/home/wojtek/data.csv"}, "output_format": "text", "output_args": {"method": "default", "output_file_path": "/home/wojtek/out.txt"}}]
Done...
```

## API
If you would like to become a `pdm` developer or just write own reader/writer, have on mind that all registered functions should be compatibile with API, which depends on plugin type (READER/WRITER):

**1. READER**
* Mandatory arguments order: `input_file_path` of type `str`, `verbose=False` od type `bool`
* Arguments: you can use as much arguments as you like, but rather preffered to use keywords arguments instead of positional
* Returned value: list of tuples of dict with personal data records. For instance: `[('Mark', 'Australia', '+610000000'), {name: 'Bob', address: 'USA', phone_number: '+100000000000}]`
* Example of reader function
```python
def read_csv(input_file_path, verbose=False, delimiter=','):
    """
    Function reads csv file and returns list of records
    :param input_file_path: path to csv file
    :param verbose: defines if verbose mode
    :param delimiter: fields separator in csv file
    :return: list of records
    """
    result = []
    with open(input_file_path) as csv_file:
        for row in csv.reader(csv_file, delimiter=delimiter):
            result.append(row)

    if verbose:
        print(result)

    return result
```

**2. WRITER**
* Mandatory arguments order: `data` of type `set`, `output_file_path` of type `str`, `verbose=False` or type `bool`
* Arguments: you can use as much arguments as you like, but rather preffered to use keywords arguments instead of positional
* Returned value: Not required, but status can be returned
* Example of writer function
```python
def write_text_output(data, output_file_path, verbose=False):
    """
    Function writes data to text file
    :param data: set of _PersonalData class objects
    :param output_file_path: path to output file
    :param verbose: defines if verbose mode
    """
    result = []
    for data_record in data:
        result.append(str(data_record))

    with open(output_file_path, 'w') as result_file:
        txt_output = '\n====================\n'.join(result)
        result_file.write(txt_output)

        if verbose:
            print(txt_output)
```


## Jenkinsfile
`pdm` is also shipped with Jenkinsfile which can be used in Jenkin's pipelines verification process.

## Tests
**1. UT**
You can run unit tests for this project by typing from main dir of cloned repository:
```
$ python -m unittest discover pdm.test
```
If you need to have coverage report try this:
```
$ pip install coverage
$ coverage run -m unittest discover pdm.tests
$ coverage report -m
```

**2.Pylint**
`pdm` has own Pylint rcfile configuration which should be used to run pylint tests
```
$ pylint pdm --rcfile=config.rcfile
```

## License
[MIT](https://github.com/biniow/pdm/blob/master/LICENSE)

## Contact
If you have any questions of would like to become a port of the development team, do not hesitate to contact me at: wojtek.biniek@gmail.com
