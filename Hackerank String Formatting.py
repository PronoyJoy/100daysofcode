
def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        decimal = str(i).rjust(w," ")
        octal = oct(i)[2:].rjust(w," ")
        hexadecimal = hex(i)[2:].rjust(w," ")
        binary = bin(i)[2:].rjust(w," ")

        print(f'{decimal} {octal} {hexadecimal.upper()} {binary}')
        

   


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)