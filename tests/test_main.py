import unittest
from unittest.mock import patch
from domain_inspector.config import Config
from domain_inspector.main import main


class TestConfig(unittest.TestCase):

    @patch.dict('os.environ', {
        'DATABASE_URL': 'sqlite:///test_database.db',
        'SECRET_KEY': 'testsecretkey',
        'DEBUG': 'True'
    })
    def test_config_values(self):
        config = Config()
        self.assertEqual(config.get_database_url(), 'sqlite:///test_database.db')
        self.assertEqual(config.get_secret_key(), 'testsecretkey')
        self.assertEqual(config.get_debug(), 'True')


class TestMain(unittest.TestCase):

    @patch('builtins.print')
    @patch.dict('os.environ', {
        'DATABASE_URL': 'sqlite:///test_database.db',
        'SECRET_KEY': 'testsecretkey',
        'DEBUG': 'True'
    })
    def test_main_debug_on(self, mock_print):
        main()
        mock_print.assert_any_call("Database URL: sqlite:///test_database.db")
        mock_print.assert_any_call("Secret Key: testsecretkey")
        mock_print.assert_any_call("Debug Mode: True")
        mock_print.assert_any_call("Debug mode is on")

    @patch('builtins.print')
    @patch.dict('os.environ', {
        'DATABASE_URL': 'sqlite:///test_database.db',
        'SECRET_KEY': 'testsecretkey',
        'DEBUG': 'False'
    })
    def test_main_debug_off(self, mock_print):
        main()
        mock_print.assert_any_call("Database URL: sqlite:///test_database.db")
        mock_print.assert_any_call("Secret Key: testsecretkey")
        mock_print.assert_any_call("Debug Mode: False")
        mock_print.assert_any_call("Debug mode is off")


if __name__ == '__main__':
    unittest.main()
