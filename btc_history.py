import bitcoin as bt

#any bitcoin Address
btc_address = '13dMHRKdcj17yGkuaxAbayiPsi3JSJKsky'

#btc_address = input("Enter a BitCoin Address: ")

#prints the history of the bitcoin address
history = bt.history(btc_address)
print(history)
