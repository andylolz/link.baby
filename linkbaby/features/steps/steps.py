from django.test import Client
from behave import given, when, then

from linkbaby.factories import LinkupFactory, LinkeeFactory
from linkbaby.models import Linkup, Linkee, Introduction


@given('a linkup')
def step_a_linkup(context):
    LinkupFactory()


@given('the linkup has a linkee called {name}')
def step_the_linkup_has_a_linkee(context, name):
    linkup = Linkup.objects.first()
    LinkeeFactory(
        user__name=name,
        linkup=linkup
    )


@when('{name} subscribes to introductions')
def step_attendee_subscribes_to_introductions(context, name):
    attendee = Linkee.objects.get(user__name=name)
    attendee.subscribe()


@when('{name} unsubscribes')
def step_attendee_unsubscribes(context, name):
    attendee = Linkee.objects.get(user__name=name)
    attendee.unsubscribe()


@then('an unscheduled introduction should be created ' +
      'between {name1} and {name2}')
def step_an_introduction_should_exist(context, name1, name2):
    intro = Introduction.objects.filter(
        recipients__user__name=name1).filter(
        recipients__user__name=name2).filter(
        scheduled_at__isnull=True,
    )
    context.test.assertEqual(len(intro), 1)


@then('the total number of introductions should be {num:d}')
def step_the_total_number_of_introductions_should_be_num(context, num):
    context.test.assertEqual(Introduction.objects.count(), num)


@when('a user visits \'{url}\'')
def step_a_user_visit_url(context, url):
    client = Client()
    context.response = client.get(url)


@then('they see the text \'{text}\'')
def step_they_see_the_text_text(context, text):
    context.test.assertContains(context.response, text)


@then('they see a form with the following fields')
def step_they_see_a_form_with_fields(context):
    # TODO: field types are currently ignored
    for row in context.table:
        context.test.assertContains(context.response, row['label'])
