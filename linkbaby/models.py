from email.utils import formataddr

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Host(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('host name'))
    email = models.EmailField(_('email address'), blank=False, null=False)

    @property
    def formatted_email(self):
        return formataddr((self.name, self.email))

    def __str__(self):
        return self.name


class Linkup(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('linkup name'))
    host = models.ForeignKey(Host, on_delete=models.CASCADE,
                             blank=False, null=False)
    welcome_message = models.TextField(blank=True, null=False)

    def send_welcome_emails(self):
        linkees = self.linkee_set.filter(welcome_sent_at=None)
        content = self.welcome_message
        subject = '{} - Linkup'.format(self.name)
        from_email = self.host.formatted_email
        for linkee in linkees:
            params = {'content': content, 'linkee': linkee}
            msg_txt = render_to_string('welcome_message.txt', params)
            msg_html = render_to_string('welcome_message.html', params)
            send_mail(subject=subject, from_email=from_email,
                      recipient_list=[linkee.formatted_email],
                      message=msg_txt, html_message=msg_html,
                      fail_silently=False)
            linkee.welcome_sent_at = timezone.now()
            linkee.save()

    @property
    def subscribed_linkees(self):
        return self.linkee_set.filter(
            subscribed_at__isnull=False,
            unsubscribed_at__isnull=True,
        )

    def __str__(self):
        return self.name


class Linkee(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    email = models.EmailField(_('email address'), blank=False, null=False)
    bio = models.TextField()
    linkup = models.ForeignKey(Linkup, on_delete=models.CASCADE)
    welcome_sent_at = models.DateTimeField(null=True)
    last_contacted_at = models.DateTimeField(null=True)
    last_scheduled_at = models.DateTimeField(null=True)
    subscribed_at = models.DateTimeField(null=True)
    unsubscribed_at = models.DateTimeField(null=True)

    @property
    def formatted_email(self):
        return formataddr((self.name, self.email))

    @property
    def is_subscribed(self):
        if self.subscribed_at is None:
            return False
        if self.unsubscribed_at is not None:
            return False
        return True

    def unsubscribe(self):
        if self.unsubscribed_at is not None:
            raise Exception('Already unsubscribed')
        self.unsubscribed_at = timezone.now()
        self.save()
        self.delete_introductions()

    def subscribe(self):
        if self.subscribed_at is not None:
            raise Exception('Already subscribed')
        self.subscribed_at = timezone.now()
        self.save()
        self.initialise_introductions()

    def initialise_introductions(self):
        # TODO: prevent re-initialisation
        for subscriber in self.linkup.subscribed_linkees:
            if subscriber == self:
                continue
            if not subscriber.is_subscribed:
                continue
            intro = Introduction(linkup=self.linkup)
            intro.save()
            intro.recipients.add(subscriber)
            intro.recipients.add(self)

    def delete_introductions(self):
        self.introduction_set.all().delete()

    def __str__(self):
        return self.name


class Introduction(models.Model):
    recipients = models.ManyToManyField(Linkee)
    linkup = models.ForeignKey(Linkup, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField(null=True)
    introduced_at = models.DateTimeField(null=True)

    # @classmethod
    # def schedule_to_send(cls):
    #     introductions = cls.where(introduced_at=None)
    #     while len(introductions) > 0:
    #         introduction = introductions.pop(0)
    #         Schedule(introduction)
    #         total_introcutions = len(introductions)
    #         *** introductions = ifilter()
    #         for x in range(total_introcutions):
    #             for recipient in introduction.recipients:
    #                 if recipient in introductions[x].recipients:
    #                     del introductions[x]
    #                     x += 1
    #                     break

    def __str__(self):
        recipients = self.recipients.all()
        return ', '.join([str(r) for r in recipients])
