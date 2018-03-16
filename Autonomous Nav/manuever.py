import numpy as np

def rock_manuever(Rover):
    Rover.manuever_flag = 'True'
    rock_ang = abs(Rover.rock_ang.min())
    rock_dist = abs(Rover.rock_dist.min())
    if rock_dist > Rover.rock_stop_forward:
        if Rover.vel > .8:
            Rover.throttle = 0
            Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
        if Rover.vel < .8:
            Rover.throttle = .5
            Rover.brake = 0
            Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
    if rock_dist < Rover.rock_stop_forward:
        Rover.throttle = 0
        if rock_ang >.7 and rock_dist < 60:
            if Rover.vel > 0: 
                Rover.brake = .1
    if Rover.vel == 0:
        Rover.throttle = 0
        Rover.brake = 0
        if (Rover.rock_ang.min()) > 0:
            Rover.steer = 4
        if (Rover.rock_ang.min()) < 0:
            Rover.steer = -4
    if abs(Rover.rock_ang.min()) < .2:
        Rover.steer = np.clip(np.mean(Rover.rock_ang * 180/np.pi), -15, 15)
        Rover.throttle = .5
        Rover.brake = 0
    if Rover.near_sample:
        Rover.throttle = 0
        Rover.brake = 1
        if Rover.near_sample and Rover.vel == 0:
            Rover.send_pickup = 'True'
            Rover.reverse = 'True'
        else:
            Rover.send_pickup = 'False'
            Rover.brake = 0
    return Rover
   

    
    
    
    