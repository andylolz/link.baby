Feature: Linkup creation

Scenario: Check the form fields
    When a user visits '/create'
    Then they see a form with the following fields:
        | label           | type     |
        | Linkup name     | Text     |
        | Welcome message | Textarea |
