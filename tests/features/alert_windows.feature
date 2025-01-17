Feature: open and close new tab
    As a visitor
    I want to open and close new tab

    Scenario: open and close new tab
        Given I go to the alert windows page
        When I click on the button new tab
        And I see a new tab
        Then I close the new tab