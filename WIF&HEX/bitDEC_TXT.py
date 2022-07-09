from bit import *
from bit.format import bytes_to_wif
import string
import re
import trotter
from tqdm import tqdm
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

print('Bitcoin Addresses Loading Please Wait: ')

filename ='btc.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

INPUTNEEDEDDEC = '''[yellow]

  ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
  |esc| [red]1[/red] | [red]2[/red] | [red]3[/red] | [red]4[/red] | [red]5[/red] | [red]6[/red] | [red]7[/red] | [red]8[/red] | [red]9[/red] | [red]0[/red] | + | ' | <-    |
  |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
  | ->| | Q | W | E | R | T | Y | U | I | O | P | ] | ^ |     |
  |-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
  | Caps | A | S | D | F | G | H | J | K | L | \ | [ | * |    |
  |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
  |    | < | Z | X | C | V | B | N | M | , | . | - |          |
  |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
  | ctrl |🪟| alt |  **  MAX 18 MISSING  **  |altgr |  | ctrl |
  '------'  '-----'--------------------------'------'  '------'    

[/yellow]'''
print(Mizogg)

print(INPUTNEEDEDDEC)
print ('[green]DEC Recovery Tool **  MAX 18 MISSING  ** [/green]')
DEC_key_FIND = str(input('Enter DEC with Missing Characters  as * : (Example = 23146314254365124563412***** ) \n Enter Here =  '))

def complete_key(DEC_key_FIND_string, missing_letters):
    for letter in missing_letters:
        DEC_key_FIND_string = DEC_key_FIND_string.replace('*', letter, 1)
    #print(f"DEC_key_FIND_string: {DEC_key_FIND_string}", end='\r') # Showing more info but slower
    return DEC_key_FIND_string

if __name__ == '__main__':
    missing_length = DEC_key_FIND.count('*')
    print(f"Looking for {missing_length} characters in {DEC_key_FIND}")
    allowed_characters = '0123456789'
    master_list = trotter.Amalgams(missing_length, allowed_characters)
    print(master_list)
    print(len(master_list))
    for i in tqdm(range(len(master_list))):
        test_key = complete_key(DEC_key_FIND, master_list[i])
        try:
            dec = int(test_key)
            HEX = "%064x" % dec
            key = Key.from_int(dec)
            wifu = bytes_to_wif(key.to_bytes(), compressed=False)
            wifc = bytes_to_wif(key.to_bytes(), compressed=True)
            key1 = Key(wifu)
            caddr = key.address
            uaddr = key1.address
            length = len(bin(dec))
            length -=2
            print(f"DEC: {dec}  bits {length}", end='\r')
            if uaddr in add or caddr in add:
                print ('WINNER WINNER Check WINNER.txt')
                print(f"DEC Key: {dec} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                f=open('WINNER.txt','a')
                f.write('===========================================================================\n')
                f.write(f"DEC Key: {dec} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                f.write('===========================================================================\n')
                f.close()    
        except ValueError:
            pass