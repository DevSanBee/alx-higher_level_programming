#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    for element in my_list:
        if element == search:
            my_list[element] = replace
    return my_list
