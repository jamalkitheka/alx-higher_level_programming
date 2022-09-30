#!/usr/bin/python3
def best_score(a_dictionary):
    init = 0
    key = ''
    if a_dictionary is None:
        return(None)
    else:
        for k, v in a_dictionary.items():
            if v > init:
                init = v
                key = k
    if init == 0:
        return(None)
    return(key)
