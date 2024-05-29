Feature: Say hello!

    Scenario: Run the cli command
        Given I have the cli installed
        When I run the 'hello' command with 'Ivan Pina' as argument
        Then I should see 'Hello Ivan Pina!'
