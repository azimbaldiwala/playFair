
key = 'playfair' # key for encryption.
plain_text = "hello"

def generate_table(key_):
    alpahbets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    table = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
    r_count = 0 
    c_count = 0 

    def remove_duplicates(key):
        got_ = []
        for i in key:
            if i not in got_:
                got_.append(i)

        got_str = ''
        for i in range(len(got_)):
            got_str += got_[i]

        return got_str 

    key = remove_duplicates(key_)
    index_count = 0 
    while True:
        if index_count == len(key):
            break 

        if r_count < 5:
            if key[index_count] == 'i':
               table[c_count][r_count] = 'i/j' 
            else:
                table[c_count][r_count] = key[index_count]
            r_count += 1
            index_count += 1 
        else: 
            r_count = 0 
            c_count += 1 
    i = 0 
    while c_count < 5:
        if r_count < 5:
            if alpahbets[i] == 'i' and alpahbets[i] not in key:
                table[c_count][r_count] = 'i/j'
                r_count += 1 
                i += 2 

            if alpahbets[i] not in key and alpahbets[i] != 'j': 
                table[c_count][r_count] = alpahbets[i]
                r_count += 1 
            i += 1 
        else:
            r_count = 0 
            c_count += 1 
    return table 


def print_table(table):
    print("***TABLE GENERATED BASED TO KEY***")
    print("--------------------")
    for i in range(0, 5):
        for j in range(0, 5):
            print(table[i][j], end=' | ')
        print()
        print("--------------------")


def make_pairs(plain_text):
    
    def set_even_duplicate(plain_text):
        new_plain_text = ''
        for i in range(len(plain_text)):
            if i + 1  < len(plain_text):

                if i % 2 == 0 and plain_text[i] == plain_text[i + 1]:
                    new_plain_text += plain_text[i] + 'x'
                else: 
                    new_plain_text += plain_text[i]
            else: 
                new_plain_text += plain_text[i]
        return new_plain_text
    
    plain_text = set_even_duplicate(plain_text)
    def set_pairs(plain_text):
        pairs = []
        if len(plain_text) % 2 != 0:
            plain_text += 'x'
        
        index_ = 0 
        while index_ < len(plain_text) : 
           if index_ % 2 == 0:
               pairs.append(f'{plain_text[index_]}{plain_text[index_ + 1]}')
           index_ += 1 

    pairs = set_pairs(plain_text)
    return pairs 

print(make_pairs('hello')) 

