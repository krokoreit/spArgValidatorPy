from spArgValidatorPy import ArgValidator


def test_1():
    obj = ArgValidator()

    arg1 = "blabla"
    assert obj.for_test_only(arg1) == arg1

