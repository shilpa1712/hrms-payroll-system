from app.models import Employee
from app.payroll import calculate_salary

def test_salary_calculation():
    emp = Employee("Shilpa", 20000, 200)
    result = calculate_salary(emp, 10)

    assert result["total_salary"] == 22000

def test_zero_overtime():
    emp = Employee("Test", 15000, 100)
    result = calculate_salary(emp, 0)

    assert result["total_salary"] == 15000
