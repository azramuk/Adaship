class TextColours:
  RESET = '\x1b[0m'
  BOLD = '\x1b[1m'
  ITALIC = '\x1b[3m'
  UNDERLINE = '\x1b[4m'

  BLACK = '\x1b[30m'
  RED = '\x1b[31m'
  GREEN = '\x1b[32m'
  YELLOW = '\x1b[33m'
  BLUE = '\x1b[34m'
  BRIGHT_RED = '\x1b[91m'
  WHITE = '\x1b[37m'

  BG_RED = '\x1b[41m'
  BG_GREEN = '\x1b[42m'
  BG_BLUE = '\x1b[44m'

print(f"{TextColours.RED}Red")
print(f"{TextColours.BRIGHT_RED}bRIGHT Red")
# print(f"{bcolors.HEADER}Warning: No active frommets remain. Continue?{bcolors.HEADER}")
# print(f"{bcolors.OKBLUE}Warning: No active frommets remain. Continue?{bcolors.OKBLUE}")
# print(f"{bcolors.OKCYAN}Warning: No active frommets remain. Continue?{bcolors.OKCYAN}")
# print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.OKGREEN}")
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.WARNING}")
# print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.FAIL}")
# print(f"{bcolors.BOLD}Warning: No active frommets remain. Continue?{bcolors.BOLD}")
# print(f"{bcolors.UNDERLINE}Warning: No active frommets remain. Continue?{bcolors.UNDERLINE}")
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?")


colors = {
  'reset': '\x1b[0m',
  'bold': '\x1b[1m',
  'italic': '\x1b[3m',
  'underline': '\x1b[4m',
  'inverse': '\x1b[7m',

  'black': '\x1b[30m',
  'red': '\x1b[31m',
  'green': '\x1b[32m',
  'yellow': '\x1b[33m',
  'blue': '\x1b[34m',
  'magenta': '\x1b[35m',
  'cyan': '\x1b[36m',
  'white': '\x1b[37m',
  'gray': '\x1b[90m',
  'bright_red': '\x1b[91m',
  'bright_green': '\x1b[92m',
  'bright_yellow': '\x1b[93m',
  'bright_blue': '\x1b[94m',
  'bright_magenta': '\x1b[95m',
  'bright_cyan': '\x1b[96m',
  'bright_white': '\x1b[97m',

  'bg_black': '\x1b[40m',
  'bg_red': '\x1b[41m',
  'bg_green': '\x1b[42m',
  'bg_yellow': '\x1b[43m',
  'bg_blue': '\x1b[44m',
  'bg_magenta': '\x1b[45m',
  'bg_cyan': '\x1b[46m',
  'bg_white': '\x1b[47m',
  'bg_gray': '\x1b[100m',
  'bg_bright_red': '\x1b[101m',
  'bg_bright_green': '\x1b[102m',
  'bg_bright_yellow': '\x1b[103m',
  'bg_bright_blue': '\x1b[104m',
  'bg_bright_magenta': '\x1b[105m',
  'bg_bright_cyan': '\x1b[106m',
  'bg_bright_white': '\x1b[107m'
}

print(f'{colors["red"]}Red Text{colors["reset"]} {colors["bg_blue"]}text with blue background{colors["reset"]} normal text')

input()



from colorama import Fore, Back, Style

print(Back.RED + Fore.WHITE + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

class TextColours:
  RESET = '\x1b[0m'
  BOLD = '\x1b[1m'
  ITALIC = '\x1b[3m'
  UNDERLINE = '\x1b[4m'

  BLACK = '\x1b[30m'
  RED = '\x1b[31m'
  GREEN = '\x1b[32m'
  YELLOW = '\x1b[33m'
  BLUE = '\x1b[34m'
  BRIGHT_RED = '\x1b[91m'
  WHITE = '\x1b[37m'

  BG_RED = '\x1b[41m'
  BG_GREEN = '\x1b[42m'
  BG_BLUE = '\x1b[44m'

# print(f"{TextColours.WHITE}{TextColours.BG_RED}Red")
# print(f"{TextColours.BRIGHT_RED}bRIGHT Red")
print("\033[31;46mMy text\033[m")
input()