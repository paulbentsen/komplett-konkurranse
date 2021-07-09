from solution_interface import SolutionInterface
import api
import random

liste=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

maxFuel = []

prevMove = []
#Prev move info:
# 0 = stayed on same spot
# 1 = Moved forward
# 2 = Turned left
# 3 = Turned right

facing = []
#Face info:
# 0 = North
# 1 = East
# 2 = South
# 3 = West

positionA = []
positionB = []

#Map info:
# 0 = darkspot
# 1 = luft
# 2 = uvisst objekt
# 3 = vegg
# 4 = var luft, nå objekt (fiende)

class Solution(SolutionInterface):
    def __init__(self):
        # You can initiate and calculate things here
        pass
    
    def update(self):
        #print map when dead
        if api.current_fuel() < 3:
            for x in liste:
                print(x)
        
        #Turn left function
        def snu_venstre():
            api.turn_left()
            print("SNUDDE VENSTRE")
            if facing[-1] == 0:
                facing.append(3)
            else:
                facing.append(facing[-1]-1)
        
        #Turn right function
        def snu_høyre():
            api.turn_right()
            print("SNUDDE HØYRE")
            if facing[-1] == 3:
                facing.append(0)
            else:
                facing.append(facing[-1]+1)
        
        #Drive forward
        def drive_forward():
            api.move_forward()
            if facing[-1] == 0:
                positionA.append(positionA[-1] - 1)
                print("pos A moved one step north")
            if facing[-1] == 1:
                positionB.append(positionB[-1] + 1)
                print("pos B moved one step east")
            if facing[-1] == 2:
                positionA.append(positionA[-1] + 1)
                print("pos A moved one step south")
            if facing[-1] == 3:
                positionB.append(positionB[-1] - 1)
                print("pos B moved one step west")
            print("Currently facing: ", facing[-1])
            print("Current position is ", positionA[-1], positionB[-1])

        print("Current fuel er: ", api.current_fuel())
        if len(facing) > 1:
            print("Currently facing: ", facing[-1])
        
        maxFuel.append(api.current_fuel())
        #make genesis map
        if api.current_fuel() == maxFuel[0]:
            facing.append(0)
            liste[23][23] = 9
            positionA.append(23)
            positionB.append(23)
        
        #Setter = 1 som luft
        counter = 0
        while counter < api.lidar_front():
            if facing[-1] == 0:
                liste[positionA[-1]-counter][positionB[-1]] = 1
            if facing[-1] == 1:
                liste[positionA[-1]][positionB[-1]+counter] = 1
            if facing[-1] == 2:
                liste[positionA[-1]+counter][positionB[-1]] = 1
            if facing[-1] == 3:
                liste[positionA[-1]][positionB[-1]-counter] = 1
            counter += 1
        
        #Setter = 3 som vegg, hvis ikke fiende er foran
        if api.identify_target() == False:
            if facing[-1] == 0:
                liste[positionA[-1]-api.lidar_front()][positionB[-1]] = 3
            if facing[-1] == 1:
                liste[positionA[-1]][positionB[-1]+api.lidar_front()] = 3
            if facing[-1] == 2:
                liste[positionA[-1]+api.lidar_front()][positionB[-1]] = 3
            if facing[-1] == 3:
                liste[positionA[-1]][positionB[-1]-api.lidar_front()] = 3

        def finn_uidentifisert_objekt():
            ufo_action = "null"
            ufo_action_verdi = 99
            ufo_felt_en = 0
            ufo_felt_to = 0

            #nord
            if facing[-1] == 0:
                if liste[positionA[-1]][positionB[-1] - api.lidar_left()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1] - api.lidar_left()] = 2
                    if api.lidar_left() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_left()
                        ufo_action = "v"
                        ufo_felt_en = positionA[-1]
                        ufo_felt_to = positionB[-1] - api.lidar_left()

                
                if liste[positionA[-1]][positionB[-1]+api.lidar_right()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1]+api.lidar_right()] = 2
                    if api.lidar_right() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_right()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1]
                        ufo_felt_to = positionB[-1]+api.lidar_right()
                
                if liste[positionA[-1]+api.lidar_back()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]+api.lidar_back()][positionB[-1]] = 2
                    if api.lidar_back() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_back()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1]+api.lidar_back()
                        ufo_felt_to = positionB[-1]
            
            #øst
            if facing[-1] == 1:
                if liste[positionA[-1]- api.lidar_left()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]- api.lidar_left()][positionB[-1]] = 2
                    if api.lidar_left() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_left()
                        ufo_action = "v"
                        ufo_felt_en = positionA[-1] - api.lidar_left()
                        ufo_felt_to = positionB[-1]
                
                if liste[positionA[-1]+api.lidar_right()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]+api.lidar_right()][positionB[-1]] = 2
                    if api.lidar_right() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_right()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1] + api.lidar_right()
                        ufo_felt_to = positionB[-1]
                    
                if liste[positionA[-1]][positionB[-1]- api.lidar_back()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1]-api.lidar_back()] = 2
                    if api.lidar_back() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_back()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1] 
                        ufo_felt_to = positionB[-1] - api.lidar_back()
                    
            #sør
            if facing[-1] == 2:
                if liste[positionA[-1]][positionB[-1]+ api.lidar_left()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1]+ api.lidar_left()] = 2
                    if api.lidar_left() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_left()
                        ufo_action = "v"
                        ufo_felt_en = positionA[-1] 
                        ufo_felt_to = positionB[-1] + api.lidar_left()
                        
                
                if liste[positionA[-1]][positionB[-1]- api.lidar_right()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1]- api.lidar_right()] = 2
                    if api.lidar_right() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_right()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1] 
                        ufo_felt_to = positionB[-1] - api.lidar_right()

                if liste[positionA[-1]- api.lidar_back()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]- api.lidar_back()][positionB[-1]] = 2
                    if api.lidar_back() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_back()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1] - api.lidar_back()
                        ufo_felt_to = positionB[-1] 

            #vest
            if facing[-1] == 3:
                if liste[positionA[-1] + api.lidar_left()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1] + api.lidar_left()][positionB[-1]] = 2
                    if api.lidar_left() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_left()
                        ufo_action = "v"
                        ufo_felt_en = positionA[-1] - api.lidar_left()
                        ufo_felt_to = positionB[-1]                         
                    
                if liste[positionA[-1]-api.lidar_right()][positionB[-1]] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]-api.lidar_right()][positionB[-1]] = 2
                    if api.lidar_right() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_right()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1] - api.lidar_right()
                        ufo_felt_to = positionB[-1] 
                
                if liste[positionA[-1]][positionB[-1] + api.lidar_back()] == 0:
                    print("fant uidentifisert objekt")
                    liste[positionA[-1]][positionB[-1] + api.lidar_back()] = 2
                    if api.lidar_right() < ufo_action_verdi:
                        ufo_action_verdi = api.lidar_right()
                        ufo_action = "h"
                        ufo_felt_en = positionA[-1]
                        ufo_felt_to = positionB[-1] + api.lidar_back() 
            
            if liste[ufo_felt_en + 1][ufo_felt_to] in (0,2,3):
                ufo_action_verdi += 3
                print("økte ufo-verdi v1")
            elif liste[ufo_felt_en - 1][ufo_felt_to] in (0,2,3):
                ufo_action_verdi += 3
                print("økte ufo-verdi v2")
            elif liste[ufo_felt_en][ufo_felt_to + 1] in (0,2,3):
                ufo_action_verdi += 3
                print("økte ufo-verdi v3")
            elif liste[ufo_felt_en][ufo_felt_to - 1] in (0,2,3):
                ufo_action_verdi += 3
                print("økte ufo-verdi v4")
                    
            return ufo_action_verdi, ufo_action, ufo_felt_en, ufo_felt_to
        ufo_action_verdi_ute, ufo_action_ute, ufo_felt_en_ute, ufo_felt_to_ute = finn_uidentifisert_objekt()

        #setter = 4 hvis man finner overraskende fiende, og returnerer beste trekk hvis fiender i nærheten (lavere action_verdi er bedre)
        def finn_fiende():
            action = "null"
            action_verdi = 99
            #nord
            if facing[-1] == 0:
                if liste[positionA[-1]][positionB[-1] - api.lidar_left()] in (1, 4):
                    print("fant en overraskende fiende (tank facing nord, fiende på venstre)")
                    liste[positionA[-1]][positionB[-1] - api.lidar_left()] = 4
                    action_verdi = api.lidar_left()
                    action = "v"
                    
                if liste[positionA[-1]][positionB[-1]+api.lidar_right()] in (1, 4):
                    print("fant en overraskende fiende (tank facing nord, fiende på høyre)")
                    liste[positionA[-1]][positionB[-1]+api.lidar_right()] = 4
                    if api.lidar_right() < action_verdi:
                        action_verdi = api.lidar_right()
                        action = "h"
                    
                if liste[positionA[-1]+api.lidar_back()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing nord, fiende på bakre)")
                    liste[positionA[-1]+api.lidar_back()][positionB[-1]] = 4
                    if api.lidar_back() < action_verdi:
                        action_verdi = api.lidar_back()
                        action = "h"
                    
            #øst
            if facing[-1] == 1:
                if liste[positionA[-1]- api.lidar_left()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing øst, fiende på venstre)")
                    liste[positionA[-1]- api.lidar_left()][positionB[-1]] = 4
                    if api.lidar_left() < action_verdi:
                        action_verdi = api.lidar_left()
                        action = "v"
                
                if liste[positionA[-1]+api.lidar_right()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing øst, fiende på høyre)")
                    liste[positionA[-1]+api.lidar_right()][positionB[-1]] = 4
                    if api.lidar_right() < action_verdi:
                        action_verdi = api.lidar_right()
                        action = "h"
                    
                if liste[positionA[-1]][positionB[-1]- api.lidar_back()] in (1, 4):
                    print("fant en overraskende fiende (tank facing øst, fiende på bakre)")
                    liste[positionA[-1]][positionB[-1]-api.lidar_back()] = 4
                    if api.lidar_back() < action_verdi:
                        action_verdi = api.lidar_back()
                        action = "h"
                    
            #sør
            if facing[-1] == 2:
                if liste[positionA[-1]][positionB[-1]+ api.lidar_left()] in (1, 4):
                    print("fant en overraskende fiende (tank facing sør, fiende på venstre)")
                    liste[positionA[-1]][positionB[-1]+ api.lidar_left()] = 4
                    if api.lidar_left() < action_verdi:
                        action_verdi = api.lidar_left()
                        action = "v"
                
                if liste[positionA[-1]][positionB[-1]- api.lidar_right()] in (1, 4):
                    print("fant en overraskende fiende (tank facing sør, fiende på høyre)")
                    liste[positionA[-1]][positionB[-1]- api.lidar_right()] = 4
                    if api.lidar_right() < action_verdi:
                        action_verdi = api.lidar_right()
                        action = "h"

                if liste[positionA[-1]- api.lidar_back()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing sør, fiende på bakre)")
                    liste[positionA[-1]- api.lidar_back()][positionB[-1]] = 4
                    if api.lidar_back() < action_verdi:
                        action_verdi = api.lidar_back()
                        action = "h"
            
            #vest
            if facing[-1] == 3:
                if liste[positionA[-1] + api.lidar_left()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing vest, fiende på venstre)")
                    liste[positionA[-1] + api.lidar_left()][positionB[-1]] = 4
                    if api.lidar_left() < action_verdi:
                        action_verdi = api.lidar_left()
                        action = "v"
                    
                if liste[positionA[-1]-api.lidar_right()][positionB[-1]] in (1, 4):
                    print("fant en overraskende fiende (tank facing vest, fiende på høyre)")
                    liste[positionA[-1]-api.lidar_right()][positionB[-1]] = 4
                    if api.lidar_right() < action_verdi:    
                        action_verdi = api.lidar_right()
                        action = "h"
                
                if liste[positionA[-1]][positionB[-1] + api.lidar_back()] in (1, 4):
                    print("fant en overraskende fiende (tank facing vest, fiende på bakre)")
                    liste[positionA[-1]][positionB[-1] + api.lidar_back()] = 4
                    if api.lidar_back() < action_verdi:
                        action_verdi = api.lidar_back()
                        action = "h"
            return action_verdi, action
        action_verdi_ute, action_ute = finn_fiende()

        # Shoot if enemy is close
        if api.identify_target() and api.lidar_front() < 4:
            api.fire_cannon()
        
        #Turn if enemy is closer than 10 grids
        elif action_verdi_ute<7:
            if action_ute == "v":
                snu_venstre()
            elif action_ute == "h":
                snu_høyre()
        
        # Shoot 
        elif api.identify_target():
            api.fire_cannon()
        
        elif ufo_action_verdi_ute < 4:
            if ufo_action_ute == "v":
                print("snudde pga ufo-funksjon nivå1")
                snu_venstre()
            elif ufo_action_ute == "h":
                print("snudde pga ufo-funksjon nivå1")
                snu_høyre()

        elif ufo_action_verdi_ute < 8 and random.randint(0,100)<30:
            if ufo_action_ute == "v":
                print("snudde pga ufo-funksjon nivå2")
                snu_venstre()
            elif ufo_action_ute == "h":
                print("snudde pga ufo-funksjon nivå2")
                snu_høyre()

        #Turn if facing wall
        elif api.lidar_front() < 2:
            print("snudde pga nærme-vegg-funksjon")
            if api.lidar_left() < api.lidar_right():
                snu_høyre()
            else:
                snu_venstre()
        
        #Turn randomly
        #elif random.randint(0,100)<10:
        #        if random.randint(0,2)==0:
        #            snu_venstre()
        #        else:
        #            snu_høyre()

        #Auto engine move forward
        else:
            drive_forward()