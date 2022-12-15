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
            phones = mi.get_number_line()
        # print(phones)
        me.write_in_txt(phones)
        me.write_in_csv(phones)

    elif choice == "2":
        me.print_from_txt()
    # elif choice == "2":
    #     fd
    else:
        print("Error!")
