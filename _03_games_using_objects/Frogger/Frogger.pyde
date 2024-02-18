
def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 800)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    global bg
    global frog
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    frog.resize(100, 100)
    bg.resize(800, 800)
    global frog_x, frog_y
    frog_x = 350
    frog_y = 700
    global car
    global car1
    global car2
    global car3
    car3 = Car(100, 200, 200, 1)
    car2 = Car(100, 400, 200, 3)
    car1 = Car(100, 600, 200, 5)

def draw(): 
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    global frog_x, frog_y
    image(frog, frog_x, frog_y)
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    global car
    car1.update()
    car1.draw()
    car2.update()
    car2.draw()
    car3.update()
    car3.draw()
    global frog_x
#write individual lines of if statements so that it doesn't check when it is greater than the car
    if intersection(car2):
        intersection = False
        print(frog_x)
        print(frog_y)
        print("car 2 y = " + str(car2.x))
        print("car 2 y = " + str(car2.y))
    if intersection(car1):
        frog_y = 700
        print(frog_x)
        print(frog_y)
        print("car 1 y = " + str(car1.x))
        print("car 1 y = " + str(car1.y))
    
    if intersection(car3):
        frog_y = 700
        print(frog_x)
        print(frog_y)
        print("car 3 y = " + str(car3.x))
        print("car 3 y = " + str(car3.y))
        
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.

def intersection(car):
    global frog_x, frog_y
    if frog_y + 100 > car.y:
        return False
    else:
        if frog_x == car.x + car.length and frog_y <= car.y + 50:
            return True
    

    # 9. Create more car objects of different lengths, speed, and size
    
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
def keyPressed():
    global frog_y
    if key == 'w':
        frog_y -= 50
    if key == 's':
        frog_y += 50
    
