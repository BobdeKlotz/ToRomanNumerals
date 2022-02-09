def to_roman_numerals(num_to_convert):
    accu = ''
    partials = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    representations = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    for i in range(len(partials)):
        num_to_convert, accu = check_for_partial(num_to_convert, accu, partials[i], representations[i])

    return accu

def check_for_partial(num_to_convert, accu, partial, representation):
    partial_occurences = int(num_to_convert / partial)
    accu += representation * partial_occurences
    num_to_convert = num_to_convert - partial_occurences * partial
    return num_to_convert, accu
