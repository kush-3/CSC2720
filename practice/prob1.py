from collections import defaultdict
from typing import List


def transaction_pairs(transactions):

    seen = set()

    for transaction in transactions:
        sender, receiver = transaction.split()
        seen.add((sender, receiver))

    pairs = set()

    for sender, receiver in seen:
        if (receiver, sender) in seen:
            pair = tuple(sorted([sender, receiver]))
            pairs.add(pair)

    return len(pairs)


transactions = [
  "alice bob",
  "alice bob",
  "bob alice",
  "alice charlie",
  "charlie alice",
  "bob charlie",
  "dave alice"
]
print(transaction_pairs(transactions))