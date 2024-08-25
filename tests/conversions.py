from typing import List
from data_structures.array_sorted_list import ArraySortedList

def SLtoList(sl: ArraySortedList):
    out = []
    for i in range(len(sl)):
        out.append(sl[i].value)
    return out

def ListtoSL(lst: List):
    sl = ArraySortedList(len(lst))
    for item in lst:
        sl.add(item)
    return sl