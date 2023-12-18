def factorial(n):
  """Computes the factorial of n.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
