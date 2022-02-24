MORSE_KEYS = {
  '.-': 'A',
  '-...': 'B',
  '-.-.': 'C',
  '-..': 'D',
  '.': 'E',
  '..-.': 'F',
  '--.': 'G',
  '....': 'H',
  '..' : 'I',
  '-.-': 'K',
  '.-..': 'L',
  '--': 'M',
  '-.': 'N',
  '---': 'O',
  '.--.': 'P',
  '--.-': 'Q',
  '.-.': 'R',
  '...': 'S',
  '-': 'T',
  '..-': 'U',
  '...-': 'V',
  '.--': 'W',
  '-..-': 'X',
  '-.--': 'Y',
  '--..': 'Z'
}

def convertCode(code):
  return MORSE_KEYS[code]


def decodeMessage(message):
  words = message.split(' ')
  decoded = ''
  for i in words:
    if '.' in i or '-' in i:
      decoded = decoded + convertCode(i)
    else:
      if not i.strip():
        decoded += ' '
      else:
        decoded += " " + i + " "
  print(decoded)

decodeMessage('.-   -... --- -..-   ..-. ..- .-.. .-..   --- ..-. / .-. ..- -... .. . ...')