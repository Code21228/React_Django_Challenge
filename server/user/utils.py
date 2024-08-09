from web3 import Web3
from core import settings
# Connect to an Ethereum node
# You can use Infura, Alchemy, or your own node
INFURA_URL = f"https://mainnet.infura.io/v3/{settings.INFURA_KEY}"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_eth_balance(address):
    # Ensure the address is valid
    if not web3.is_address(address):
        return "Invalid Ethereum address"
    
    # Get the balance in Wei
    balance_wei = web3.eth.get_balance(address)
    
    # Convert Wei to Ether
    balance_eth = web3.from_wei(balance_wei, 'ether')
    
    return balance_eth