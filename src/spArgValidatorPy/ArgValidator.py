# ================================================================================
#
#   ArgValidator class
#
#   object for validating function arguments and either raising an exception 
#   or returning the validated value
#
#   MIT License
#
#   Copyright (c) 2025 krokoreit (krokoreit@gmail.com)
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#
# ================================================================================

import sys
import inspect


original_excepthook = sys.excepthook
stop_TB_at_function_name = None
def my_excepthook(type, value, traceback):
    print("my_excepthook")
    iter_tb = traceback
    while iter_tb.tb_next is not None:
        if iter_tb.tb_next.tb_frame.f_code.co_name is stop_TB_at_function_name:
            iter_tb.tb_next = None
            break
        iter_tb = iter_tb.tb_next
    original_excepthook(type, value, traceback)

# shift to my handler
sys.excepthook = my_excepthook

def raise_with_stopped_traceback(exception_type, exception_text):
    global stop_TB_at_function_name

    frame = inspect.currentframe().f_back.f_back
    function_name = frame.f_code.co_name
    stop_TB_at_function_name = function_name
    function = None
    if "self" in frame.f_locals:
        function = getattr(frame.f_locals["self"].__class__, function_name)
    else:
        function = getattr(inspect.getmodule(frame), function_name)
    if function is None:
        sig = "()"
    else:    
        sig = inspect.signature(function)
    raise exception_type(function_name + str(sig) + " " + exception_text)


def get_value_for_var_name(var_name):
    frame = inspect.currentframe().f_back
    local_vars = frame.f_back.f_locals
    if len(var_name) == 0:
        raise_with_stopped_traceback(ValueError, "called without var_name, must be one of " + str(local_vars.keys()))
    if var_name not in local_vars:
        raise_with_stopped_traceback(ValueError, "called with unknown var_name '" + var_name + "', must be one of " + str(local_vars.keys()))
    return local_vars[var_name]


class ArgValidator:

    def get_validated_int(self, var_name, min_value=None, max_value=None):
        value = get_value_for_var_name(var_name)
        # might be string representation
        if isinstance(value, str):
            sValue = value.strip()
            try:
                value = int(sValue)
                if str(value) != sValue:
                    value = None
            except Exception as e:
                value = None
        if not isinstance(value, int):
            raise_with_stopped_traceback(TypeError, "called with '" + var_name + "' not being an integer or a string representation of an integer.")
        if min_value is not None and value < min_value:
            raise_with_stopped_traceback(ValueError, "called with '" + var_name + "' being less than minimum value of " + str(min_value) + ".")
        if max_value is not None and value > max_value:
            raise_with_stopped_traceback(ValueError, "called with '" + var_name + "' being more than maximum value of " + str(max_value) + ".")
        return value


    def get_validated_float(self, var_name, min_value=None, max_value=None):
        value = get_value_for_var_name(var_name)
        # might be string representation or int
        if isinstance(value, str):
            sValue = value.strip()
            period_pos = sValue.find(".")
            if period_pos > -1:
                # trim trailing zeros
                sPos = len(sValue) - 1
                while sPos > period_pos + 2:
                    if sValue[sPos] == "0":
                        sPos -= 1
                    else:
                        period_pos = len(sValue)
                sValue = sValue[:sPos+1]
            else:
                # add some
                sValue += ".0"
            try:
                value = float(sValue)
                if str(value) != sValue:
                    value = None
            except Exception as e:
                value = None
        elif isinstance(value, int):
            value = float(value)
        # check for float
        if not isinstance(value, float):
            raise_with_stopped_traceback(TypeError, "called with '" + var_name + "' not being a float, an integer or a string representation of a float.")
        if min_value is not None and value < min_value:
            raise_with_stopped_traceback(ValueError, "called with '" + var_name + "' being less than minimum value of " + str(min_value) + ".")
        if max_value is not None and value > max_value:
            raise_with_stopped_traceback(ValueError, "called with '" + var_name + "' being more than maximum value of " + str(max_value) + ".")
        return value



    def get_validated_str(self, var_name, min_length=1):
        value = get_value_for_var_name(var_name)
        if not isinstance(value, str):
            raise_with_stopped_traceback(TypeError, "called with '" + var_name + "' not being a string.")
        if len(value) < min_length:
            raise_with_stopped_traceback(ValueError, "called with length of '" + var_name + "' being less than " + str(min_length) + ".")
        return value

