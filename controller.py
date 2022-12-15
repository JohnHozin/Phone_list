import modul_import as mi
import view as v
import modul_export as me

def button_click():
    choice = v.hello()
    phones = []
    if choice == "1":
        choice_2 = v.str_or_line()
        if choice_2 == "1":
            phones = mi.get_number()
        elif choice_2 == "2":
            mi.get_number_line_example()
            mi.get_number_line()
        print(phones)
        me.write_in_txt(phones)

    # elif choice == "2":
    #     fd
    # elif choice == "2":
    #     fd
    # else:
        print("Error!")
