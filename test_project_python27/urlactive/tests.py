from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .templatetags.urlactive import url_active, ACTIVE_STRING

class UrlActiveTests(TestCase):
    """tests for the url_active template tag."""
    urls = 'urlactive.test_urls'

    def test_prints_active_when_at_url(self):
        """verify that the url_active tag renders to 
        the ACTIVE_STRING when rendered from the url
        it is passed as an argument.
        """
        c = Client()
        self.assertIn(
            'before' + ACTIVE_STRING + 'after',
            c.get(reverse('a-url')).content)

    def test_doesnt_print_active_when_not_at_url(self):
        """verfiy that the url_active tag does not render
        to the ACTIVE_STRING when it is rendered from a url
        which is different from the url it was passed as an
        argument.
        """
        c = Client()
        self.assertNotIn(
            'before' + ACTIVE_STRING + 'after',
            c.get(reverse('a-different-url')).content)
