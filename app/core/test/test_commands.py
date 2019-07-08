from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTest(TestCase):

    def test_wait_for_db_ready(self):
        """ Test wait for db when db is available """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value = True)
    def test_wait_for_db(self, ts): # Second argument because of the @ Decorator
        """ Test wait for db when db is not available """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] # Returns 5 Operational errors and then true
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
