from blankquestions.Iteration_and_Conditionals import *
def test_getSumOfString1():
    assert getSumOfString("10 2 5 3") == 20

def test_getSumOfString2():
    assert getSumOfString("1") == 1

def test_getSumOfString3():
    assert getSumOfString("10 -12 03") == 1

def test_reorder1():
    assert reorder("ZzAa") == "AaZz"

def test_reorder2():
    assert reorder("Z") == "Z"

def test_reorder3():
    assert reorder("ZzyYXxwWzZabc") == "abcwWXxyYZzzZ"

def test_reorder3():
    assert reorder("ZzyYXxwWzZabc") == "abcwWXxyYZzzZ"

def test_orderAndDeleteDuplicates1():
    assert orderAndDeleteDuplicates("ZzaA") == "aZ"

def test_orderAndDeleteDuplicates2():
    assert orderAndDeleteDuplicates("ZzyYXxwWzZabc") == "abcwXyZ"


def test_orderAndDeleteDuplicates3():
    assert orderAndDeleteDuplicates("BAaaaaaaaaaaaaaaab") == "AB"



