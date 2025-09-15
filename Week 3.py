# Age = 25
# print(Age)

Welcome_message = """
Hello
Goodbye
"""
print(Welcome_message)


"""Professor Harding is running a half marathon - she ran 10 miles in 1 hr 18 min with a pace of about 7:42
For the half (13.2), what is her projected finish time. hr:min:sec
"""
minutes = 7
seconds = 42
pace = minutes*60 +42

distance = 13.2

Timetotalsec = distance* pace
print(Timetotalsec)


hr = int(Timetotalsec//3600)

min = int(Timetotalsec % 3600 // 60)

sec = int(Timetotalsec % 60)

print("Project Finish Time: " + str(hr) + ":" + str(min) + ":" + str(sec))


#art

awesome = """
    ___/______\_____
   |  ___________  __\
     O           O 


"""