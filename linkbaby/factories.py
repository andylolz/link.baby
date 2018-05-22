import factory

from .models import Event, EventOrganiser, EventAttendee, LinkbabyUser


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = LinkbabyUser

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        '.'.join(x.name.lower().split(' '))))


class EventOrganiserFactory(factory.DjangoModelFactory):
    class Meta:
        model = EventOrganiser

    user = factory.SubFactory(UserFactory)


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    organiser = factory.SubFactory(EventOrganiserFactory)
    name = factory.LazyAttribute(lambda x: '{}’s awesome event'.format(
        x.organiser.user.first_name))


class EventAttendeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = EventAttendee

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('paragraph')
    event = factory.SubFactory(EventFactory)
