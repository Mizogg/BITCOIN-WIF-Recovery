import random
from bit import *
from bit.format import bytes_to_wif
import hashlib
import base58
import binascii
add = '1K4ezpLybootYF23TM4a8Y4NyP7auysnRo' # wallet address need to recover
count=0
while True:
    count+=1
    c1 = str (random.choice('5'))
    c2 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c3 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c4 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c5 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c6 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c7 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c8 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))      
    c9 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c10 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c11 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c12 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c13 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c14 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c15 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c16 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c17 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c18 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c19 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c20 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c21 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c22 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c23 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c24 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c25 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c26 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c27 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c28 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c29 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c30 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c31 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c32 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c33 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c34 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c35 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c36 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c37 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c38 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c39 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c40 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c41 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c42 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c43 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c44 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c45 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c46 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c47 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c48 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c49 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c50 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c51 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    private_key_WIF = (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38+c39+c40+c41+c42+c43+c44+c45+c46+c47+c48+c49+c50+c51)
    first_encode = base58.b58decode(private_key_WIF)
    private_key_full = binascii.hexlify(first_encode)
    private_key = private_key_full[2:-8]
    key = Key.from_hex(str(private_key.decode('utf-8')))
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    addr = key.address
    addr1 = key1.address
    #print(' Scanning : ', count,' : Current TEST WIF= ', private_key_WIF, end='\r')
    print('\n GOOD LUCK AND HAPPY HUNTING', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
    if addr in add or addr1 in add:
        print('\n Congraz FOUND!!!', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
        f=open('winner.txt','a')
        f.write('\n Congraz FOUND!!!' + '\nPrivateKey= ' + private_key.decode('utf-8') + '\nCompressed Address = ', addr + '\nCompressed WIF = ' + wif1 + '\nUncompressed = ' + addr1 + '\nUncompressed WIF = ' + wif)
        f.close()