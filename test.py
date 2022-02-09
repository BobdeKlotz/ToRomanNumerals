from main import to_roman_numerals

class TestClass:
    def test_to_roman_numerals(self):
        assert to_roman_numerals(1) == 'I'
        assert to_roman_numerals(2) == 'II'
        assert to_roman_numerals(4) == 'IV'
        assert to_roman_numerals(5) == 'V'
        assert to_roman_numerals(9) == 'IX'
        assert to_roman_numerals(10) == 'X'
        assert to_roman_numerals(42) == 'XLII'
        assert to_roman_numerals(99) == 'XCIX'
        assert to_roman_numerals(2013) == 'MMXIII'        
        assert to_roman_numerals(3000) == 'MMM'
