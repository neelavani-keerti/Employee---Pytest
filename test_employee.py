from employee import employee_details
def test_employee_details():
    expected output=(
        "Employee Name:Keerti\n"
        "Employee ID:E123\n"
        "Department=Tech\n"
        "Salary=98000\n"
    )
    assert employee_details("Keerti","E123","Tech",98000)== expected_output