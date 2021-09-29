#  You can experiment here, it won’t be checked
import argparse

parser = argparse.ArgumentParser(description="Decode messages")
parser.add_argument("file")
parser.add_argument("n")

args = parser.parse_args()


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


filename = args.file
offset = int(args.n)

opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
decode_caesar_cipher(encoded_text, offset)
opened_file.close()  # always close the files you've opened
