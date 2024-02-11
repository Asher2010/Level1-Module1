
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
    global car1
    global car2
    global car3
    global car4
    global car5
    car1 = Car(100, 600, 200, 1)
    car2 = Car(100, 200, 200, 2)

    car4 = Car(100, 400, 200, 3)

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
    car1.update()
    car1.draw()
    car2.update()
    car2.draw()
    car4.update()
    car4.draw()
    global frog_x
    if intersection(car1):
        frog_y = 700
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.

def intersection(car):
    global frog_x, frog_y
    if frog_x <= car.x + car.length and frog_y <= car.y + 20:
        return True

#if frog_x <= car2.x + car2.length and frog_y <= car2.y + 20:
    #frog_y = 700

#if frog_x <= car4.x + car4.length and frog_y <= car4.y + 20:
    #frog_y = 700

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
        frog_y -= 56
    if key == 's':
        frog_y += 56
    
