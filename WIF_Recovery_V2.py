import itertools, random
from bit import *
from bit.format import bytes_to_wif
import hashlib
import base58
import binascii

alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

miss = int(input('How Many Missing Chars Enter 0 for none : '))

def iter_all(count):
    if count == 0:
        yield start
    else:
        for a in alphabet:
            if count == a:
                continue
            else:
                for scan in iter_all(count-1):
                    yield scan + a
total=0 

if miss == 0:
    startsingle= str(input('Enter Your WIF HERE : '))
    if startsingle[0] == '5':
        private_key_WIF = startsingle
        first_encode = base58.b58decode(private_key_WIF)
        private_key_full = binascii.hexlify(first_encode)
        private_key = private_key_full[2:-8]
    elif startsingle[0] in ['L', 'K']:
        private_key_WIF = startsingle
        first_encode = base58.b58decode(private_key_WIF)
        private_key_full = binascii.hexlify(first_encode)
        private_key = private_key_full[2:-10]
    key = Key.from_hex(str(private_key.decode('utf-8')))
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    addr = key.address
    addr1 = key1.address
    print('\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
    f=open('winner.txt','a')
    f.write('\nPrivateKey= ' + private_key.decode('utf-8') + '\nCompressed Address = ' + addr + '\nCompressed WIF = ' + wif1 + '\nUncompressed = ' + addr1 + '\nUncompressed WIF = ' + wif)
    f.close()
else:
    start= str(input('Leave Bank or Input Starting Part : '))
    stop = str(input('Leave Bank or Input Ending Part : '))
    add= str(input('Enter Bitcoin address Looking to match WIF = '))
    for a in iter_all(miss):
        total+=1
        if start[0] == '5':
            private_key_WIF = a + stop
            first_encode = base58.b58decode(private_key_WIF)
            private_key_full = binascii.hexlify(first_encode)
            private_key = private_key_full[2:-8]
        elif start[0] in ['L', 'K']:
            private_key_WIF = a + stop
            first_encode = base58.b58decode(private_key_WIF)
            private_key_full = binascii.hexlify(first_encode)
            private_key = private_key_full[2:-10]
        key = Key.from_hex(str(private_key.decode('utf-8')))
        wif = bytes_to_wif(key.to_bytes(), compressed=False)
        wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wif)
        addr = key.address
        addr1 = key1.address
        print(' Scanning : ', total,' : Current TEST WIF= ', private_key_WIF, end='\r')
        #print('\n GOOD LUCK AND HAPPY HUNTING', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
        if addr in add or addr1 in add:
            print('\n Congraz FOUND!!!', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
            f=open('winner.txt','a')
            f.write('\n Congraz FOUND!!!' + '\nPrivateKey= ' + private_key.decode('utf-8') + '\nCompressed Address = ' + addr + '\nCompressed WIF = ' + wif1 + '\nUncompressed = ' + addr1 + '\nUncompressed WIF = ' + wif)
            f.close()
