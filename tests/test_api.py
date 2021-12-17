import requests

# Simple test script - execute when the app is running
url = "http://127.0.0.1:5000"

one_addresses = [
    "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3",
    "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
    "one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2",
    "somewrongaddress",
]

happy_flow = {"addresses": one_addresses}
wrong_address = {"addresses": ["somewrongaddress"]}
wrong_key = {"wrong_key": ""}
empty_request = {"addresses": []}


def make_request(params: dict) -> list:
    res = requests.post(url, params=params).json()
    print(res)
    return res


def base(params: list, expected: str, status: str = None) -> None:
    for p in params:
        r = make_request(p)
        assert r[0].get(expected)
        if status:
            assert r[0].get(expected) == status


def test_happy_flow():
    base((happy_flow,), "status")


def test_wrong_address():
    base((wrong_address,), "status", status="error")


def test_error_responses():
    base((wrong_key, empty_request), "error")


if __name__ == "__main__":
    # test request
    params = {"addresses": "SomeAddress"}
    make_request(params)

    # manual check tests. - uncomment to run.

    # test_happy_flow()
    # test_error_responses()
    # test_wrong_address()