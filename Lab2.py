# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    pass  # Replace with your code
    h_01 = float(input("Enter intial height: "))
    time1 = float(input("Enter time: "))
    ht = h_01 - (0.5 * 9.8 * (time1 ** 2))
    print("Height of the ball at ", time1, "seconds = " + str(ht) + " meters" )
    print()
    h_02 = float(input("Enter initial height: "))
    time2 = float(input("Enter time: "))
    ht2 = h_02 - (0.5 * 9.8 * (time2 ** 2))
    print("Height of the ball at ", time2, "seconds = " + str(ht2) + " meters" )
    print()
    h_03 = float(input("Enter initial height: "))
    time3 = float(input("Enter time: "))
    ht3 = h_03 - (0.5 * 9.8 * (time3 ** 2))
    print("Height of the ball at ", time3, "seconds = " + str(ht3) + " meters")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
    speed=20
    time=float(input("Enter time (in seconds): "))
    distance = speed * time
    print("The car will travel " + str(distance) + " meters in " + str(time) + " seconds.")
    print()
    time=float(input("Enter time (in seconds): "))
    distance = speed * time
    print("The car will travel " + str(distance) + " meters in " + str(time) + " seconds.")
    print()
    time=float(input("Enter time (in seconds): "))
    distance = speed * time
    print("The car will travel " + str(distance) + " meters in " + str(time) + " seconds.")
    print()
