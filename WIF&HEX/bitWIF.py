from bit import *
from bit.format import bytes_to_wif
import string
from typing import Generator
from random import SystemRandom as RND
import re
import trotter
from tqdm import tqdm
import hashlib
import base58
import binascii
from rich import print

Mizogg = '''[red]
                ╔═╗╔═╗                   
                ║║╚╝║║                   
                ║╔╗╔╗║╔╗╔═══╗╔══╗╔══╗╔══╗
                ║║║║║║╠╣╠══║║║╔╗║║╔╗║║╔╗║
                ║║║║║║║║║║══╣║╚╝║║╚╝║║╚╝║
                ╚╝╚╝╚╝╚╝╚═══╝╚══╝╚═╗║╚═╗║
                                 ╔═╝║╔═╝║
                                 ╚══╝╚══╝
                  ___            ___  
                 (o o)          (o o) 
                (  V  ) MIZOGG (  V  )
                --m-m------------m-m--
[/red]'''

INPUTNEEDED = '''[yellow]

  ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
  |esc| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | + | ' | <-    |
  |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
  | ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |
  |-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
  | Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |
  |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
  |    | < | Z | X | C | V | B | N | M | , | . | - |          |
  |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
  | ctrl |🪟| alt |                          |altgr |  | ctrl |
  '------'  '-----'--------------------------'------'  '------'    

[/yellow]'''

INPUTNEEDEDWIF = '''[yellow]

  ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
  |esc| [red]1[/red] | [red]2[/red] | [red]3[/red] | [red]4[/red] | [red]5[/red] | [red]6[/red] | [red]7[/red] | [red]8[/red] | [red]9[/red] | [red]0[/red] | + | ' | <-    |
  |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
  | ->| | Q | W | [red]E[/red] | R | T | Y | U | I | O | P | ] | ^ |     |
  |-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
  | Caps | [red]A[/red] | S | [red]D[/red] | [red]F[/red] | G | H | J | K | L | \ | [ | * |    |
  |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
  |    | < | Z | X | [red]C[/red] | V | [red]B[/red] | N | M | , | . | - |          |
  |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
  | ctrl |🪟| alt |                          |altgr |  | ctrl |
  '------'  '-----'--------------------------'------'  '------'    

[/yellow]'''
print(Mizogg)
print(INPUTNEEDED)
print ('[green]WIF Recovery Tool Edit Line 66 For More Information[/green]')
addr_look = str(input('Enter Your Bitcoin Address Here : (Example = 16UX8hrqG2h5idgaqA1zzPDGtmXTkE8deR ) '))

print(INPUTNEEDEDWIF)
print ('[green]WIF Recovery Tool Edit Line 66 For More Information[/green]')
WIF_key_FIND = str(input('Enter WIF with Missing Characters  as * : (Example = KwDiBf**QgGcZwzunkKCSmeavWjCmdZ1CJSDfh*2pHWYV4nLoEoj ) '))


alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

#addr_look = '1M9iGgKRatAXXw43Vr8jUc8eTiBtH6oBYs'
#WIF_key_FIND = '5HpHagT65TZzT3VXYD5aQWboCfucHugso4VpjJNJdYP6hskas5T'
#WIF_key_FIND = '5HpHagT65TZzT3VXY**aQWboCfucHugso4VpjJNJdYP6hskas5T'
#WIF_key_FIND = '5HpHagT65TZzT3VXY****WboCfucHugso4VpjJNJdYP6hskas5T'
#WIF_key_FIND = '5HpHagT65TZzT3VXY**aQWboCfucHugso4VpjJNJdYP6hsk**5T'

#addr_look = '16UX8hrqG2h5idgaqA1zzPDGtmXTkE8deR'

#WIF_key_FIND = 'KwDiBf89QgGcZwzunkKCSmeavWjCmdZ1CJSDfhf2pHWYV4nLoEoj'
#WIF_key_FIND = 'KwDiBf**QgGcZwzunkKCSmeavWjCmdZ1CJSDfhf2pHWYV4nLoEoj'
#WIF_key_FIND = 'KwDiBf**QgGcZwzunkKCSmeavWjCmdZ1CJSDfh*2pHWYV4nLoEoj'
#WIF_key_FIND = 'KwDiBf**QgGcZwz**kKCSmeavWjCmdZ1****fhf2pHWYV4nLoEoj'


def complete_key(WIF_key_FIND_string, missing_letters):
    for letter in missing_letters:
        WIF_key_FIND_string = WIF_key_FIND_string.replace('*', letter, 1)
    #print(f"WIF_key_FIND_string: {WIF_key_FIND_string}", end='\r') # Showing more info but slower
    return WIF_key_FIND_string

if __name__ == '__main__':
    missing_length = WIF_key_FIND.count('*')
    print(f"Looking for {missing_length} characters in {WIF_key_FIND}")
    allowed_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    missing_letters_master_list = trotter.Amalgams(missing_length, allowed_characters)
    print(missing_letters_master_list)
    print(len(missing_letters_master_list))
    for i in tqdm(range(len(missing_letters_master_list))):
        test_key = complete_key(WIF_key_FIND, missing_letters_master_list[i])
        try:
            if test_key[0] == '5':
                private_key_WIF = test_key
                first_encode = base58.b58decode(private_key_WIF)
                private_key_full = binascii.hexlify(first_encode)
                private_key = private_key_full[2:-8]
            elif test_key[0] in ['L', 'K']:
                private_key_WIF = test_key
                first_encode = base58.b58decode(private_key_WIF)
                private_key_full = binascii.hexlify(first_encode)
                private_key = private_key_full[2:-10]
            key = Key.from_hex(str(private_key.decode('utf-8')))
            wif = bytes_to_wif(key.to_bytes(), compressed=False)
            wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
            key1 = Key(wif)
            uaddr = key.address
            caddr = key1.address
            #print(f"key: {test_key} address: {addr}", end='\r')
            if uaddr in addr_look or caddr in addr_look:
                print ('WINNER WINNER Check WINNER.txt')
                f=open('WINNER.txt','a')
                f.write('===========================================================================\n')
                f.write(f"TEST Key: {test_key} \nWIF Key Uncompressed: {wif} \nBTC Address Uncompressed: {uaddr} \nWIF Key Compressed: {wif1} \nBTC Address Compressed: {caddr}\n")
                f.write('===========================================================================\n')
                f.close()

        except ValueError:
            pass