def solution(s):
    arr = list(s)
    output = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    braille = ['100000', '110000', '100100','100110','100010','110100','110110','110010','010100','010110','101000','111000','101100','101110','101010','111100','111110','111010','011100','011110',"101001","111001","010111","101101","101111","101011"]
    for letter in arr:
        if letter == ' ':
            output += "000000"
        else:
            pos = alphabet.index(letter.lower())
            toAdd = ""
            if letter.lower() != letter:
                toAdd = "000001"
            output += toAdd + braille[pos]
    return output