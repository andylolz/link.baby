Feature: Introductions

Background:
    Given an event
    And the event has an attendee called Alice
    And the event has an attendee called Bob
    And the event has an attendee called Charlie
    And the event has an attendee called Daisy

Scenario: Test a simple introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    Then an introduction should be created between Alice and Bob
    And the total number of introductions should be 1

Scenario: Test a more complicated introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    And Charlie subscribes to introductions
    Then an introduction should be created between Alice and Bob
    And an introduction should be created between Alice and Charlie
    And an introduction should be created between Bob and Charlie
    And the total number of introductions should be 3
