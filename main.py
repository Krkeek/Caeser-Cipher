from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
  new_text = ""
  for letter in text:  
    if letter in alphabet:   
      if direction == "encode":
        new_position = alphabet.index(letter) + shift     
      elif direction == "decode":
        new_position = alphabet.index(letter) - shift
      new_text += alphabet[new_position]
    else:
      new_text += letter
  print(f"The {direction} of the text is {new_text}")      
                      
quit = False
while quit == False: 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction,text,shift)
    try_again = input("Do you want to try again? Yes or No?").lower()
    if try_again == "no":
      quit = True        
  else:
    print("Invalid input, try again.")
