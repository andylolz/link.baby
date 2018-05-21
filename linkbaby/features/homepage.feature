Feature: Homepage

Scenario: Test the homepage
    When a user visits '/'
    Then they see the text 'Hello, hello'
