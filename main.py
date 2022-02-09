def to_roman_numerals(num_to_convert):
    accu = ''

    num_to_convert, accu = check_for_partial(num_to_convert, accu, 1000, 'M')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 900, 'CM')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 500, 'D')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 400, 'CD')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 100, 'C')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 90, 'XC')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 50, 'L')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 40, 'XL')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 10, 'X')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 9, 'IX')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 5, 'V')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 4, 'IV')
    num_to_convert, accu = check_for_partial(num_to_convert, accu, 1, 'I')

    return accu

def check_for_partial(num_to_convert, accu, partial, representation):
    partial_occurences = int(num_to_convert / partial)
    accu += representation * partial_occurences
    num_to_convert = num_to_convert - partial_occurences * partial
    return num_to_convert, accu
