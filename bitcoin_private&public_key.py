import bitcoin as bt
#private Key
private_key = bt.random_key()
public_key = bt.privtopub(private_key)
with open('data.txt', 'w') as fob:
    fob.write(private_key+'\n'+public_key)
    fob.close()

print('Private Key:', private_key)
print('Public Key:', public_key)
