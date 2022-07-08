import string
import re, trotter
from tqdm import tqdm
from hdwallet import HDWallet
from hdwallet.symbols import BTC
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
addr = str(input('Enter Your Bitcoin Address Here : (Example = 16UX8hrqG2h5idgaqA1zzPDGtmXTkE8deR ) '))

print(INPUTNEEDEDWIF)
print ('[green]WIF Recovery Tool Edit Line 66 For More Information[/green]')
WIF_key_FIND = str(input('Enter WIF with Missing Characters  as * : (Example = KwDiBf**QgGcZwzunkKCSmeavWjCmdZ1CJSDfh*2pHWYV4nLoEoj ) '))

def complete_key(WIF_key_FIND_string, missing_letters):
    for letter in missing_letters:
        WIF_key_FIND_string = WIF_key_FIND_string.replace('*', letter, 1)
    # print(f"WIF_key_FIND_string: {WIF_key_FIND_string}", end='\r') # Showing more info but slower
    return WIF_key_FIND_string

def btc_address_from_private_key(my_secret, secret_WIF='WIF'):
    assert secret_WIF in ['WIF']
    hdwallet = HDWallet(symbol=BTC)
    match secret_WIF:
        case 'WIF':
            hdwallet.from_wif(wif=my_secret)

    return hdwallet.p2pkh_address()

if __name__ == '__main__':
    missing_length = WIF_key_FIND.count('*')
    print(f"Looking for {missing_length} characters in {WIF_key_FIND}")
    allowed_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    master_list = trotter.Amalgams(missing_length, allowed_characters)
    print(master_list)
    print(len(master_list))
    for i in tqdm(range(len(master_list))):
        test_key = complete_key(WIF_key_FIND, master_list[i])
        try:
            address = btc_address_from_private_key(test_key, secret_WIF='WIF')
            print(address)
            print(f"key: {test_key} address: {address}")
            if address in addr:
                print ('WINNER WINNER Check WINNER.txt')
                f=open('WINNER.txt','a')
                f.write('===========================================================================\n')
                f.write(f"WIF Key: {test_key} \nBTC Address: {address}\n")
                f.write('===========================================================================\n')
                f.close()
        except ValueError:
            pass