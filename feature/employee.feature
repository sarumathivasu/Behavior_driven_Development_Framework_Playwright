Feature: Employee Management

  Scenario: Search for a newly created employee

    Given the user creates an employee
    When the user searches for the employee
    Then the employee should be displayed