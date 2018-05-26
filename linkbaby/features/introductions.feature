Feature: Introductions

Background:
    Given a linkup
    And the linkup has a linkee called Alice
    And the linkup has a linkee called Bob
    And the linkup has a linkee called Charlie
    And the linkup has a linkee called Daisy

Scenario: Test a simple introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    Then an unscheduled introduction is created between Alice and Bob
    And the total number of introductions is 1

Scenario: Test a more complicated introduction
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    And Charlie subscribes to introductions
    Then an unscheduled introduction is created between Alice and Bob
    And an unscheduled introduction is created between Alice and Charlie
    And an unscheduled introduction is created between Bob and Charlie
    And the total number of introductions is 3

Scenario: Test event unsubscribe
    When Alice subscribes to introductions
    And Bob subscribes to introductions
    And Charlie subscribes to introductions
    And Alice unsubscribes
    Then an unscheduled introduction is created between Bob and Charlie
    And the total number of introductions is 1
