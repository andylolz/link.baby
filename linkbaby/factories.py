import factory
from linkbaby.models import Event, EventOrganiser, EventAttendee


class EventOrganiserFactory(factory.DjangoModelFactory):
    class Meta:
        model = EventOrganiser

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        x.name.lower().replace(' ', '.')))


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    organiser = factory.SubFactory(EventOrganiserFactory)
    name = factory.LazyAttribute(lambda x: '{}’s awesome event'.format(
        x.organiser.name.split()[0]))


class EventAttendeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = EventAttendee

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        x.name.lower().replace(' ', '.')))
    bio = factory.Faker('paragraph')
    event = factory.SubFactory(EventFactory)
