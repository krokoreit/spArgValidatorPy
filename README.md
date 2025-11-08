# spArgValidatorPy

[![PyPI - Version](https://img.shields.io/pypi/v/spArgValidatorPy.svg)](https://pypi.org/project/spArgValidatorPy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spArgValidatorPy.svg)](https://pypi.org/project/spArgValidatorPy)


This package provides a Python module validating function arguments and either raising an exception or returning the validated value.

When an argument for a numeric value is given as a string representation (e.g. "100" or "3.24"), it is converted and returned as a valid integer or float value, unless validation is done in strict mode. It is also possible to validate numeric values against limits by specifying a minimum value, a maximum value or both.

A value for a string argument is treated as valid, when such value can be converted to a string (e.g. 123 becomes "123"), unless validation is done in strict mode, which will only accept values of type str. By default strings are validated against a minimum length of 1, meaning that empty strings will throw an exception. This can be disabled by validation with a minimum length of 0. Similarly, strings can be validated against a minimum length of e.g. 10 characters.

All validation functions have an optional 'default' argument, which - instead of an exception thrown - is returned in case the validation fails. This simplifies coding, as it avoids the need to wrap a validation function with a try: .. except: block to set a specific fallback value.

Equally, validation functions for numeric values have an optional 'return_limits' argument, which, when set to True, causes the function to return a set minimum or maximum value instead of throwing an exception when this limit is exceeded.


Enjoy

&emsp;krokoreit  
&emsp;&emsp;&emsp;<img src="assets/krokoreit-01.svg" width="140"/>


## Installation

```console
pip install spArgValidatorPy
```


## Usage & API

### ArgValidator Class
Import module:
```py
  from spArgValidatorPy import ArgValidator

  obj = ArgValidator()
```


</br>

### API

#### Methods
* [aaa()](#aaa-method)  
* [bbb()](#bbb-method)  


#### aaa() Method
```py
  get_zoneinfo_utc()
```



<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>


</br>

## License
MIT license  
Copyright &copy; 2025 by krokoreit
