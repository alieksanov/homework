#!/usr/bin/env python3

## https://github.com/alieksanov/homework/blob/master/xoriant_072018.py

# Task 1
print("Task 1\n")
import sys
try:
  line = sys.argv[1]
except:
  line = "Mississippi borders Tennessee."

out = {}
for l in set(line):
  out[l] = line.count(l)
for t in sorted(out.items(), key=lambda i: i[1], reverse=True):
  print("{0}: {1}".format(t[0], t[1]*"#"))

# Task 2
print("\n", "="*20)
print("Task 2\n")
fnames = ["Mary", "James", "Thomas", "William", "Elizabeth"]
lnames = ["Li", "O'Day", "Miller", "Garcia", "Davis"]
last_name = dict(zip(fnames, lnames))
for t in sorted(last_name.items(), key=lambda x: (len(x[1]), x[0])):
  print("{0} {1}".format(t[0], t[1]))

# Task 3
print("\n", "="*20)
print("Task 3\n")
def is_balanced(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    open_br = set("([{")
    pair_br = set([ ("(",")"), ("[","]"), ("{","}") ])
    for i in s:
        if i in open_br:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if (last, i) not in pair_br:
                return False
    return len(stack) == 0

print("Test passed: {0}".format(list(map(is_balanced, ["([)]{}", "](){", "{}([])", "{{{"])) == [False, False, True, False]))

# Task 4
print("\n", "="*20)
print("Task 4\n")
print("Test passed: {0}".format(list(map(is_balanced, [")()(", "()(())", "((("])) == [False, True, False]))

# Task 5
print("\n", "="*20)
print("Task 5\n")
def strip_comments(s):
  import re
  return re.sub(r'(\s|^)//.*\n', '', s)

d = """// this is a comment
{ // another comment
true, "foo", // 3rd comment

"http://www.ariba.com" // comment after URL
}"""

print(strip_comments(d))





