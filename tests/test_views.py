from asosiy.models import *
from statsapp.models import *
from unittest import TestCase
from rest_framework.test import APIClient

class TestClientApiViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def client_all_test_view(self):
        natija = self.client.get('/clientlar/')
        print('sa')
        assert natija.status_code == 200
class TestStatsApiViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def stats_all_test_view(self):
        natija = self.client.get('/stats/')
        assert natija.status_code == 200
