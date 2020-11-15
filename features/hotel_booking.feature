Feature: to book the hotel
  Scenario: to search the hotel
    Given Browser is launch
    And open the Php hotel homepage
    When enter the destination
    And select the check in date and check out date
    And enter the adult number
    And enter the children number
    And click on the search button
    Then hotel should get search


  Scenario: Get the hotel details
    Given Hotel should get searched
    When click on the first searched hotel details button
    Then Details should get displayed