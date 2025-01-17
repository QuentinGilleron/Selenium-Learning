Feature: Verify that the button Start finishes at 100%

  Scenario: Verify that the button Start finishes at 100%
    Given I am on the progress barre page
    When I click on Start button
    Then I verify that the button Start finishes at 100%

  Scenario: click on the sub sub item 2
    Given I am on the widget menu page
    When I click on Main Item 2
    And I click on Sub Sub List
    Then I can click the Sub Sub Item 2