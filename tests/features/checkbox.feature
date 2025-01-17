Feature: Use check box
    As a visitor
    I want to use check box

    Scenario: Select all the element except Office and Excel file.doc
        Given I go to the check box page
        When I select all the element except Office and Excel file.doc
        Then I should see the element selected