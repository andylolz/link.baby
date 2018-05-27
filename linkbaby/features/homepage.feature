Feature: Homepage

Scenario: Test the homepage
    When a user visits '/'
    Then they see the text 'Hello, hello'

Scenario: Check linkup creation page works
    When a user visits '/create'
    Then they see a form with the following fields:
        | label            |
        |------------------|
        | Host name:       |
        | Email address:   |
        | Linkup name:     |
        | Welcome message: |
        | Recipients:      |
