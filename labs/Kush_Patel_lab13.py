#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    trie = {}
    result = []

    for operation, value in queries:
        if operation == "add":
            node = trie
            for ch in value:
                if ch not in node:
                    node[ch] = {"_count": 0}
                node = node[ch]
                node["_count"] += 1

        elif operation == "find":
            node = trie
            found = True

            for ch in value:
                if ch not in node:
                    found = False
                    break
                node = node[ch]

            if found:
                result.append(node["_count"])
            else:
                result.append(0)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()