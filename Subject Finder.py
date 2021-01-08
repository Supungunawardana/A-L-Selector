# Enter Exam Number
ExamNo = input("Enter your Ordinary Level Exam Number: ")

# Enter Subject Passes
print("Enter your Ordinary Level Result")
Maths = int(input("Mathmatics : "))
Science = int(input("Science : "))
Sinhala = int(input("Sinhala : "))
English = int(input("English : "))
History = int(input("History : "))
Religion = int(input("Religion : "))
BucketI = int(input("Bucket I : "))
BucketII = int(input("Bucket II : "))
BucketIII = int(input("Bucket III : "))

# If you have C pass for Maths,Science and English. You can do A/L exam.
# As well as Science has B pass, you can do Bio and Maths has B pass, you can do Maths.
# You have two B passes for Science and Maths subject. You can do any stream for A/L exam.

if (Maths>=55) and (Science>=55) and (English>=55):
    print("You are eglible to do Advance Level Exam")
    if (Science>=65):
        print("and selected Bio stream")
    if (Maths>=65):
        print("and selected Maths stream")
    if (Science>=65) and (Maths>=65):
        print("So you can choose any stream for Advance Level Exam.")
else:
    print("Sorry. You have to do Ordinary Level Exam again")





input("Press Enter End Program")