from django.test import Client
from django.core import mail
from behave import given, when, then
from bs4 import BeautifulSoup as bs

from linkbaby.factories import LinkupFactory, LinkeeFactory
from linkbaby.models import Linkup, Linkee, Introduction


@given('a linkup')
def step_a_linkup(context):
    LinkupFactory()


@given('the linkup has a linkee called {name}')
def step_the_linkup_has_a_linkee(context, name):
    linkup = Linkup.objects.first()
    LinkeeFactory(
        name=name,
        linkup=linkup
    )


@when('{name} subscribes to introductions')
def step_attendee_subscribes_to_introductions(context, name):
    attendee = Linkee.objects.get(name=name)
    attendee.subscribe()


@when('{name} unsubscribes')
def step_attendee_unsubscribes(context, name):
    attendee = Linkee.objects.get(name=name)
    attendee.unsubscribe()


@then('an unscheduled introduction is created ' +
      'between {name1} and {name2}')
def step_an_introduction_is_created(context, name1, name2):
    intro = Introduction.objects.filter(
        recipients__name=name1).filter(
        recipients__name=name2).filter(
        scheduled_at__isnull=True,
    )
    context.test.assertEqual(len(intro), 1)


@then('the total number of introductions is {num:d}')
def step_the_total_number_of_introductions_is_num(context, num):
    context.test.assertEqual(Introduction.objects.count(), num)


@given('a user visits \'{url}\'')
@when('a user visits \'{url}\'')
def step_a_user_visit_url(context, url):
    context.url = url
    context.client = Client()
    context.response = context.client.get(url)


@then('they see the text \'{text}\'')
def step_they_see_the_text_text(context, text):
    context.test.assertContains(context.response, text)


@then('they see a form with the following fields')
def step_they_see_a_form_with_fields(context):
    for row in context.table:
        if all(map(lambda x: x == '-', row['label'])):
            continue
        context.test.assertContains(context.response, row['label'])


def add_value_to_field(context, label, value):
    if not hasattr(context, 'soup'):
        context.soup = bs(context.response.content, 'html.parser')
    if not hasattr(context, 'payload'):
        context.payload = {x.get('name'): x.get('value')
                           for x in context.soup.find_all('input')}
        context.payload.update({x.get('name'): x.text
                                for x in context.soup.find_all('textarea')})
    id_ = context.soup.find('label', text=label).get('for')
    name = context.soup.find(id=id_).get('name')
    context.payload[name] = value


@given('in the "{label}" field, enters "{value}"')
def step_enters_value_in_the_field(context, label, value):
    add_value_to_field(context, label, value)


@given('in the "{label}" field, enters')
def step_enters_long_value_in_the_field(context, label):
    add_value_to_field(context, label, context.text)


@when('they submit the form')
def step_submit_form(context):
    url = context.soup.form.get('action', context.url)
    context.response = context.client.post(url, data=context.payload)


@then('they are redirected to \'{url}\'')
def step_then_redirected_to(context, url):
    context.test.assertRedirects(context.response, url)


@then('welcome emails are sent to {num:d} recipients')
def step_welcome_emails_sent(context, num):
    context.test.assertEqual(len(mail.outbox), num)
