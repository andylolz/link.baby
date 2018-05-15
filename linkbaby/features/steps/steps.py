from behave import given, when, then

from linkbaby.factories import EventFactory, EventAttendeeFactory
from linkbaby.models import Event, EventAttendee, Introduction


@given('an event')
def step_an_event(context):
    EventFactory()


@given('the event has an attendee called {name}')
def step_the_event_has_an_attendee(context, name):
    event = Event.objects.first()
    EventAttendeeFactory(
        name=name,
        event=event
    )


@when('{name} subscribes to introductions')
def step_attendee_subscribes_to_introductions(context, name):
    attendee = EventAttendee.objects.get(name=name)
    attendee.subscribe_to_introductions()


@then('an introduction should be created between {name1} and {name2}')
def step_an_introduction_should_exist(context, name1, name2):
    intro = Introduction.objects.filter(
        recipients__name=name1).filter(
        recipients__name=name2)
    context.test.assertEqual(len(intro), 1)


@then('the total number of introductions should be {num:d}')
def step_the_total_number_of_introductions_should_be_num(context, num):
    context.test.assertEqual(Introduction.objects.count(), num)
