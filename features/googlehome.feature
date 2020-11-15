Feature: Test functionality on Google home page
  Scenario: Search the keyword on Google home
    Given Open the browser
    When Open the google homepage which has search box
    Then Search for keyword 'Sample' and verify the title of the browser.
    And close the browser
