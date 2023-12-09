Feature: OrangeHRM Login
  Scenario: Verify that user can login with valid credentials
    Given : User can load the demo website
    When  : Enter Username
    When  : Enter Password
    When  : Click Login Button
    Then  : User should be logged in successfully

