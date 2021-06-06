alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

tr = "yes"
def encrypt(txt, shift_no):
  new = ""
  for i in txt :
    pos = alphabet.index(i)
    if pos + shift_no < (len(alphabet)-1) :
      new_pos = pos + shift_no
    else :
      new_pos = -(shift_no-1)
    new += alphabet[new_pos]
  print(f"Encoded Word : {new}")
def decrypt(txt, shift_no):
  new = ""
  for i in txt :
    pos = alphabet.index(i)
    new_pos = pos - shift_no
    new += alphabet[new_pos]
  print(f"Decoded Word : {new}")
while tr == "yes" :
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode" :
    encrypt(txt = text,shift_no =  shift)
  elif direction == "decode" :
    decrypt(txt = text, shift_no = shift)
  tr =input("Type yes to continue Or NO to Close The Program: ") 
