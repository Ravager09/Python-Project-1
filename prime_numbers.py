

def is_prime(input_number):
    list_of_numbers_from_2_to_mainusome = list(range(2, input_number))
    for numer in list_of_numbers_from_2_to_mainusome:
        if input_number % numer == 0:
            return False
    return True




if __name__ == "__main__":
    print("This is a file for testing prime numbers")

    input_numbers = [2,3,4,5,6,7,8,9,10,11,12]
    for number in input_numbers:
        if is_prime(number):
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

