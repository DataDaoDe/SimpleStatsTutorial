

def arithmetic_mean(x: list[float]) -> float:
  """
  The sum of all measurements in `x` divided
  by the number of observations in the vector `x`

  .. math::
    \\sum_{i=1}^{n} x_i
  where :math:`n` is the length of the vector :math:`x`
  >>> 
  """
  sum_total = 0
  for i in range(len(x)):
    sum_total += x[i]
  return sum_total
