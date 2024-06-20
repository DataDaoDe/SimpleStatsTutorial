import simple_stats.central_tendency as ct


def test_arithmetic_mean():
  specs = [
    [[1,2,3], 6],
    [[100], 100],
    [[100, -100], 0],
  ]
  for t in specs:
    result = ct.arithmetic_mean(t[0])
    assert result == t[1]