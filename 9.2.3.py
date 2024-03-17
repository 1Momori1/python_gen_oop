'''
Класс CaesarCipher
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].
'''


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, text,shift = 1):
        shift = self.shift*shift
        encoded_text = ''
        eng = range(ord('a'), ord('z') + 1)
        ENG = range(ord('A'), ord('Z') + 1)
        for char in text:
            if char.isalpha() and (ord(char) in eng or ord(char) in ENG):
                if char.isupper():
                    char_index = ord(char) - ord('A')
                    encoded_char_index = (char_index + shift) % 26
                    encoded_char = chr(encoded_char_index + ord('A'))
                else:
                    char_index = ord(char) - ord('a')
                    encoded_char_index = (char_index + shift) % 26
                    encoded_char = chr(encoded_char_index + ord('a'))
            else:
                encoded_char = char
            encoded_text += encoded_char
        return encoded_text

    def decode(self, text):
        return self.encode(text,-1)
        
# INPUT DATA:

# TEST_1:
cipher = CaesarCipher(10)

print(cipher.encode('Beegeek'))
print(cipher.decode('Gjjljjp'))

# TEST_2:
cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))

# TEST_3:
cipher = CaesarCipher(10)

words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
         'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
         'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
         'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
         'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
         'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
         'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
         'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
         'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_4:
cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_5:
cipher = CaesarCipher(15)

words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏', 'size🤥',
         'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_6:
cipher = CaesarCipher(1)
print(cipher.encode('ZzzZzz'))
print(cipher.decode('AaaAaa'))