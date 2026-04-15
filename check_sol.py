import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
address = "266Z687YV6WfbzS67C6YpY9qYvE9p6qYvE9p6qYvE9p6"
def get_solana_balance(address, api_key):
    url = f"https://mainnet.helius-rpc.com/?api-key={api_key}"
    payload = {
        "jsonrpc": "2.0",
        "id": "my-id",
        "method": "getAssetsByOwner",
        "params": {
            "ownerAddress": address,
            "page": 1,
            "limit": 1000
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_parsed_transactions(address, api_key):
    url = f"https://api.helius.xyz/v0/addresses/{address}/transactions?api-key={api_key}"
    response = requests.get(url)
    # Helius 会直接告诉你：这是一个 "SWAP"、"BET" 还是 "TRANSFER"
    return response.json()
if __name__ == "__main__":
    balance = get_solana_balance(address, API_KEY)
    print(balance)
    transactions = get_parsed_transactions(address, API_KEY)
    print(transactions)
