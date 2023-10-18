"""
In this task you will need to use lists and list functionality. To see the range of
functionality a list datastructure has, have a look at the W3 schools website python lists which gives
some useful demos of list methods.
"""
from typing import Any

"""
Q1 Removing Duplicates

Write a function (removeDuplicates(l: list[Any]) -> None) which takes a single list argument and 
removes any duplicates from the list.

e.g.
l1 = [1, 2, 2, 3, 1, 2, 3, 4]
removeDuplicates(l1)
print(l1) -> [1, 2, 3, 4]

l2 = ["a", "b", "ba", "a", "ba", "ab", "ab"]
removeDuplicates(l2)
print(l2) -> ["a", "b", "ba", "ab"]

"""


def removeDuplicates(l: list[Any]) -> None:
    # write your code here

    return


"""
Q2 Punctuation and Caps Disposal

The poet ee cummings had a famous aversion to punctuation. Write a function 
(eecummings(s: str) -> str) which removes all of the punctuation from a given string
and converts all capitals to lower case.

e.g 
marvell = "Had we but world enough and time, This coyness, lady, were no crime."
newStr = eecummings(marvell)
print(newStr) -> "had we but world enough and time this coyness lady were no crime"

"""


def eecummings(s: str) -> str:
    # write your code here

    return ""


"""
Q3 Circular shift

Complete this function (circularShift(num: int, l: list[Any])-> None) which takes an positive or negative 
integer argument and a list argument. The function then performs a circular shift on the list 
which is determined by the integer argument.

e.g.
l1 = ["a", "b", "c", "x", "y", "z"]
circularShift(2, l1)
print(l1) -> ["y", "z", "a", "b", "c", "x"]

l2 = [1, 2, 3, 7, 8, 9]
circularShift(-2, l2)
print(l2) -> [3, 7, 8, 9, 1, 2]

"""


def circularShift(num: int, l: list[Any]) -> None:
    # write your code here

    return
