import random
from bit import *
from bit.format import bytes_to_wif
import hashlib
import base58
import binascii
#5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4vz2VxEJVe5ANUVRj
#5HpHagT65TZ*G1PH3CSu63k8D**vD8s5ip4vz2VxE**e5ANUVRj
add = '1EC6zJAVxdwUk2gt5upAuGpD68fic8191v '
count=0
while True:
    count+=1
    c1 = str (random.choice('5'))
    c2 = str (random.choice('H'))
    c3 = str (random.choice('p'))
    c4 = str (random.choice('H'))
    c5 = str (random.choice('a'))
    c6 = str (random.choice('g'))
    c7 = str (random.choice('T'))
    c8 = str (random.choice('6'))      
    c9 = str (random.choice('5'))
    c10 = str (random.choice('T'))
    c11 = str (random.choice('Z'))
    c12 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c13 = str (random.choice('G'))
    c14 = str (random.choice('1'))
    c15 = str (random.choice('P'))
    c16 = str (random.choice('H'))
    c17 = str (random.choice('3'))
    c18 = str (random.choice('C'))
    c19 = str (random.choice('S'))
    c20 = str (random.choice('u'))
    c21 = str (random.choice('6'))
    c22 = str (random.choice('3'))
    c23 = str (random.choice('k'))
    c24 = str (random.choice('8'))
    c25 = str (random.choice('D'))
    c26 = str (random.choice('b'))
    c27 = str (random.choice('p'))
    c28 = str (random.choice('v'))
    c29 = str (random.choice('D'))
    c30 = str (random.choice('8'))
    c31 = str (random.choice('s'))
    c32 = str (random.choice('5'))
    c33 = str (random.choice('i'))
    c34 = str (random.choice('p'))
    c35 = str (random.choice('4'))
    c36 = str (random.choice('v'))
    c37 = str (random.choice('z'))
    c38 = str (random.choice('2'))
    c39 = str (random.choice('V'))
    c40 = str (random.choice('x'))
    c41 = str (random.choice('E'))
    c42 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c43 = str (random.choice('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'))
    c44 = str (random.choice('e'))
    c45 = str (random.choice('5'))
    c46 = str (random.choice('A'))
    c47 = str (random.choice('N'))
    c48 = str (random.choice('U'))
    c49 = str (random.choice('V'))
    c50 = str (random.choice('R'))
    c51 = str (random.choice('j'))
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
    print(' Scanning : ', count,' : Current TEST WIF= ', private_key_WIF, end='\r')
    #print('\n GOOD LUCK AND HAPPY HUNTING', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
    #print( addr,wif)
    #print(addr1,wif1)
    if addr in add or addr1 in add:
        print('\n Congraz FOUND!!!', '\nPrivateKey= ', private_key.decode('utf-8'), '\nCompressed Address = ', addr, '\nCompressed WIF = ', wif1, '\nUncompressed = ', addr1, '\nUncompressed WIF = ', wif)
        f=open('winner.txt','a')
        f.write('\n Congraz FOUND!!!' + '\nPrivateKey= ' + private_key.decode('utf-8') + '\nCompressed Address = ' + addr + '\nCompressed WIF = ' + wif1 + '\nUncompressed = ' + addr1 + '\nUncompressed WIF = ' + wif)
        f.close()