from Questions import *

l1 = [True, False, False, True]
l2 = [1, 2, 11, 22, 12, 21, 1 , 2, 11]
l3 = ["a", "aa", "aba", "aa", "a", "ba"]
s1 = "H,i? Th$ere. 'HOW .are YoU?"
s2 = ".?-"
s3 = "numbers12345"
def test_removeDuplicates1():
    removeDuplicates(l1)
    assert l1 == [True, False]

def test_removeDuplicates2():
    removeDuplicates(l2)
    assert l2 == [1, 2, 11, 22, 12, 21]


def test_removeDuplicates3():
    removeDuplicates(l3)
    assert l3 == ["a", "aa", "aba", "ba"]
def test_eecummings1():
    assert eecummings(s1) == "hi there how are you"

def test_eecummings2():
    assert eecummings(s2) == ""

def test_eecummings3():
    assert eecummings(s3) == "numbers"

def test_circularShift1():
    circularShift(1, l2)
    assert l2 == [21, 1, 2, 11, 22, 12]

def test_circularShift2():
    circularShift(-1, l2)
    assert l2 == [1, 2, 11, 22, 12, 21]

def test_circularShift3():
    circularShift(1000001, l1)
    assert l1 == [False, True]