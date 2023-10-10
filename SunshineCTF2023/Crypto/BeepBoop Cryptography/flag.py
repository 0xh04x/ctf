import codecs 

def convert_to_binary(input_string):
    output_string = input_string.replace("beep", "0").replace("boop", "1")
    return output_string
with open("BeepBoop", "r") as file:
    input_string = file.read().replace(" ", "").replace("\t", "").replace("\n", "")

def binary_to_text(binary):
    # Split the binary string into 8-bit chunks
    binary_chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    
    # Convert each 8-bit chunk to a decimal value and then to a character
    text = ''.join([chr(int(chunk, 2)) for chunk in binary_chunks])
    
    return text


input_string = convert_to_binary(input_string)
rot = binary_to_text(input_string)
flag = codecs.decode(rot, 'rot13')
print(flag)

