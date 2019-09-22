import unittest
from hamcrest import assert_that, equal_to

def test_app_returns_404_if_resource_does_not_exist(client):
    response = client.get('does/not/exist')
    assert_that(response.status_code, equal_to(404))

def test_post_healthcheck_not_allowed(client):
    response = client.post('api/healthcheck')
    assert_that(response.status_code, equal_to(405))

def test_get_healthcheck_endpoint_exists(client):
    response = client.get('api/healthcheck')
    assert_that(response.status_code, equal_to(200))

