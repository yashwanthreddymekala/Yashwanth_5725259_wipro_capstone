Feature: BigBasket Fashion Module

  @critical
  Scenario: Login and checkout
    Given the user opens BigBasket website
    When the user logs in with valid mobile number
    And the user waits for OTP and verifies login
    And the user opens Shop By Category
    And the user navigates to Fashion
    And the user navigates to Footwear
    And the user opens Brands filter
    And the user selects Adidas Sports
    And the user adds the first product to cart
    And the user scrolls half page
    And the user selects Action checkbox
    And the user adds the second product to cart
    And the user opens basket with two items
    And the user increments product quantity
    And the user proceeds to checkout
    Then the products should be added and checkout should be opened