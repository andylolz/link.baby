Feature: Introductions

Scenario: Test a simple introduction
    Given an event
    And the event has an attendee called Alice
    And the event has an attendee called Bob
    And the event has an attendee called Jane
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    Then an introduction should be created between Alice and Bob
