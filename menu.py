menu = {}
menu['1'] = "Option 1." 
menu['2'] = "Option 2."
menu['3'] = "Option 3."
menu['4'] = "Exit"
while True: 
    options=menu.keys()
    # options.sort()
    for num in options:
      print(num, menu[num])
    selection = input("Please Select: ") 
    if selection == '1': 
      print("This is option 1.") 
    elif selection == '2': 
      print("This is option 2.")
    elif selection == '3':
      print("This is option 3.") 
    elif selection == '4': 
      break
    else: 
      print("Unknown Option Selected!")