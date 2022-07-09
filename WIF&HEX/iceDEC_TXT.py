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
print ('[green]DEC Recovery Tool ******************  MAX 18 MISSING  ****************** [/green]')
DEC_key_FIND = str(input('Enter DEC with Missing Characters  as * :\n (Example = ***52312848583266388373324160190187140051835877600158453279131187530910662657** ) \n (Example = 115792089237316195423570985008687907852837564279074904382605****************** ) \n (Example = 1157**0892373*6*95423570985***687907*52837***279074*0438260***3141518161494*** ) \n Enter Here =  '))
#1157**0892373*6*95423570985***687907*52837***279074*0438260***3141518161494*** 
maxN = 115792089237316195423570985008687907852837564279074904382605163141518161494336
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
    found = 0
    print(master_list)
    print(len(master_list))
    for i in tqdm(range(len(master_list))):
        test_key = complete_key(DEC_key_FIND, master_list[i])
        if int(test_key) < maxN:
            try:
                dec = int(test_key)
                HEX = "%064x" % dec
                uaddr = ice.privatekey_to_address(0, False, dec)
                caddr = ice.privatekey_to_address(0, True, dec)
                length = len(bin(dec))
                length -=2
                print(f"DEC: {dec}  bits {length} Found {found}", end='\r')
                if uaddr in add or caddr in add:
                    found += 1
                    wifc = ice.btc_pvk_to_wif(HEX)
                    wifu = ice.btc_pvk_to_wif(HEX, False) 
                    print(f"WINNER WINNER Check WINNER.txt \n DEC Key: {dec} bits {length} Found {found} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                    f=open('WINNER.txt','a')
                    f.write('===========================================================================\n')
                    f.write(f"DEC Key: {dec} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n")
                    f.write('===========================================================================\n')
                    f.close()    
            except ValueError:
                pass