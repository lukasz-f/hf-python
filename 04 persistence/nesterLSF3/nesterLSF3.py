"""This is the "nester.py" module and it provides one function called
   print_lol() which prints lists that may or may not include nested lists"""
import sys


def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    """This function takes a positional argument called "the_list", which is
       any Python list (of, possibly, nested lists). Each data item is the
       provided list is (recursively) printed to the screen on its own line.
       A second argument called "indent" it's possible to switch on indented
       output.
       A third argument called "level" is used to insert tab-stops when
       a nested list is encountered.
       A fourth argument called "file" identify a place to write data to."""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, file)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='', file=file)
            print(each_item, file=file)
