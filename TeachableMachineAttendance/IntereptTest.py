import keyboard
import time


def main_processing():
    loopy = True
    try:
        while loopy:
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print ("keyboard pressed")
                loopy = False
            print("loopy")
            time.sleep(1)
    except KeyboardInterrupt:
        print("")
        print("Attendance has been completed")

run_loop = True;

while run_loop:
    print("")
    print("Main menu Attendance Taker")
    print(" 1 - Take Attendance")
    print(" 2 - Print Absent List")
    print(" 3 - End Attendance App")
    menu_choice=int(input("Menu : "))
    if (menu_choice == 1):
        main_processing()
    elif (menu_choice == 2):
        print("attendance")
    elif (menu_choice == 3):
        run_loop = False
    else:
         print("Not a valid menu item")


print("")
print("Attendance App Exited")