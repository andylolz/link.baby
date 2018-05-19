from django.contrib.auth.models import User
import factory

from linkbaby.models import Event, EventOrganiser, EventAttendee


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: x.first_name)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda x: '{}.{}@example.com'.format(
        x.first_name.lower(), x.last_name.lower()))


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
