import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        
    def test_multiplication(self):
        assert 10 == calculator.multiply(10, 10)
    
    def test_divide(self):
        assert 1 == calculator.divide(10, 10)