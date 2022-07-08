import string
import re, trotter
from tqdm import tqdm
import secp256k1 as ice
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

INPUTNEEDEDHEX = '''[yellow]

  ,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
  |esc| [red]1[/red] | [red]2[/red] | [red]3[/red] | [red]4[/red] | [red]5[/red] | [red]6[/red] | [red]7[/red] | [red]8[/red] | [red]9[/red] | [red]0[/red] | + | ' | <-    |
  |---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
  | ->| | Q | W | [red]E[/red] | R | T | Y | U | I | O | P | ] | ^ |     |
  |-----',--',--',--',--',--',--',--',--',--',--',--',--'|    |
  | Caps | [red]A[/red] | S | [red]D[/red] | [red]F[/red] | G | H | J | K | L | \ | [ | * |    |
  |----,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'----|
  |    | < | Z | X | [red]C[/red] | V | [red]B[/red] | N | M | , | . | - |          |
  |----'-,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
  | ctrl |🪟| alt |  **  MAX 10 MISSING  **  |altgr |  | ctrl |
  '------'  '-----'--------------------------'------'  '------'    

[/yellow]'''
print(Mizogg)

print(INPUTNEEDEDHEX)
print ('[green]HEX Recovery Tool **  MAX 10 MISSING  ** [/green]')
HEX_key_FIND = str(input('Enter HEX with Missing Characters  as * : (Example = 0000000000000000000****00000000000000000000000000000000000****** ) \n(Example = 8ea6007390bee9daa120ac8aa5840230ed16f77c8611**d*ae5254********02 )\n Enter Here =  '))
#0000000000000000000200000000000000000000000000000000000000000001
def complete_key(HEX_key_FIND_string, missing_letters):
    for letter in missing_letters:
        HEX_key_FIND_string = HEX_key_FIND_string.replace('*', letter, 1)
    #print(f"HEX_key_FIND_string: {HEX_key_FIND_string}", end='\r') # Showing more info but slower
    return HEX_key_FIND_string

if __name__ == '__main__':
    missing_length = HEX_key_FIND.count('*')
    print(f"Looking for {missing_length} characters in {HEX_key_FIND}")
    allowed_characters = '0123456789abcdef'
    master_list = trotter.Amalgams(missing_length, allowed_characters)
    print(master_list)
    print(len(master_list))
    for i in tqdm(range(len(master_list))):
        test_key = complete_key(HEX_key_FIND, master_list[i])
        try:
            dec = int(test_key[0:64],16)
            uaddr = ice.privatekey_to_address(0, False, dec)
            caddr = ice.privatekey_to_address(0, True, dec)
            if uaddr in add or caddr in add:
                wifc = ice.btc_pvk_to_wif(test_key)
                wifu = ice.btc_pvk_to_wif(test_key, False) 
                print ('WINNER WINNER Check WINNER.txt')
                print(f"DEC Key: {dec} \n HEX Key: {test_key} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                f=open('WINNER.txt','a')
                f.write('===========================================================================\n')
                f.write(f"DEC Key: {dec} \n HEX Key: {test_key} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                f.write('===========================================================================\n')
                f.close()    
        except ValueError:
            pass