Feature: Use the web table
    As a visitor
    I want to use the web table

    Scenario: delete the first two lines and modify the salary of the remaining one
        Given I go to the web table page
        And I delete the first two lines
        And I modify the salary of the remaining one
        Then I should see the salary modified