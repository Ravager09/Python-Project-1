

print("Hello")
def sum_of_numbers_upto_n(num):
    output = 0
    for i in range(1, num+1):
        output += i

    return output


if __name__ == "__main__":
        for i in range(1,11):
            print(f"sum_of_numbers_upto {i} = {sum_of_numbers_upto_n(i)}")

def product_of_numbers_upto_n(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    return product

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"product_of_numbers_upto_n = {product_of_numbers_upto_n(i)}")




def factors_of_number(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    for i in range(1, 101):
        print(f"Factors of {i} = {factors_of_number(i)}")



