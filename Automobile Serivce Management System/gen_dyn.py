import pyfiglet


def main():
    text = pyfiglet.print_figlet(text = "Add  Vehicle", colors = "YELLOW", width = 100)
    print("\n" * 2)
    
    #BMW

print("Welcome to GENERAL DYNAMICS Moter LandSystem division")
print("\n" * 2)
text = pyfiglet.print_figlet(text = "Vehicle-class", colors = "BLUE", width = 100)
print("\n" * 2)
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

def main_():
    print(menu_box("[1]" + " ABRAMS MBT"))
    print(menu_box("[2]" + " Light Armored Vehicle"))
    print(menu_box("[3]" + " MRAP"))
    print(menu_box("[4]" + " Specialty Wheeled Vehicles"))
    opt = input(("Enter your choice: "))
    if opt == "1":
        print("ABRAMS MBT Maintenance.")
        def mod():
            print(menu_box("[1]" + " M1A1 Abrams"))
            print(menu_box("[2]" + " M1A2 Abrams"))
            option = input("Enter your choice: ")
            if option == "1":
                print("You have chosen M1A1 Abrams.")
            elif option == "2":
                print("You have chosen M1A2 Abrams.")
            else:
                print("Invalid option. Please try again.")
                mod()
        mod()
    elif opt == "2":
        print("\n")
        print("Light Armored Vehicles Maintenance.")
        def mod2():
            print(menu_box("[1]" + " LAV-II"))
            print(menu_box("[2]" + " LAV-III"))
            print(menu_box("[3]" + " LAV-6.0"))
            print(menu_box("[4]" + " LAV-700"))
            print(menu_box("[5]" + " Stryker Combat Vehicles"))
            option1 = input("Enter your choice: ")
            if option1 == "1":
                print("You have chosen LAV-II.")
            elif option1 == "2":
                print("You have chosen LAV-III.")
            elif option1 == "3":
                print("You have chosen LAV-6.0.")
            elif option1 == "4":
                print("You have chosen LAV-700.")
            elif option1 == "5":
                print("You have chosen Stryker Combat Vehicles.")
            else:
                print("Invalid option. Please try again.")
                mod2()
        mod2()
    elif opt == "3":
        print("MRAP Maintainence.")
        def mod3():
            print(menu_box("[1]" + " Cougar 4x4"))
            print(menu_box("[2]" + " Cougar 6x6"))
            print(menu_box("[3]" + " Cougar ISS"))
            print(menu_box("[4]" + " Buffalo"))
            print(menu_box("[5]" + " RG-31 MK5"))
            option2 = input("Enter your choice: ")
            if option2 == "1":
                print("You have chosen Cougar 4x4.")
            elif option2 == "2":
                print("You have chosen Cougar 6x6.")
            elif option2 == "3":
                print("You have chosen Couger ISS.")
            elif option2 == "4":
                print("you have chosen Buffalo.")
            elif option2 == "5":
                print("You have chosen RG-31 MK5.")
            else:
                print("Invalid option. Please try again.")
                mod3()
        mod3()
    elif opt == "4":
        print("\n")
        print("Specialty Wheeled Vehicles Maintenance.")
        def mod4():
            print(menu_box("[1]" + " Ocelot"))
            print(menu_box("[2]" + " PKSV"))
            option3 = input("Enter Your choice: ")
            if option3 == "1":
                print("You have chosen Ocelot.")
            elif option3 == "2":
                print("You have chosen PKSV.")
            else:
                print("Invalid option. please try again.")
                mod4()
        mod4()
main_()
