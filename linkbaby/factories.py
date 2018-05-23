import factory

from .models import Linkup, Host, Linkee, LinkbabyUser


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = LinkbabyUser

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: '{}@example.com'.format(
        '.'.join(x.name.lower().split(' '))))


class HostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Host

    user = factory.SubFactory(UserFactory)


class LinkupFactory(factory.DjangoModelFactory):
    class Meta:
        model = Linkup

    host = factory.SubFactory(HostFactory)
    name = factory.LazyAttribute(lambda x: '{}’s awesome linkup'.format(
        x.host.user.first_name))


class LinkeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Linkee

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('paragraph')
    linkup = factory.SubFactory(LinkupFactory)
