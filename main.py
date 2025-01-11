

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        splitted = file_contents.split()
        legth = len(splitted)
    return legth



def count_characters():
    with open("books/frankenstein.txt") as f:
        characters = {}
        file_contents = f.read()
        lower_case = file_contents.lower()
        for item in lower_case:
            if item not in characters:
                characters[item] = 1
            else:
                characters[item] += 1
        return characters

def format_dict(f):
    new_dict = {}
    for i in f:
        if i.isalpha() == True:
            new_dict[i] = f[i]
    return new_dict


#def sorted_dict(x):
    ls = []
    for item in x:
        ls.append({item : x[item]})
    sorted_dictionary = ls.sort(reverse = True, key = lambda v,: x[v])
    return sorted_dictionary

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{count_words()} was found in the document')
    f = count_characters()
    print(format_dict(f))
    n_d = format_dict(f)
    for item in n_d:
        print(f'The {item} character was found {n_d[item]} times')

    print("--- End report ---")
main()