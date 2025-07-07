import pyfiglet


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GREY = "\033[90m"
RESET = "\033[0m"

def style_line(text):
    styled = ""
    for ch in text:
        if ch == "#":
            styled += MAGENTA + ch
        elif ch == "-":
            styled += GREEN + ch
        else:
            styled += YELLOW + ch
        styled += RESET
        return styled


def main():
    print("\n" * 2)
    text = pyfiglet.print_figlet(text = "Registration", colors = "YELLOW", width = 100)
    print("\n" * 2)
D = main()
def display_registration():
    print("\n" * 2)
    print("Welocme and Thank you for registering with ARYA-MOTO!")
    print(style_line("#" * 100))
    print(f"{YELLOW}Name: {NAME}")
    print(f"Age: {AGE}")
    print(f"Email: {EMAIL}")
    print(f"Phone: {PHONE}")
    print(f"Address: {ADDRESS}{RESET}")
    print(style_line("#" * 100))
    print("\n")

NAME = input("Enter your name:")
AGE = input("Enter your age: ")
EMAIL = input("Enter your email: ")
PHONE = input("Enter your phone number: ")
ADDRESS = input("Enter your address: ")

A = display_registration()

def menu_box(text):
    screen_width = 128  
    RED = "\033[91m"
    RESET = "\033[0m"

    styled_text = ""  
    for ch in text:
        if ch in "12345":  
            styled_text += RED + ch + RESET  
        else:
            styled_text += ch  
    return styled_text  

def main():
    print(menu_box("[1]" + " Register a customer"))
    print(menu_box("[2]" + " Add a vehicle"))
    print(menu_box("[3]" + " Log Service Visit "))
    print(menu_box("[4]" + " View All Services Records"))
    print(menu_box("[5]" + " Exit"))



    opt = input(("Enter your choice: "))
    if opt == "1":
        print("You have chosen to register a customer.")
        import register
        register.main()
    elif opt == "2":
        print("You have chosen to add a vehicle.")
        import add_vehicle
        add_vehicle.main()
    elif opt == "3":
        print("You have chosen to log a service visit.")
        import log_service
        log_service.main()
    elif opt == "4":
        print("You have chosen to view all service records.")
        import view_services
        view_services.main()
    elif opt == "5":
        print("\n")
        print("Exiting the program. Thank you for using ARYA-MOTO!")
        print("\n")
        text = pyfiglet.print_figlet(text = "THANK  YOU", colors = "BLUE", width = 100)

    else:
        print("Invalid option. Please try again.")
        main()

Choose = main()