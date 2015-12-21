# Midterm project.py
# External Ballistics of a bullet

from visual.controls import *
from visual.graph import *
import matplotlib
import matplotlib.pyplot as plt

scene.title = 'External Ballistics of Bullets'
scene.background = color.gray(0.2)
scene.forward = (1,0,0)
scene.width = 1000
scene.center = (-25,0,5)
scene.range = 75
scene.visible = True

c = controls (title = 'Variable Control', x = 0, y = 450, width = 1000, height = 450, range =300, background = color.gray(0.25))
s1 = slider(pos = (-230, -10), min = 100, max =1000, value = 100)
l1 = label(display=c.display, text = 'Distance to Target from 100 - 1000 m)', pos = (-180, 10), height = 10, width = 50 )
s2 = slider(pos = (-230,50), min = -15, max =15, value = 0)
l2 = label(display=c.display, text = 'Cross Wind Speed (m/s) (-15 - 15) Negative is out of the left', pos = (-180, 70), height = 10, width = 50 )

t1 = toggle(display = c.display, pos = (-180,-70,0), width = 25, height = 25, text0 = 'Right Hand Twist', text1 = 'Left Hand Twist')

m1 = menu(display = c.display, pos = (200, 70,0), width = 200, height = 20, text = 'Caliber Selection')
m1.items.append (('7mm', lambda: seven_rem_mag()))
m1.items.append (('.223', lambda: two_two_three()))
m1.items.append (('.308', lambda: three_Oh_eight()))
m1.items.append (('300 Wby Mag', lambda: three_hundred_wby()))
m1.items.append (('7mm Ultra Mag', lambda: seven_ultra_mag()))
m1.items.append (('.416 Rigby', lambda: four_sixteen_rigby()))
m1.items.append (('.17 Rem', lambda: seventeen_rem()))
m1.items.append (('.22-250', lambda: two_two_fifty()))

b = button(text = 'Shoot!', pos = (0, -60), height = 50, width = 50, action=lambda: run() )


gd = gdisplay(x = 1000, y = 450, width = 500, height = 450, title = 'Graph of bullet trajectories', xtitle = 'Distance (m)', ytitle = 'Drop (m)', background = color.gray(0.25))
gd.display.visible = True





scene2 = display(title = 'Target', x  = 1000, width = 500)
target2 = box (pos = (0,0,0), length = 50, width = 10, height = 50, color = color.black)
scene2.background = color.gray(0.2)
scene2.range = 50


def seven_rem_mag():
    ### BULLET INFO 7mm ###
    global caliber
    caliber = 0.5 * 0.0072136
    global Cd
    Cd = 0.457
    global A
    A = 0.00160782
    global m
    m = .093958422
    global MV
    MV = 826.008

def two_two_three():
    ### BULLET INFO .223 Caliber ###
    global caliber
    caliber = 0.5 * 0.0056896
    global Cd
    Cd = 0.255
    global A
    A = 0.00100076
    global m
    m = .035639401
    global MV
    MV = 1121.664

def three_Oh_eight():
    ### BULLET INFO .308 Caliber ###
    global caliber
    caliber = 0.5 * 0.0078232
    global Cd
    Cd = 0.477
    global A
    A = 0.0018923
    global m
    m = .10691820
    global MV
    MV = 822.96


def three_hundred_wby():
    ### BULLET INFO .300 Wby Caliber ###
    global caliber
    caliber = 0.5 * 0.0078232
    global Cd
    Cd = 0.477
    global A
    A = 0.00100076
    global m
    m = 0.097198367
    global MV
    MV = 1078.992


def seven_ultra_mag():
    ### BULLET INFO 7mm Ultra Mag Caliber ###
    global caliber
    caliber = 0.5 * 0.0072136
    global Cd
    Cd = 0.457
    global A
    A = 0.00160782
    global m
    m = .090718476
    global MV
    MV = 1043.94


def four_sixteen_rigby():
    ### BULLET INFO .416 Rigby Caliber ###
    global caliber
    caliber = 0.5 * 0.0105664
    global Cd
    Cd = 0.364
    global A
    A = 0.00345186
    global m
    m = .25919565
    global MV
    MV = 731.52

def seventeen_rem():
    ### BULLET INFO .17 Rem ###
    global caliber
    caliber = 0.5 * 0.004318
    global Cd
    Cd = 0.270
    global A
    A = 0.00058928
    global m
    m = .012959782
    global MV
    MV = 1295.4

