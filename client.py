import requests
import logging
from rich.logging import RichHandler

base_url = "http://127.0.0.1:8000"


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)
log = logging.getLogger("iptables")

def make_request(method, url):
    response = method(url)
    log.info(f"{method.__name__.upper()} {url}")
    log.info(f"Response: {response.status_code}")
    log.info(response.json())
    log.info("")


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
    log.info("Running iptables operations...")

    # Get tables
    log.info("Getting tables...")
    get_tables()

    # Add chain
    log.info("Adding chain...")
    put_chain()
    log.info("Chain added.")

    # Get tables after adding chain
    log.info("Getting tables after adding chain...")
    get_tables()

    # Delete chain
    log.info("Deleting chain...")
    delete_chain()
    log.info("Chain deleted.")

    # Get tables after deleting chain
    log.info("Getting tables after deleting chain...")
    get_tables()