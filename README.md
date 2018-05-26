# link.baby

![logo inspiration](logo-inspiration.png)

[![Build Status](https://travis-ci.org/andylolz/link.baby.svg?branch=master)](https://travis-ci.org/andylolz/link.baby)

At the end of a meetup or event, it’s really tempting to set up a [mailing list](https://en.wikipedia.org/wiki/Electronic_mailing_list) / [slack](https://slack.com/) / [whatsapp](https://www.whatsapp.com) group etc to “keep the conversation going”. But for a number of reasons, these rarely work out.

Instead:

 1. the facilitator shares the email addresses of attendees with [link.baby](https://link.baby), along with some introductory email copy.
 2. [link.baby](https://link.baby) contacts all participants with the facilitator’s introductory email. Participants are asked to opt in by clicking a link and providing a short bio.
 3. Those who opt in then receive a series of emails from [link.baby](https://link.baby) – one per day – introducing them to a different attendee
 4. Participants can opt out at any time, using the opt out link

### Requirements

Python 3.6 or thereabouts.

### Installation

This is a django site. It’s all pretty standard.

1. Clone the repo:

    ```shell
    git clone https://github.com/andylolz/link.baby.git linkbaby
    cd linkbaby
    ```

2. Create a virtualenv:

    ```shell
    pyvenv venv
    ```

3. Copy the settings:

    ```shell
    cp core/settings/local.py.example core/settings/local.py
    echo "DJANGO_SETTINGS_MODULE=core.settings.local" > .env
    ```

4. Update `core/settings/local.py` with your settings. Then load the env:

    ```shell
    source venv/bin/activate
    ```

5. Install the dependencies:

    ```shell
    pip install requirements/local.txt
    ```

6. Setup the database:

    ```shell
    python manage.py migrate
    ```

### Running

```shell
python manage.py runserver
```

### Testing

```shell
DJANGO_SETTINGS_MODULE="core.settings.testing" python manage.py behave
```

### Setting up on heroku

```shell
heroku create app-name
heroku config:set DJANGO_SETTINGS_MODULE=core.settings.heroku
```

### Deploying to Heroku

```shell
git remote add heroku https://git.heroku.com/linkbaby.git
git push heroku master
```