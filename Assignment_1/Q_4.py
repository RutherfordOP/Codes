def highestoccuring(str):
    char_count = {}

    for i in str:
        i = i.lower()
        if i.isalpha():
            if not char_count.get(i):
                char_count[i] = 1
            else:
                char_count[i] += 1

    max_char = None
    max_count = 0
    for j in char_count.keys():
        if(char_count.get(j) > max_count):
            max_char = j
            max_count = char_count.get(j)

    return (max_char, max_count)

if __name__ == "__main__":
    result = highestoccuring("jfkjdfkshdhfwueufuehiuaehfas")
    print(f"{result[0]}: {result[1]}")