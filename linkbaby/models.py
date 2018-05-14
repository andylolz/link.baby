from django.db import models
from django.utils import timezone


class EventOrganiser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    organiser = models.ForeignKey(EventOrganiser, on_delete=models.CASCADE)
    welcome_message = models.TextField()
    took_place_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class EventAttendee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    last_contacted_at = models.DateTimeField(null=True)
    last_scheduled_at = models.DateTimeField(null=True)
    subscribed_at = models.DateTimeField(null=True)
    unsubscribed_at = models.DateTimeField(null=True)

    @property
    def is_subscribed(self):
        if self.subscribed_at is None:
            return False
        if self.unsubscribed_at is not None:
            return False
        try:
            Unsubscribe.objects.get(email=self.email)
        except:
            return True
        return False

    def subscribe_to_introductions(self):
        self.subscribed_at = timezone.now()
        self.save()
        self.initialise_introductions()

    def initialise_introductions(self):
        others = list(
            EventAttendee.objects.filter(
                event=self.event,
                subscribed_at__isnull=False,
                unsubscribed_at__isnull=True,
            ).exclude(
                pk=self.pk,
            )
        )
        for other in others:
            if not other.is_subscribed:
                continue
            intro = Introduction(event=self.event)
            intro.save()
            intro.recipients.add(other)
            intro.recipients.add(self)

    def __str__(self):
        return self.name


class Unsubscribe(models.Model):
    email = models.EmailField()
    unsubscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Introduction(models.Model):
    recipients = models.ManyToManyField(EventAttendee)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
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


class Email(models.Model):
    pass