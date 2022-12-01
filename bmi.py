def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("Bmi = " + str(bmi))
    if(bmi < 18.5):
        print("You are under weight")
    elif(bmi > 25.0):
        print("You are over weight")
    else:
        print("You are normal weight")


calculate_bmi(weight=64, height=1.77)
