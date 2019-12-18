import bitcoin as bt

#1st Sig
private_key1 = bt.random_key()
public_key1 = bt.privttopub(private_key1)
#2nd Sig
private_key2 = bt.random_key()
public_key2 = bt.privttopub(private_key2)
#3rd Sig
private_key3 = bt.random_key()
public_key3 = bt.privttopub(private_key3)

multi_sig = bt.mk_multisig_script(public_key1, public_key2, public_key3, 2,3)
btc_address = scriptaddr(multi_sig)

#with open('data.txt', 'w') as fob:
#    fob.write('Private Key1: ' + private_key1 + '\nPrivate Key2: ' + private_key2 + '\nPrivate Key3: ' + private_key3 + 'nPublic Key1: ' + public_key1 + '\nPublic Key2: ' + public_key2 + '\nPublic Key3: ' + public_key3 + '\nBTC  Address: '+bitcoin_address+'\n')
#    fob.close()

print('Private Key1:', private_key1)
print('Private Key2:', private_key2)
print('Private Key3:', private_key3)
print('BTC  Address:', btc_address)
