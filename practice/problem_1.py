from collections import defaultdict, Counter
from email.policy import default


def transaction_logs(s):
    merchants = defaultdict(lambda: [0,0])
    for t in s:
        _, merchant, amount = t.split()
        amount = int(amount)
        merchants[merchant][0] += amount 
        merchants[merchant][1] += 1

    result = []
    for merchant, (amount, count) in merchants.items():        
        result.append((merchant, amount, count))
    
    result.sort(key=lambda x: (-x[1], x[0]))
    return [f"{m} {net} {count}" for m, net, count in result]
    



transactions = [
  "1001 amazon 500",
  "1002 walmart 300",
  "1003 amazon -100",
  "1004 target 500",
  "1005 walmart 200",
  "1006 amazon 400",
  "1007 target -500"
]
print(  transaction_logs(transactions))