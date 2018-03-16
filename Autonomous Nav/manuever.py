import numpy as np

def rock_manuever(Rover):
    Rover.manuever_flag = 'True'
    rock_ang = abs(Rover.rock_ang.min())  #Load min of class variable into local variable
    rock_dist = abs(Rover.rock_dist.min())  #Load min of class variable into local variable
    if rock_dist > Rover.rock_stop_forward:  #limit speed as Rover approaches rock samples
        if Rover.vel > .8:
            Rover.throttle = 0
            Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
        if Rover.vel < .8:
            Rover.throttle = .5
            Rover.brake = 0
            Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
    if rock_dist < Rover.rock_stop_forward:  #Prevent overshooting of rock samples
        Rover.throttle = 0
        if rock_ang >.7 and rock_dist < 60:  #Allows the rover to turn and realign with the rock and approach
            if Rover.vel > 0: 
                Rover.brake = .1
    if Rover.vel == 0:
        Rover.throttle = 0
        Rover.brake = 0
        if (Rover.rock_ang.min()) > 0:
            Rover.steer = 4
        if (Rover.rock_ang.min()) < 0:
            Rover.steer = -4
    if abs(Rover.rock_ang.min()) < .2:  #When Rover is lined up with rock increase speed pickup rock
        Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
        Rover.throttle = .5
        Rover.brake = 0
    if Rover.near_sample:  #Apply brake when Rover is near sample
        Rover.throttle = 0
        Rover.brake = 1
        if Rover.near_sample and Rover.vel == 0:  #When stopped in fron of rock send pick up command
            Rover.send_pickup = 'True'
            Rover.reverse = 'True'
        else:
            Rover.send_pickup = 'False'
            Rover.brake = 0
    return Rover
   

    
    
    
    