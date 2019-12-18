import bitcoin as bt
#private Key
private_key = bt.random_key()
#public Key
public_key = bt.privtopub(private_key)

#also generates a text file if you like to save that
#with open('data.txt', 'w') as fob:
#    fob.write('Private Key: '+private_key+'\nPublic  Key: '+public_key+'\n')
#    fob.close()

print('Private Key:', private_key)
print('Public Key:', public_key)
