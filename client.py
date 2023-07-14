import requests

base_url = "http://127.0.0.1:8000"


def make_request(method, url):
    response = method(url)
    print(f"{method.__name__.upper()} {url}")
    print(f"Response: {response.status_code}")
    print(response.json())
    print()


def get_tables():
    url = f"{base_url}/tables/"
    make_request(requests.get, url)


def put_chain():
    url = f"{base_url}/add-chain/filter/test_chain"
    make_request(requests.put, url)


def delete_chain():
    url = f"{base_url}/delete-chain/filter/test_chain"
    make_request(requests.delete, url)


if __name__ == "__main__":
    print("Running iptables operations...")

    # Get tables
    print("Getting tables...")
    get_tables()
    print("############")

    # Add chain
    print("Adding chain...")
    put_chain()
    print("Chain added.")
    print("############")

    # Get tables after adding chain
    print("Getting tables after adding chain...")
    get_tables()
    print("############")

    # Delete chain
    print("Deleting chain...")
    delete_chain()
    print("Chain deleted.")
    print("############")

    # Get tables after deleting chain
    print("Getting tables after deleting chain...")
    get_tables()
    print("############")
