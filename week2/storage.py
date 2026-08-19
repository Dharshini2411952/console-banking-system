from collections import defaultdict

# Main account storage
accounts = {}

# Transaction history for each account
transactions = defaultdict(list)

# Customer name -> account IDs
customer_index = defaultdict(list)