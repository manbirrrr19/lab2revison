def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmii = weight/(height*height)
    bmi=round(bmii,2)
    print("BMI =" + str(bmi))

    if bmi < 18.5:
        print("Under weight")
        value = -1
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
        value = 0
    elif bmi >25.0:
        print("Overweight")
        value = 1
    return value


calculate_bmi(weight=57, height=1.73)
