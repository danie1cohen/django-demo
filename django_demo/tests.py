from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class TestViews(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index(self):
        r = self.c.get(reverse('index'))
        assert r.status_code == 200
