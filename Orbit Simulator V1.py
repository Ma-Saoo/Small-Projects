import pygame
import math
pygame.init() #initialize module

##Set up pygame window
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #Game screen
pygame.display.set_caption("Planet Simulation") #Title of game

font = pygame.font.SysFont("comicsans",16) #Font for text

WHITE = (255,255,255) # Color code
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (178, 190, 181)
YELLOW = (255, 255, 0)
WHITE_YELLOW = (255, 255, 224)

class Planet: # OOP of class Planet
    AU = 149.6e6 * 1000 # in Meters
    G = 6.67428e-11 # Gravitational Constant
    SCALE = 80 / AU # What does 1 meter represent in pixels??
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, name, x, y, radius, mass, color):
        self.name = name
        self.x = x #in meters
        self.y = y #in meters
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.is_sun = False
        self.distance_to_sun = 0

        self.x_vel = 0 #in meters
        self.y_vel = 0 #in meters

    def draw(self, win):
        x=self.x * self.SCALE + WIDTH/2 # Remember for coordinates (0,0) is top-left
        y=self.y * self.SCALE + HEIGHT/2

        if(len(self.orbit)>2):
            scaled_points=[]
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                scaled_points.append((x,y))
            pygame.draw.lines(win, self.color, False, scaled_points, 2)
        if (self.is_sun==False):
            distance_text = font.render(f"{round(self.distance_to_sun/Planet.AU,4)}AU",1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

        pygame.draw.circle(win, self.color, (x,y), self.radius) # Draw a circle with (where = window, color of circle = self.color, xy coordinates = (x,y), radius of circle = self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        if other.is_sun:
            self.distance_to_sun = distance

        force = self.mass * other.mass * self.G / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_pos(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x,self.y))
        

##Set up infinite pygame event loop so it goes on forever unless we close the window

def main():
    a=0
    run=True
    clock = pygame.time.Clock()

    sun = Planet("Sun", 0, 0, 16, 1.98892 * 10**30, YELLOW) # Lets use radius as 30 pixel (a guess). Solar mass = 1.98892*10^30 kg
    sun.is_sun = True # it is an object which has property is_sun = True, cuz.... its the sun 

    earth = Planet("Earth", -1 * Planet.AU, 0, 9, 5.9742 * 10**24, BLUE)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet("Mars", -1.524 * Planet.AU, 0, 7, 6.39 * 10**23, RED)
    mars.y_vel = 24.077 * 1000

    mercury = Planet("Mercury", 0.387 * Planet.AU, 0, 5, 3.3 * 10**23, GRAY)
    mercury.y_vel = -47.4 * 1000

    venus = Planet("Venus", 0.723 * Planet.AU, 0, 6, 4.8685 * 10**24, WHITE_YELLOW)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]
    
    while(run):
        a+=1
        clock.tick(60) #Maximum refresh is 60
        if(a==720):
            sun.mass=0.01
            sun.color=WHITE
        WIN.fill((0,0,0)) # Background refresh it everytime

        for event in pygame.event.get(): #Mouse movement, keyboard presses, mouse clicks, etc
            if event.type==pygame.QUIT: #If user presses X button to close window
                run = False #Stop while loop

        for planet in planets:
            planet.update_pos(planets)
            planet.draw(WIN)

        pygame.display.update() # Update changes into screen
    
    pygame.quit()

main()