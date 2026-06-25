import pytest
from app.validation import validate_overtime

def test_valid_overtime():
    assert validate_overtime(10) == True

def test_negative_overtime():
    with pytest.raises(ValueError):
        validate_overtime(-5)

def test_excess_overtime():
    with pytest.raises(ValueError):
        validate_overtime(150)
