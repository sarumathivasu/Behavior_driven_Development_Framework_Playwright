Feature: Verify OrangeHRM login flow

Scenario Outline: Verify user login with different credentials

Given the user navigates to the login page
When the user enters "<username>" and "<password>"
Then the "<expected_result>" should be displayed

Examples:
| username  | password  | expected_result       |
| Admin     | admin123  | Dashboard             |
| Admin     | wrong123  | Invalid credentials   |
| WrongUser | admin123  | Invalid credentials   |