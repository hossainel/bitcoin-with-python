import bitcoin as bt

#any bitcoin Address
btc_address = '329e5RtfraHHNPKGDMXNxtuS4QjZTXqBDg'

#btc_address = input("Enter a BitCoin Address: ")

#prints the history of the bitcoin address
history = bt.history(btc_address)
for i in history:
  for j in i:
    print(j, ":", i[j])

