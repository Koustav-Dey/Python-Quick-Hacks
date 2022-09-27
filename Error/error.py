import re

for i in dir(__builtins__):
    # print(i)
    if re.match(r'^[A-Z]',i):
        print(i)