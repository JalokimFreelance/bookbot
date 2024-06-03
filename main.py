def count_words(string):
    return len(string.split())

def count_letters(string):
    dic = {}
    for s in string:
        s = s.lower()
        if not s.isalpha():
            continue
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return dic

def print_report(file):
    text = file.read()
    print(f"--- Begin report of {file.name} ---")
    print(f"{count_words(text)} words found in document")
    chars = count_letters(text)
    chars_list = []
    for char in chars:
        chars_list.append({"char": char, "num": chars[char]})
    chars_list.sort(reverse=True, key=lambda dict: dict["num"])
    for c in chars_list:
        print(f"The '{c["char"]}' character was found {c["num"]} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        print_report(f)
if __name__ == '__main__':
    main()
