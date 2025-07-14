class AttendanceTracker:
    def __init__(self):
        self.Student=set()
    def add_name(self,name):
        if name in self.Student:
            print("already in set")
        else:
            self.Student.add(name)
            print("added to set")
    def remove_name(self,name):
        if name in self.Student:
            self.Student.remove(name)
            print("Removed from attendance")
        else:
            print("Student not in attendance")
    def display_attendance(self):
        if not self.Student:
            print("No students present")
        else:
            for i in self.Student:
                print(i)
