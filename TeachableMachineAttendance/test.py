from TeachableMachinePython import TeachableMachinePython

my_test = TeachableMachinePython("keras_model.h5", "labels.txt")
#my_test.main_processing_loop()

loop_flag = True
while loop_flag:
    my_test.main_processing_begin_loop()

    print(my_test.get_predicted_label())

    loop_flag = my_test.main_check_to_end_loop()

my_test.main_loop_stop()
