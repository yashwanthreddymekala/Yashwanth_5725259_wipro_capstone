Feature: BigBasket Negative Test Cases

  @critical
  Scenario: Invalid Mobile Number

    Given the user opens BigBasket website for negative testing
    When the user clicks login button
    And the user enters invalid mobile number
    Then the continue button should remain disabled


  @critical
  Scenario: Invalid OTP

    Given the user opens BigBasket website for OTP negative testing
    When the user clicks login button for OTP test
    And the user enters valid mobile number
    And the user clicks continue button
    And the user enters invalid OTP manually
    And the user clicks verify and continue button
    Then the login should fail for invalid OTP