name = input("What's your name? ").title()
def main(): 
    address()

def address():
    match name:
        case "Sangmesh"| "Sangmeshwar" | "Sangmeshwar Ramshetty":
            print("Hiii, ", name.strip())
        case _:
            print("hi, ",name.lower())
            

    
if __name__ == "__main__":
    main()