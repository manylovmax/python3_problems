
def flatten(data):
  output = []
  stack = []

  stack.append(data)
  while len(stack):
    x = stack.pop()
    if isinstance(x, list):
      stack.extend(x)
    else:
      output.insert(0, x)

  return output


def test_flatten():
  assert flatten([[1, 2, [3]], 4, [[5]]]) == [1, 2, 3, 4, 5]
  assert flatten([]) == []
  data = [0]
  for i in range(1000):
    data = [data]
  assert flatten(data) == [0]

try:
  print('running list_flattening.py')
  test_flatten()
except Exception as e:
  raise e
else:
  print('all tests passed!')
