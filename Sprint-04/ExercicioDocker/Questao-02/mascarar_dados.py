import hashlib

while True:

    input_string = input("Digite uma palavra: ")

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    print(f"Hash SHA-1 da palavra '{input_string}': {sha1_hash}\n")