def two_two_fifty():
    ### BULLET INFO .22-250 ###
    global caliber
    caliber = 0.5 * 0.005588
    global Cd
    Cd = 0.255
    global A
    A = 0.00100076
    global m
    m = .032399456
    global MV
    MV = 1158.24
    
    
 
    


def run ():
  
    
    
    scene.select() 
    L = s1.value

    for obj in scene.objects:
       obj.visible = False

    background = [(0,50), (0,0), (50,0)]
    extrusion(pos= [(0,-25,0), (0,-25,L)], shape = background, color = color.orange, material = materials.rough)
    target = box (pos = (-25, 0,L+5), length = 50, width = 30, height = 50, color = (0,0,0) )
    
    bullet_tip = cone(pos = (-25,0,0), axis = (0,0,2), radius = 0.5)
    bullet_body = cylinder(pos = (-25,0,-3), axis = (0,0,3), radius = 0.5)
    bullet_body.trail = curve(pos = [bullet_body.pos], color = color.red)

    scene.center = (-25,0,5)
    ### GUN INFO ###

    twist = 0.3048 #for 1/12 twist

    for direction in range (0,1):
        if t1.value == 0:
            direction = 1 #Right Handed twist
        else:
            direction == -1

        
    
    


    ### CONSTANTS ###

    p = 1.184
    g = 9.8
    y = 0
    z = 0
    M = 0
    dt = 0.01
    t = 0
    corr = 1/dt # Scale correction for the time
    v = MV


    theta = 0
    theta = theta*pi/180
    vz = v*cos(theta)
    vy = v*sin(theta)
    ws = s2.value #wind speed
    vm = 0 

    vz_end = 0
    vy_end = 0
    vm_end = 0



    ### CONSTANTS ###

    while bullet_body.pos.z <= target.pos.z :
        rate (100)


        vt = sqrt((2*m*g) / (p*A*Cd)) #Calculates the Terminal velocity of the bullet



        #plt.plot (bullet_body.pos.z, bullet_body.pos.y, 'bo') #Graphs the bullet positions

        v = sqrt (vz*vz + vy*vy) #Recombines the vectors vz and vy to create v

        def f(vz):                  #Calculates wind resistance in the z direction
            return -g*v*vz/(vt*vt)

        s = v*twist  #the revelutions per second of the bulelt

        Vr = 2*pi*caliber*s #rotational velocity of bullet

        G = 2*pi*caliber*Vr #vortex strength

        def lift(ws):     #The formula for the lift on a spinning cylinder
            return p*G*ws * direction # The * direction is a correction either positive or negative for barrel twist direction

        def fn(vy):                                     #Calculates wind resistance in the y direction
            return -g*(1.0 + v*vy / (vt*vt)) + lift(ws)

        ### CALCULATES THE DERIVITAVE USING HUEN's METHOD ###
        vz_end = vz + f(vz) * dt        
        vz = vz + (f(vz_end) + f(vz))*dt/2

        vy_end = vy + fn(vy) * dt
        vy = vy + (fn(vy_end) + f(vy))*dt/2

        z = z + vz*dt
        y = y + vy*dt

        t = t + dt

        ### CALCULATES THE DERIVITAVE USING HUEN's METHOD ###

        bullet_tip.pos.z += z/corr #divide by corr to correct scale since each calulation occurs at 1/corr of a second
        bullet_body.pos.z +=z/corr  #divide by corr to correct scale since each calulation occurs at 1/corr of a second



        bullet_tip.pos.y += (y ) /corr  #divide by corr to correct scale since each calulation occurs at 1/corr of a second
        bullet_body.pos.y += (y )/corr  #divide by corr to correct scale since each calulation occurs at 1/corr of a second





        bullet_body.trail.append(pos = bullet_body.pos) #Updates the bullet trail
        
        scene.center = bullet_body.pos #Constantly updates the center of the scene to where the bullet is

        
        f1 = gdots(color = color.red)
        f1.plot(pos = (bullet_body.pos.z,bullet_body.pos.y))

    if bullet_body.pos.z >= target.pos.z:  #function to adjust scene center after bullet has struck the target
        scene.center = target.pos
        scene2.select() #Selects the 2nd window to put an object into
        hit = sphere( color = color.red, pos = (0,bullet_body.pos.y,4), radius = 1.5) #puts a shphere in the second window where the bullet hit the target
                    

    #plt.show()
