import random

# 重複ありうる
def rand_ints_dup(a, b, k):
  return [random.randint(a, b) for i in range(k)]

# 重複なし
def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

print(rand_ints_dup(0, 10, 7))

print(rand_ints_nodup(0, 10, 7))

