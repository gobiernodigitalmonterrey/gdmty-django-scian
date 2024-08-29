from django.test import TestCase
from cat_scian.models import SCIAN

class SCIANTest(TestCase):
    fixtures = ["fixtures/SCIANFixture.json"]

    def test_scian(self):
        scian = SCIAN.objects.get(id=11)
        self.assertEqual(scian.id, 11)

    