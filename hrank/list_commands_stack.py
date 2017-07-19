# stack is a list of commands for a list, e.g.
# insert i e - insert at position i element 3,
# pop - pop the list
# append e - append e to list
# print - print the list

mylist, cs = list(), [input().split(" ") for _ in range(int(input()))]
[getattr(mylist, c)(*map(int, args)) if hasattr(mylist, c) else print(mylist) for c, *args in cs]
