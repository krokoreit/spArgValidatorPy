# spArgValidatorPy

[![PyPI - Version](https://img.shields.io/pypi/v/spArgValidatorPy.svg)](https://pypi.org/project/spArgValidatorPy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spArgValidatorPy.svg)](https://pypi.org/project/spArgValidatorPy)


This package provides a Python module validating function arguments and either raising an exception or returning the validated value.

When an argument for a numeric value is given as a string representation (e.g. "100" or "3.24"), it is converted and returned as a valid integer or float value, unless validation is done in strict mode. It is also possible to validate numeric values against limits by specifying a minimum value, a maximum value or both.

A value for a string argument is treated as valid, when such value can be converted to a string (e.g. 123 becomes "123"), unless validation is done in strict mode, which will only accept values of type str. By default strings are validated against a minimum length of 1, meaning that empty strings will throw an exception. This can be disabled by validation with a minimum length of 0. Similarly, strings can be validated against a minimum length of e.g. 10 characters.

All validation functions have an optional 'default' argument, which - instead of an exception thrown - is returned in case the validation fails. This simplifies coding, as it avoids the need to wrap a validation function with a try: .. except: block to set a specific fallback value. Note, that this value has to be given as an keyword argument (i.e. 'default=value') with value being the correct type (i.e. str, int or float).

Equally, validation functions for numeric values have an option to return the set minimum or maximum value instead of throwing an exception, when setting the keyword argument 'return_limits=True'.

For more details see below API explanation and over 20 examples given in the example01.py file (examples folder).

Enjoy

&emsp;krokoreit  
&emsp;&emsp;&emsp;<img src="assets/krokoreit-01.svg" width="140"/>


## Installation

```console
pip install spArgValidatorPy
```


## Usage & API

### ArgValidator Class
Import module and instantiate an ArgValidator object:
```py
  from spArgValidatorPy import ArgValidator

  av = ArgValidator()
```

Argument validation is then as simple as
```py
  def my_function(str_arg, int_arg, float_arg):
      str_arg = av.get_validated_str("str_arg")
      int_arg = av.get_validated_int("int_arg")
      float_arg = av.get_validated_float("float_arg")
      ....
```
Note that the name of the argument is passed to the validation function and not the value.  
After successful validation (no exception raised), these variables can be safely used as str, int and float. For more complex validation with the use of strict mode, minumum or maximum values allowed or defaults, see the validation functions below.


</br>

### API

#### Methods
* [get_validated_int()](#get_validated_int-method)  
* [get_validated_float()](#get_validated_float-method)  
* [get_validated_str()](#get_validated_str-method)  
</br>
</br>


#### get_validated_int() Method
```py
  get_validated_int(var_name, min_value, max_value, strict, default=None, return_limits=False)
```
Arguments:
- var_name  
  The name of the argument being validated.
- min_value  
  Optional lower limit to validate var_name's value against.
- max_value  
  Optional upper limit to validate var_name's value against.
- strict  
  Optional setting to allow only integers as var_name's value, when set to True. The default is validation in non-strict mode, which allowes string representations of an integer (e.g. "220").
- default  
  Optional setting for an integer default value. This avoids an exception being raised in case var_name's value fails validation and this default value is returned instead. 
- return_limits  
  Optional setting to avoid an exception being raised for values outside the limits. 
  When set to True and with either min_value or max_value being exceeded, this limit value is returned as validated value.

Returns the validated integer value or with the default or return_limits option used, one of these values instead of an exception raised.

<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>

</br>

#### get_validated_float() Method
```py
  get_validated_float(var_name, min_value, max_value, strict, default=None, return_limits=False)
```
Arguments:
- var_name  
  The name of the argument being validated.
- min_value  
  Optional lower limit to validate var_name's value against.
- max_value  
  Optional upper limit to validate var_name's value against.
- strict  
  Optional setting to allow only a float as var_name's value, when set to True. The default is validation in non-strict mode, which allowes string representations of a float (e.g. "1.99").
- default  
  Optional setting for a float default value. This avoids an exception being raised in case var_name's value fails validation and this default value is returned instead. 
- return_limits  
  Optional setting to avoid an exception being raised for values outside the limits. 
  When set to True and with either min_value or max_value being exceeded, this limit value is returned as validated value.

Returns the validated float value or with the default or return_limits option used, one of these values instead of an exception raised.


<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>

</br>

#### get_validated_str() Method
```py
  get_validated_str(var_name, min_length, strict, default=None)
```
- var_name  
  The name of the argument being validated.
- min_length  
  The minimum length required for a valid string.
- strict  
  Optional setting to allow only a string as var_name's value, when set to True. The default is validation in non-strict mode, which allowes any value, which can be converted into a string.
- default  
  Optional setting for a string default value. This avoids an exception being raised in case var_name's value fails validation and this default value is returned instead. 

Returns the validated string value or with the default option used, this value instead of an exception raised.

<div style="text-align: right"><a href="#methods">&#8679; back up to list of methods</a></div>

</br>

## License
MIT license  
Copyright &copy; 2025 by krokoreit
