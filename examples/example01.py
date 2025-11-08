#   example01.py
#
#   file to demonstrate the use of spArgValidatorPy
#
#
import sys

from spArgValidatorPy import ArgValidator

print("running Python executable from path", sys.executable)

av = ArgValidator()


class ExampleObj():

    def fail(self, a):
        a = av.get_validated_int("a")



def regular_fail_func():
    # cause exception
    print(1/0)


def func01(a, b):
    av.get_validated_str("a")
    av.get_validated_str("b")
    #av.get_validated_str("c")
    if a is None:
        print("a is None")

def func02(a, b=None):
    a = av.get_validated_int("a", 6, 10)
    print("a", type(a), a)

def func03(a):
    a = av.get_validated_float("a")
    print("a", type(a), a)


# ++++++++++++++++++++++++++++++++++++++++++


#func01("None", "33")
try:
    func02("15")
except Exception as e:
    print("Error:", str(e))

func03("15")

dum = ExampleObj()
dum.fail("ww")

#func01(None, b=33)
#regular_fail_func()

#func03("s")

exit()


try:
    func01(None, b=33)
    #func01("None", b=33)
    func01("None", b="33")
except Exception as e:
    print("we has an issue: " + str(e))

regular_fail_func()

