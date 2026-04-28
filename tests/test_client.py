from cathode import CathodeClient


def test_client_default_base_url():
    client = CathodeClient(api_key="test-key")
    assert client.base_url == "https://api.cathode.cloud"
    client.close()


def test_client_custom_base_url():
    client = CathodeClient(api_key="test-key", base_url="https://custom.api/")
    assert client.base_url == "https://custom.api"
    client.close()


def test_client_context_manager():
    with CathodeClient(api_key="test-key") as client:
        assert client.base_url == "https://api.cathode.cloud"
