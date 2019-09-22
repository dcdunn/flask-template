import unittest
import requests
from hamcrest import assert_that, equal_to, has_key, has_entry

APP_URL="http://app:5000"

class TestHealthcheck(unittest.TestCase):

    def test_healthcheck_exists(self):
        resp = requests.get(f'{APP_URL}/api/healthcheck')
        assert_that(resp.status_code, equal_to(200))
        body = resp.json()
        assert_that(body, has_key("data"))
        assert_that(body["data"], has_entry("type", "healthcheck"))

