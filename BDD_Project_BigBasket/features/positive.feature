Feature: BigBasket Fashion Module

  Scenario: Login And Checkout Positive Flow

    Given User opens BigBasket website
    When User clicks login button
    And User enters mobile number
    And User clicks continue button
    And User waits for OTP and clicks verify button
    Then User should login successfully

    When User opens footwear page
    Then Footwear page should open successfully

    When User opens brands filter
    And User selects Adidas Sports
    And User adds first product
    Then First product should be added successfully

    When User scrolls half page
    And User selects Action checkbox
    And User adds second product
    And User opens basket
    Then Basket should open successfully