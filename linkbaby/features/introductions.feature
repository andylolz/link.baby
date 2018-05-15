Feature: Introductions

Background:
    Given an event
    And the event has an attendee called Alice
    And the event has an attendee called Bob
    And the event has an attendee called Charlie
    And the event has an attendee called Dean

Scenario: Test a simple introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    Then an introduction should exist between Alice and Bob

Scenario: Test a more complicated introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    And Charlie subscribes to introductions
    Then an introduction should exist between Alice and Bob
    And an introduction should exist between Alice and Charlie
    And an introduction should exist between Bob and Charlie
