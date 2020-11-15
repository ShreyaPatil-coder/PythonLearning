Feature:  Sign_in functionality
  Scenario:Test sign_in functionality
    Given launch the browser
    When open the php homepage
    And click on the sign_in button
    And enter email id and password and login
    Then verify the user is able to sign_in
    And close the sign_in page