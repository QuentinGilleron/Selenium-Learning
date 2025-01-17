Feature: Search book
  As a visitor
  I want to search for a book

  Scenario: Search for a book
    Given I am on the book page
    When I search for Marijn Haverbeke
    Then I verify that the search result is correct