class Attendance:
    studentList = {}
    presentList = {}
    className = ""

    def __init__(self, student_fName, className):
        self.className = className
        self.studentList = set()
        self.presentList = set()
        if (student_fName == ""):
            self.load_test_students()
        else:
            self.load_students(student_fName)


    def load_test_students(self):
        #testing proposes only
        self.studentList.add("Jack")
        self.studentList.add("Jill")
        self.studentList.add("Joan")
        self.studentList.add("Jean")
        self.studentList.add("Joe")

    def load_students(self, studentFName):
        try:
            with open(studentFName, "r") as studentFile:
                for studentName in studentFile:
                    studentName = studentName.rstrip('\r\n')  # strip out all tailing whitespace
                    self.studentList.add(studentName)
                studentFile.close()
        except IOError:
            print ("ERROR: file - %s not found!" % studentFName)

    def getStudentList(self):
        return(self.studentList)

    def studentPresent(self, studentName):
        self.presentList.add(studentName)

    def getAbsentList(self):
        absentList = self.studentList.difference(self.presentList)
        return absentList

    def printAbsentList(self):
        print("List of absent students for %s \n" % self.className)
        for studentName in self.getAbsentList():
            print(studentName)



