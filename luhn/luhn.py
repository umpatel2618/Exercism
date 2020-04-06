class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ','')

    def valid(self):
        check = list(reversed(self.card_num))
        if not self.card_num.isdigit() or len(check) <= 1:
            return False
        for x, v in enumerate(check):
            if x % 2 != 0:
                checked = 2 * int(v)
            else:
                checked = int(v)
            check[x] = checked if checked <= 9 else checked - 9
        return sum(check) % 10 == 0