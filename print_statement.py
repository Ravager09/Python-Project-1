

print("Hello World")

myname = "ADARSH"

print(f"Hello {myname}! How are you?")


def hello_name(somename):
    print(f"Hello {somename}! This is a function")

def repeat_hello(someone, n_times):
    for i in range(n_times):
        print(f"Hello there {someone}! This is a print statement number: {i+1}")



if __name__ == "__main__":
    hello_name("class")
    hello_name("Adarsh")
    hello_name("Folks")

    repeat_hello(someone="Adarsh", n_times=6)






