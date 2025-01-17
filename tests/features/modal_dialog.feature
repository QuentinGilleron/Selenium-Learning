Feature: Verify text in large dialogue
    As a visitor
    I want to verify text in large dialogue

    Scenario: Verify text in large dialogue
        Given I go to the modal dialogs page
        When I click on the large dialogue button
        Then I should see the text lorem ipsum 4 times