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
def step_an_introduction_should_be_created(context, name1, name2):
    attendee1 = EventAttendee.objects.get(name=name1)
    attendee2 = EventAttendee.objects.get(name=name2)
    intro = Introduction.objects.get()
    recipients = intro.recipients.all()
    context.test.assertIn(attendee1, recipients)
    context.test.assertIn(attendee2, recipients)
