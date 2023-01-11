#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all the unique integers in a list
    (only once for each integer) with the prototype 
    def uniq_add(my_list=[]):
    """
    new_list = set(my_list)
    return sum(new_list)
