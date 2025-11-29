def flatten(lst):
   result = []
   stack = lst.copy()
   while stack:
       item = stack.pop(0)
       if isinstance(item, list):
           stack = item + stack
       else:
           result.append(item)
   return result
print(flatten([1, [2, [3, 4], 5]]))
print(flatten([1, [2, [3, 4], 5,[6,7,[8,9]]]]))