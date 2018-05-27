Feature: Linkup creation

Background:
    Given a user visits '/create'
    And in the "Host name:" field, the user enters "Eve Evans"
    And in the "Email address:" field, the user enters "eve@example.com"
    And in the "Linkup name:" field, the user enters "Great to meet you"
    And in the "Welcome message:" field, the user enters:
        """
        # Hi!

        Wanted to put you all in touch.
        """

Scenario: Check linkup creation works
    Given in the "Recipients:" field, the user enters:
        """
        Alice <alice@example.com>
        bob@bob.com
        """
    When the user submits the form
    Then they are redirected to '/'
    And an email is sent to "Alice <alice@example.com>"
    And an email is sent to "bob@bob.com"

Scenario: Check linkup creation works
    Given in the "Recipients:" field, the user enters:
        """
        Alice <alice@example.com>
        """
    When the user submits the form
    Then they are redirected to '/'
    And an email is sent to "Alice <alice@example.com>"
    And the email subject line is "Great to meet you - Linkup"
