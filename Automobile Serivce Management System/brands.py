import pyfiglet

text = pyfiglet.print_figlet(text = "BMW", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "AUDI", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "LOCKHEED MARTIN", colors = "black", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "MERCEDIES", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "TOYOTA", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "VOLVO", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "FORD", colors = "white", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "NISSAN", colors = "BLUE", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "PORSCHE", colors = "RED", width = 100)
print("\n" * 2)
text = pyfiglet.print_figlet(text = "GENERAL DYNAMICS", colors = "RED", width = 100)
print("\n", "\a" * 2)

# selection 

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
    print(menu_box("[1]" + " BMW"))
    print(menu_box("[2]" + " AUDI"))
    print(menu_box("[3]" + " LOCKHEED MARTIN "))
    print(menu_box("[4]" + " MERCEDIES"))
    print(menu_box("[5]" + " TOYOTA"))
    print(menu_box("[6]" + " VOLVO"))
    print(menu_box("[7]" + " FORD"))
    print(menu_box("[8]" + " NISSAN"))
    print(menu_box("[9]" + " PORSCHE"))
    print(menu_box("[10]" + " GENERAL DYNAMICS"))
    print("\n" * 2)
    print("Please select a brand by entering the corresponding number (1-10):")
    print("\n" * 2)

    opt = input(("Enter your choice: "))
    if opt == "1":
        print("BMW .")
        import add_vehicle
        add_vehicle.main()
    elif opt == "2":
        print("You have chosen to add a vehicle.")
        import add_vehicle
        add_vehicle.main()
    elif opt == "3":
        print("You have chosen to log a service visit.")
        import add_vehicle
        add_vehicle.main()
    elif opt == "4":
        print("MERCEDIES Vehical service ")
        import add_vehicle
        add_vehicle.main()
    elif opt == "5":
        print("Exiting the program. Thank you for using ARYA-MOTO!")
        text = pyfiglet.print_figlet(text = "THANK  YOU", colors = "BLUE", width = 100)

    else:
        print("Invalid option. Please try again.")
        main()


"""//                                   .:;it1i;:,,..
//                                .:i1tfffLLLf1i;,,,.
//                              .:;;i1tffLfLLCLti:,,,,.
//                            .,,,:iLLLLLffffftti;:,,,,.
//                            :,,,;11i;;i11ii:,,,,,,,,,,,
//                           ,:..,:;,.,,,:;;::,...,,:,,.,.
//                           ;,..,,,:tf1;;;::::::::;;:,..,
//                           ,....,;fLLCCCCLt111tt1;;;,,.,
//                           ....,i1ttffLCCCLfffft1;;::,.,
//                           ....,i11ttfLLLLfffftt1;;:::.,
//                           ::..,;tt1tffLCLLLffffti::::,,
//                           ;i,.:i1ttt1ttffLLfLL1:,,,,,:.
//             .1i:      .....11:;11i;;;::,:;1tt;,,::,,::
//             ;0Ct1:..,Lif1,:ifLf11ii11ii;:;ift::;;;;;;:
//              :t1ti::,:,::,,,iLfLftt1t1ttfCLCC;i1ttf1i:
//               ;11ii:;ii1;f0Ci11fiifLttGGCLLLG1;;i11i;,
//               1Lt1111i...;t1::::,,iLftf1itttf1:::::::.
//             .iC0GGG00C:...  :1;Gi,,iii;itti;;:::,:;;:
//             tftft1iii;:,:;1tfC;:;:;1t1tttttft1;::;::.
//             .1fti;i1ttfLLCG00CffCt,:;;i1ffft1ii;;,,,
//             .LGCffffffffttffftti:,..,,,:i1tfft1;,;;..
//            .;L1tftt1iii111iii:.......,i:,,::::,,:i;...
//           ..Lt:1fLfft11it1,;: ........;t,........ .......
//          .,.G1,i;;;i11ii:.,,,...........,...... ...... ..,..
//         ,,..GG,;;;::;:;i..,:,................,::,..............
//        ,....i@1,;111;it, .,::..............;fLLtf1,...............
//       ,..... t@;:1iiGG, ...:: .............,f00GGC; ................
//      ,....... L8:.18G, ...it1,...............t880G1..................
//     ,..........8L1@C.,;iiitt1iiii:........... t808f ..................
//    ............,:;i..,,::,:,,,,................f08t ...................
//    ,...........    ...  ........................fG; ...............  .,
//   ..............................................,i.................;, .,
//   ,................................................................Lt...,
//  ,............................................................... ;i:...,,
// .,.................................................................  ....,,
// ,.........................................................................,.
// ,..........................................................................,
// ...........................................................................,.
//   ..........................................................................,
//       ......,. ..............................................................,
//              ,................................................................,
//               ,...............................................................,.
//                , ..............................................................,
"""