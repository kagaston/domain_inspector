import unittest
from unittest.mock import patch
from domain_inspector.services import get_domain_data


class TestWhoisService(unittest.TestCase):

    @patch('whois.whois')
    def test_get_domain_data(self, mock_whois):
        mock_whois.return_value = {'domain_name': 'block.xyz'}
        result = get_domain_data('block.xyz')
        self.assertEqual(result['domain_name'], 'block.xyz')


if __name__ == '__main__':
    unittest.main()
