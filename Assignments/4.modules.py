import my_programs as mp

menu = [
    "Buzz Number",
    "Magic Number",
    "Smith Number",
    "Perfect Cubes in a Range",
    "Sum of Factorials of Digits",
    "Median of a List",
    "Peterson Number",
    "Replace Consonants with #",
    "Sum of Alternate Elements in a List",
    "Trimorphic Number"
]

functions = [
    mp.buzz_number,
    mp.magic_number,
    mp.smith_number,
    mp.perfect_cubes_range,
    mp.sum_factorials_digits,
    mp.median_list,
    mp.peterson_number,
    mp.replace_consonants,
    mp.sum_alternate_elements,
    mp.trimorphic_number
]

while True:
    print("\n------ FUNCTION MENU ------")
    for i, name in enumerate(menu, 1):
        print(f"{i}. {name}")
    print("0. Exit")
    print("----------------------------")

    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Exiting program. Goodbye!")
        break
    elif 1 <= choice <= len(menu):
        print("\n" + "="*50)
        functions[choice-1]()
        print("="*50)
    else:
        print(f"Invalid choice. Please enter between 0-{len(menu)}.")