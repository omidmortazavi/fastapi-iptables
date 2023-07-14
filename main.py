import iptc
from enum import Enum

from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/tables/")
def get_all_tables() -> dict:
    result = iptc.easy.dump_all()
    return result


@app.put("/add-chain/{table}/{chain}")
def add_chain_route(table: str, chain: str):
    """
    Endpoint to add a chain to an iptables table.

    Args:
        table (str): The name of the iptables table.
        chain (str): The name of the chain to be added.

    Returns:
        dict: A JSON response with a success message.
    """
    iptc.easy.add_chain(table, chain)
    return {"message": f"Chain {chain} added to table {table}."}


@app.delete("/delete-chain/{table}/{chain}")
def delete_chain_route(table: str, chain: str):
    """
    Deletes the specified chain from the iptables table.

    Args:
        table (str): The name of the iptables table.
        chain (str): The name of the chain to be deleted.
    """
    iptc.easy.delete_chain(table, chain)
    return {"message": f"Chain {chain} deleted from table {table}."}


@app.get("/", include_in_schema=False)
def root():
    """
    Root endpoint to redirect users to the documentation.
    """
    return RedirectResponse(url="/docs")
