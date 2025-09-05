# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    #acceleration due to gravity (m/s^2) 
    g= 9.8
    h= h0 - 0.5 * g * (t ** 2)
    # Round up to one decimal point
    round(max(height, 0), 1)
    h0= float(input("Enter initial height:"))
    t= float(input("Enter time: "))
    print("Height of the ball:", calculate_height(h0, t))

  

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
