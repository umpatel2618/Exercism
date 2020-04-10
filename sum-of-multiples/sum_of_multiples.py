def sum_of_multiples(limit, multiples):
    return sum(set([h for k in multiples if k != 0 for h in range(0, limit) if h % k == 0]))
