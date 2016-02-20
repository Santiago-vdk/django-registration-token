from django.test import TestCase

from django_registration_token.models import InvitationCode

class InvitationCodeTestCase(TestCase):
    def test_token_generation(self):
        i = 5
        while i > 0:
            try:
                token = InvitationCode()
                token.save()
                print(token.code)
                print('\x1b[0m')
                i -= 1
            except:
                self.assertEqual(i,0)
        self.assertEqual(i,0)
