# Get text to encode
# Get key for caesar cipher
# encode text using caesar cipher with key
# Decode encoded text

text = 'attack at dawn'
caesar_key = 2

abc = 'abcdefghijklmnopqrstuvwxyz'
encoded_abc = abc[caesar_key:] + abc[:caesar_key]

encode_dict = dict(zip(abc, encoded_abc))

# encoded_text = []
# for ch in text:
#     encoded_text.append(encode_dict.get(ch, ' ))
# print(''.join(encoded_text))

encoded_text = ''.join([encode_dict[letter] if letter in encode_dict else letter for letter in text])
print(encoded_text)

decode_dict = dict(zip(encoded_abc, abc))
decoded_text = ''.join([decode_dict[letter] if letter in decode_dict else letter for letter in encoded_text])
print(decoded_text)
