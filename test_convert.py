import pytest
from convert import celsius_to_farenheit
def test_celsius_to_farenheit():
        assert celsius_to_farenheit(20) == 68
        assert celsius_to_farenheit(30) == 86
        assert celsius_to_farenheit (0) == 32
        assert round (celsius_to_farenheit(9),0) == 48
        assert abs (celsius_to_farenheit(9)- 48) < 0.21

def test_celsius_to_farenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_farenheit("Invalid")