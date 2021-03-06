django-urlactive-lite
=====================

A small template tag library for django, that makes highlighting active links easy.

visit the [github](https://github.com/nalourie/django-urlactive-lite).

# Purpose

This library is extremely light weight, and I probably won't add any new features. There are many larger libraries out there that already provide many more features for navigation, so I'd suggeset that people use those instead.

This library is meant partially for people who just want one simple tag to add an "active" class to a navigation link, but mostly just as a simple example of how to create a template tag in django.

# Installation

from the command line:

```
pip install django-urlactive-lite
```

In your `settings.py` file, add `urlactive` to `INSTALLED_APPS`

```python
INSTALLED_APPS = (
	...
	'urlactive',
	...
)
```

And add `django.core.context_processors.request` to your `TEMPLATE_CONTEXT_PROCESSORS` setting in `settings.py`. Remember to include the other default template context processors:

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
	...
    "django.core.context_processors.request",
	...
)
```

# Usage

## `{% url_active ... %}`'

### arguments

The `{% url_active ... %}` template tag takes one argument, a url, and prints `"active"` if the url passed as an argument is the same as the url from which the page is rendered.

### example

Don't forget to load the template tag library.

```html
{% load urlactive %}
...
...
...
<ul class="nav">
	{% url 'first_url_name' as first_url %}
	<li class="{% url_active first_url %}">
		<a href="{{ first_url }}"> First </a>
	</li>
	
	{% url 'second_url_name' as second_url %}
	<li class="{% url_active second_url %}">
		<a href="{{ second_url }}">Second</a>
	</li>
	
	{% url 'third_url_name' as third_url %}
	<li class="{% url_active third_url %}">
		<a href="{{ third_url }}">Third</a>
	</li>
</ul>
```

# Contributing

There are already many great projects for django around template tags for navigation, so I'm not looking to extend this project. Of course, feel free to fork it and do whatever you want with the code.
