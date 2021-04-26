# This is based on file test.py and IntereptTest.py


from TeachableMachinePython import TeachableMachinePython
from Attendance.Attendance import Attendance
import keyboard

attendance = Attendance("..\Attendance\webdesignstudents2.csv", "Web Design")


def main_processing():
    prediction_model = TeachableMachinePython("keras_model.h5", "labels.txt")
    loopy = True
    try:
        while loopy:
            prediction_model.main_processing_begin_loop()

            # print(prediction_model.get_predicted_label())
            attendance.studentPresent(prediction_model.get_predicted_label())

            loop_flag = prediction_model.main_check_to_end_loop()

            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                prediction_model.main_loop_stop()
                loopy = False

    except KeyboardInterrupt:
        prediction_model.main_loop_stop()

    print("")
    print("Attendance has been completed")


run_loop = True
while run_loop:
    print("")
    print("Main menu Attendance Taker")
    print(" 1 - Take Attendance")
    print(" 2 - Print Absent List")
    print(" 3 - End Attendance App")
    menu_choice = int(input("Menu : "))

    if menu_choice == 1:
        main_processing()

    elif menu_choice == 2:
        attendance.printAbsentList()

    elif menu_choice == 3:
        run_loop = False

    else:
        print("Not a valid menu item")

print("")
print("Attendance App Exited")
