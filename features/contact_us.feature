Feature: contact us functionality
  Scenario: test contact us functionality
    Given launch the contactus browser
    When open the php contactus homepage
    And click on the contact us button
    And enter all the mandatory fields
    And click on the submit
    Then submitted successfully
    And close the contactus browser