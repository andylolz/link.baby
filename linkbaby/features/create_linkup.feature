Feature: Linkup creation

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

Scenario: Check linkup creation works
    Given a user visits '/create'
    And in the "Host name:" field, enters "Eve Evans"
    And in the "Email address:" field, enters "eve@example.com"
    And in the "Linkup name:" field, enters "Great to meet you"
    And in the "Welcome message:" field, enters:
        """
        # Hi!

        Wanted to put you all in touch.
        """
    And in the "Recipients:" field, enters:
        """
        Alice <alice@example.com>
        bob@bob.com
        """
    When they submit the form
    Then they should be redirected to '/'
    And welcome emails are sent to 2 recipients
