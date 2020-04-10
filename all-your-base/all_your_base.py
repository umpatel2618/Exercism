def rebase(input_base, digits, output_base):

    if input_base < 2 or output_base < 2 :
        raise ValueError("Invalid Input")

    number = 0
    for i in range(len(digits)) :

        v = digits[::-1][i]

        if v < 0 or v >= input_base :
            raise ValueError("Invalid Input")

        number += v * input_base**i
    res = []
    while number != 0 :
        res.insert(0,number%output_base)
        number //= output_base
    
    return res if res != [] else [0]