import factory

from .models import Linkup, Host, Linkee


class HostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Host

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        '.'.join(x.name.lower().split(' '))))


class LinkupFactory(factory.DjangoModelFactory):
    class Meta:
        model = Linkup

    host = factory.SubFactory(HostFactory)
    name = factory.LazyAttribute(lambda x: '{}’s awesome linkup'.format(
        x.host.name.split(' ')[0]))


class LinkeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Linkee

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        '.'.join(x.name.lower().split(' '))))
    bio = factory.Faker('paragraph')
    linkup = factory.SubFactory(LinkupFactory)
