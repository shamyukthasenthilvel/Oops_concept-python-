import attendancetracker

attend = attendancetracker.AttendanceTracker()
attend.display_attendance()
opt=int(input("want to add or remove(1/2)"))
if opt==1:
    n = int(input("enter how many names you want to add: "))
    for i in range(n):
        name=input("enter the name")
        attend.add_name(name)
else:
    name=input("enter the name to remove")
    attend.remove_name(name)