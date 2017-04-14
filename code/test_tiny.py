import pytest
import approver
import os

def test_id_parser(monkeypatch):
    res = approver.parse_cert_id_from_email('/code/code/email_file')
    assert res == "97eccaf6-9ea3-4681-958f-cfdf8c4969bd"


def test_is_acm():
    cert_id = "e574ed09-a4fb-4cf8-beb9-7f969c436c10"
    res = approver.is_acm(cert_id, TestContext())
    assert res



class TestContext():
    def __init__(self):
        self.invoked_function_arn = 'a:a:a:us-west-2:601394826940'
