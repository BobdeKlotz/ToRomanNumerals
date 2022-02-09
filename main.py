def to_roman_numerals(num_to_convert):
    accu = ''

    thousands = int(num_to_convert / 1000)
    accu += 'M' * thousands
    num_to_convert = num_to_convert - thousands * 1000

    ninehundreds = int(num_to_convert / 900)
    accu += 'CM' * ninehundreds
    num_to_convert = num_to_convert - ninehundreds * 900

    fivehundreds = int(num_to_convert / 500)
    accu += 'D' * fivehundreds
    num_to_convert = num_to_convert - fivehundreds * 500

    fourhundreds = int(num_to_convert / 400)
    accu += 'CD' * fourhundreds
    num_to_convert = num_to_convert - fourhundreds * 400

    hundreds = int(num_to_convert / 100)
    accu += 'C' * hundreds
    num_to_convert = num_to_convert - hundreds * 100

    nineties = int(num_to_convert / 90)
    accu += 'XC' * nineties
    num_to_convert = num_to_convert - nineties * 90

    fifties = int(num_to_convert / 50)
    accu += 'L' * fifties
    num_to_convert = num_to_convert - fifties * 50

    fourties = int(num_to_convert / 40)
    accu += 'XL' * fourties
    num_to_convert = num_to_convert - fourties * 40

    tens = int(num_to_convert / 10)
    accu += 'X' * tens
    num_to_convert = num_to_convert - tens * 10

    nines = int(num_to_convert / 9)
    accu += 'IX' * nines
    num_to_convert = num_to_convert - nines * 9

    fives = int(num_to_convert / 5)
    accu += 'V' * fives
    num_to_convert = num_to_convert - fives * 5

    fours = int(num_to_convert / 4)
    accu += 'IV' * fours
    num_to_convert = num_to_convert - fours * 5

    ones = int(num_to_convert / 1)
    accu += 'I' * ones
    num_to_convert = num_to_convert - ones * 1

    return accu
