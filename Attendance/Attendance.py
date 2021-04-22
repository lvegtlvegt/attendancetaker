import statistics


class Attendance:
    studentList = []
    studentCount = []
    presentList = []
    absentList = []
    className = ""

    def __init__(self, student_fName, className):
        self.className = className
        if student_fName == "":
            self.load_test_students()
        else:
            self.loadStudents(student_fName)

    # Testing and utility methods
    def load_test_students(self):
        # testing proposes only
        self.studentSet.add("Jack")
        self.studentSet.add("Jill")
        self.studentSet.add("Joan")
        self.studentSet.add("Jean")
        self.studentSet.add("Joe")

    def standardDev(self):
        # mean = sum(self.studentCount) / len(self.studentCount)
        # variance = sum([((x-mean)**2) for x in self.studentCount]) / len(self.studentCount)
        # res = variance ** 0.5

        res = statistics.pstdev(self.studentCount)
        return res

    def standardDevDegree(self, degree):
        return self.standardDev() * degree

    # Load Student names from a file into the student list and count list
    def loadStudents(self, studentFName):
        self.studentList.clear()
        self.studentCount.clear()
        try:
            with open(studentFName, "r") as studentFile:
                for studentName in studentFile:
                    studentName = studentName.rstrip('\r\n')  # strip out all tailing whitespace
                    self.studentList.append(studentName)
                    self.studentCount.append(0)
                studentFile.close()
        except IOError:
            print("ERROR: file - %s not found!" % studentFName)

    # Setter and getters
    def setStudentList(self, studentFName):
        self.studentList.clear()
        # self.loadStudents(studentFName)

    def setClassName(self, className):
        self.className = className

    def getStudentList(self):
        return self.studentList

    # Attendance methods
    def studentPresent(self, studentName):
        try:
            foundIdx = self.studentList.index(studentName)
            self.studentCount[foundIdx] += 1
            # self.printStudentInfo()
        except (ValueError, IndexError):
            print("ERROR - %s not found" % studentName)

    # Separate the students into present and absent list based on number of images counted
    def getAbsentList(self):
        threshold = self.standardDevDegree(1)
        for i in range(len(self.studentList)):
            # print("Student : %s, count : %i" % (self.studentList[i], self.studentCount[i]))
            if self.studentCount[i] > threshold:
                self.presentList.append(self.studentList[i])
            else:
                self.absentList.append(self.studentList[i])
        return

    # Reporting methods
    def printStudentInfo(self):
        for i in range(len(self.studentList)):
            print("%s, %i" % (self.studentList[i], self.studentCount[i]))

    def printAbsentList(self):
        self.getAbsentList()
        sortStudentList = sorted(self.presentList)
        print("")
        print("%i Students PRESENT in %s" % (len(sortStudentList), self.className))
        for studentName in sortStudentList:
            print("  %s" % studentName)
        print("")
        sortAbsentList = sorted(self.absentList)
        print("%i Students ABSENT in %s" % (len(sortAbsentList), self.className))
        for studentName in sortAbsentList:
            print("  %s" % studentName)
