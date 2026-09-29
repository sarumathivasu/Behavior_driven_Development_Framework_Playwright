Feature: OrangeHRM Login

  # Background contains common steps that run before every scenario
  # in this feature.

  Background:
    Given the user is on the OrangeHRM login page

  Scenario: Successful login
    When the user enters valid username and password
    Then the Dashboard should be displayed

  Scenario: Login with invalid password
    When the user enters a valid username and invalid password
    Then the Invalid credentials message should be displayed

  Scenario: Login with invalid username
    When the user enters an invalid username and valid password
    Then the Invalid credentials message should be displayed