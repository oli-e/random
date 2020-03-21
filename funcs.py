import string


def is_mac_48_address(address):
    options =['A','B','C','D','E','F','1','2','3','4','5','6','7','8','9','0']
    filtered = list(filter(lambda x: x in options, address))
    a = [filtered[i]+filtered[i+1] for i in range(0,len(filtered)-1,2)]
    return '-'.join(a)==address and len(address)==17


def censor_this(text, forbidden_words):
    forbidden_words.extend([x.capitalize() for x in forbidden_words])
    forbidden_words.extend([x.upper() for x in forbidden_words])
    list = text.split()
    new_list = [i if i not in forbidden_words else "*" * len(i) for i in list]
    return ' '.join(new_list)


def reverse_alternate(string):
    list = string.split()
    list2 = []
    for i in range(0, len(list)):
        if i%2==0:
            list2.append(list[i])
        else:
            list2.append(''.join(reversed(list[i])))
    return " ".join(list2).strip()


def create_phone_number(arr):
    numbers = "".join(str(i) for i in arr)
    number = "("+numbers[0:3]+") "+numbers[3:6]+"-"+numbers[6:10]
    return number


low = string.ascii_lowercase
up = string.ascii_uppercase


def rot13(message):
    rot = []
    for char in message:
        if char in low:
            number = low.index(char) + 13
            if number >= len(low):
                number = number - len(low)
            rot.append(low[number])

        elif char in up:
            number = up.index(char) + 13
            if number >= len(up):
                number = number - len(up)
            rot.append(up[number])
        else:
            rot.append(char)
    return ''.join(rot)


def spin_words(sentence):
    new_sentence = []

    def reverse(s):
        str = ""
        for i in s:
            str = i + str
        return str

    for word in sentence.split():
        if len(word) <= 4:
            new_sentence.append(word)
        else:
            new_sentence.append(reverse(word))
    return " ".join(new_sentence)


def find_outlier(integers):
    def parity_check(n):
        a = []
        for i in n:
            if i % 2 == 0:
                a.append(i)
                if len(a) > 1: break;
        if (len(a)) > 1:
            return True
        else:
            return False

    if parity_check(integers) == True:
        for i in integers:
            if i % 2 != 0: return i
    else:
        for i in integers:
            if i % 2 == 0: return i


def polybius(text):
    def encode(char):
        if char == ' ': return ' '
        rows = ['ABCDE', 'FGHIJK', 'LMNOP', 'QRSTU', 'VWXYZ']
        columns = ['AFLQV','BGMRW','CHNSX','DIJOTY','EKPUZ']
        def find(items, char):
            containing = (i for i, item in enumerate(items)
                          if char in item )
            return next(containing, None)
        row = find(rows, char)+1
        column = find(columns, char)+1
        return str(row)+str(column)
    return ''.join(map(encode, text))