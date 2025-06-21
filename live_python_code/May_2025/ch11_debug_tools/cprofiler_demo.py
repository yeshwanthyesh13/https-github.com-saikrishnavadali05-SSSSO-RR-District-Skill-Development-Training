# Example 8: Profiling with cProfile
import cProfile
def test():
  total = 0
  for i in range(1000):
    total += i
  return total

cProfile.run('test()')
