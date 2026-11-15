import pytest
 
from calculator import add, divide, subtract
 
 
def test_add() -> None:
    assert add(2, 3) == 5
 
 
def test_subtract() -> None:
    assert subtract(8, 3) == 5
 
 
def test_divide() -> None:
    assert divide(10, 2) == 5


 
def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
