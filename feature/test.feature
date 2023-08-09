Feature: Login feature

  Scenario: Successful login
    Given I open the login page
    When I enter username "demo"
    And I enter password "password"
    And I click login button
    Then I should see the home page