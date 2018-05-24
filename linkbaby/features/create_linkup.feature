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
    Given the following stored as [welcome message]:
        """
        # Hi!

        Wanted to put you all in touch.
        """
    And the following stored as [recipients]:
        """
        Alice <alice@example.com>
        bob@bob.com
        """
    When a user visits '/create'
    And the user submits the following data:
        | label            | value                         |
        | Host name:       | Eve Evans                     |
        | Email address:   | eve@example.com               |
        | Linkup name:     | Thanks for attending my event |
        | Welcome message: | [welcome message]             |
        | Recipients:      | [recipients]                  |
    Then the user should be redirected to '/'
    And welcome emails are sent to 2 recipients
