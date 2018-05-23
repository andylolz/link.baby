Feature: Event creation

Scenario: Test the homepage
    When a user visits '/create'
    Then they see a form with the following fields:
        | label           | type     |
        | Event name      | Text     |
        | Took place at   | Date     |
        | Welcome message | Textarea |
