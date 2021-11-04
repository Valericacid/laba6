def rot(num):
    num_list = list(str(num))
    for index, value in enumerate(num_list):
        if value == '6':
            num_list[index] = '9'
            break
    return int("".join([str(l) for l in num_list]))

if __name__ == "__main__":
    x = 9666
    print(rot(x))