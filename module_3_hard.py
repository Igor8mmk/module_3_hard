data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
  ]

def All_calculate(*args):
  total_sum = 0
  for i in args:
    if isinstance(i, list):
      total_sum += All_calculate(*i)
    if isinstance(i, tuple):
      total_sum += All_calculate(*i)
    if isinstance(i, set):
      total_sum += All_calculate(*i)
    if isinstance(i, dict):
      total_sum += All_calculate(*i.items())
    if isinstance(i, str):
      total_sum += int(len(i))
    if isinstance(i, int or float):
      total_sum += i
  return total_sum


print(All_calculate(data_structure))

