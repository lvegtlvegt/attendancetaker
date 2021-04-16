class Attendance:
    studentList = {}
    presentList = {}
    className = ""

    def __init__(self, student_fName, className ):
        self.className = className
        self.studentList = set()
        self.presentList = set()
        self.load_students(student_fName)


    def load_students(self):
        #testing proposes only
        self.studentList.add("Jack")
        self.studentList.add("Jill")
        self.studentList.add("Joan")
        self.studentList.add("Joan")
        self.studentList.add("Joan")

    def load_students(self, studentFName):
        try:
            with open(studentFName, "r") as studentFile:
                for studentName in studentFile:
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



