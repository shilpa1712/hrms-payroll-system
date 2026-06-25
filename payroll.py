from app.validation import validate_overtime

def calculate_salary(employee, overtime_hours):
    validate_overtime(overtime_hours)

    overtime_pay = overtime_hours * employee.overtime_rate
    total_salary = employee.base_salary + overtime_pay

    return {
        "employee": employee.name,
        "base_salary": employee.base_salary,
        "overtime": overtime_hours,
        "total_salary": total_salary
    }
