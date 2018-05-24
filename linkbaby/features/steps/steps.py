from django.test import Client
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


@then('an unscheduled introduction should be created ' +
      'between {name1} and {name2}')
def step_an_introduction_should_exist(context, name1, name2):
    intro = Introduction.objects.filter(
        recipients__name=name1).filter(
        recipients__name=name2).filter(
        scheduled_at__isnull=True,
    )
    context.test.assertEqual(len(intro), 1)


@then('the total number of introductions should be {num:d}')
def step_the_total_number_of_introductions_should_be_num(context, num):
    context.test.assertEqual(Introduction.objects.count(), num)


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
    # TODO: field types are currently ignored
    for row in context.table:
        context.test.assertContains(context.response, row['label'])


@when('the user submits the following data')
def step_user_submits_data(context):
    soup = bs(context.response.content, 'html.parser')
    url = soup.form.get('action', context.url)
    payload = {x.get('name'): x.get('value') for x in soup.find_all('input')}
    payload.update({x.get('name'): x.text for x in soup.find_all('textarea')})
    for row in context.table:
        id_ = soup.find('label', text=row['label']).get('for')
        name = soup.find(id=id_).get('name')
        payload[name] = row['value']

    context.response = context.client.post(url, data=payload)


@then('the user should be redirected to \'{url}\'')
def step_then_redirected_to(context, url):
    context.test.assertRedirects(context.response, url)


@then('welcome emails are sent to all recipients')
def step_welcome_emails_sent(context):
    raise NotImplementedError('STEP: Then welcome emails are sent ' +
                              'to all recipients')
