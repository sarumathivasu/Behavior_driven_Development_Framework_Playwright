from pytest_bdd import given, when, then


@given(
    "the user creates an employee",
    target_fixture="employee_id"
)
def create_employee():

    employee_id = "EMP12345"

    print(f"Created employee: {employee_id}")

    return employee_id


@when("the user searches for the employee")
def search_employee(employee_id):

    print(f"Searching for employee: {employee_id}")


@then("the employee should be displayed")
def verify_employee(employee_id):

    print(f"Verifying employee: {employee_id}")

    assert employee_id == "EMP12345"