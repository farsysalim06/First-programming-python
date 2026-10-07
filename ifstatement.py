maths = int(input("maths marks: "))
english = int(input("english marks: "))

average = (maths + english) / 2

if average >= 80:
    print(f"average: {average}% - Grade A: Excellent work!")
elif average >= 75:
    print(f"average: {average}% - Grade B: very good work!")  
elif average >= 70:
    print(f"average: {average}% - Grade C: good work!")
else:
    print(f"average: {average}% - Grade D: Keep practicing.")    

    