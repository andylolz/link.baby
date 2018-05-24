Feature: Linkup creation

Scenario: Check linkup creation page works
    When a user visits '/create'
    Then they see a form with the following fields:
        | label            | type     |
        | Host name:       | Text     |
        | Email address:   | Text     |
        | Linkup name:     | Text     |
        | Welcome message: | Textarea |
        | Recipients:      | Textarea |

Scenario: Check linkup creation works
    When a user visits '/create'
    And the user submits the following data:
        | label            | value                                    |
        | Host name:       | Eve Evans                                |
        | Email address:   | eve@example.com                          |
        | Linkup name:     | Thanks for attending Eve’s event         |
        | Welcome message: | # Hi!\n\nWanted to put you all in touch. |
        | Recipients:      | Alice <alice@example.com>\nbob@bob.com   |
    Then the user should be redirected to '/'
    And welcome emails are sent to 2 recipients
