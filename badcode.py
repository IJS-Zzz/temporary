# -*- coding: utf-8 -*-

def isFunnyFunction(data):
    if data != None:
        i = data[0]
        for j in range(1, len(data)):
            if data[j] != i:
                i = 0
                break
        if i == 0:
            i = int(data[0])
            for j in range(1, len(data)):
                if int(data[j]) == i + 1:
                    i += 1
                else:
                    i = 0
                    break
            if i != 0:
                return 1
        else:
            return 1
        i = int(data[len(data) - 1])
        for j in range(len(data) - 2, -1, -1):
            if int(data[j]) != i + 1:
                i = 0
                break
            else:
                i += 1
        if i != 0:
            return 1
    else:
        raise ValueError("data is None")

