
'''
text-based adventure game: Players make choices that lead to different outcomes
correct choices: [B, A, B, A, B, A]
'''

import time

def main():
    story()


def story():
    chapter1()
    chapter2()
    chapter3()
    chapter4()
    chapter5()
    chapter6()
    ending()


def chapter1():
    print('\nThis is the game "Shadows of Solitutde: An Alien Game')
    print("You'll be able to make decisions throughout the story. Each decision is vital. Think carefully!\n")

    time.sleep(4)
    print("--Story Start--")

    intro_text = '''You are Amanda, a lone survivor aboard the abandoned space station "USCSS Epsilon." Waking from cryosleep, you find yourself alone, surrounded by flickering lights and echoing corridors. An eerie silence hangs in the air as you realize the station's distress signal has been broadcasting on a loop. Your mission: uncover the truth behind the station's desolation and escape before the alien predator finds you. '''
    print(intro_text, '\n')
    time.sleep(4)

    print('As you explore the station, you come across a control room. The monitor displays two options: "Activate Emergency Beacon" or "Access Security Logs." Time is running out. Choose wisely:')
    print('Option A: Activate Emergency Beacon')
    print('Option B: Access Security Logs\n')

    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'A':
        print("The blaring emergency beacon signal attracts the alien's attention. It swiftly descends upon you, ending your life in a flurry of terror.")
        quit()


def chapter2():
    time.sleep(2)
    print('\nInside the control room, you find an access panel with wires hanging loose. Sparks fly as you see a door nearby with a sign labeled "Emergency Escape." The ominous sounds of approaching footsteps reach your ears. Choose your next move:')
    print('Option A: Attempt to repair the wires')
    print('Option B: Flee through the emergency escape door\n')

    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'B':
        print("\nAs you burst through the escape door, you find yourself in a narrow corridor. The alien's screech echoes through the halls, and before you can react, its tail strikes, sealing your fate.")
        quit()


def chapter3():
    time.sleep(2)
    print('\nIn the narrow maintenance tunnels, you spot an intersection. The sound of hissing grows louder. Your flashlight flickers, casting long shadows. Your heart races. Choose your path:')
    print('Option A: Turn left and head towards the storage room')
    print('Option B: Go right and seek refuge in the crew quarters\n')

    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'A':
        print("\nYou enter the storage room, hoping to find refuge. But as you scramble for the door, the alien's jaws clamp down on your shoulder, its deadly embrace sealing your doom.")
        quit()


def chapter4():
    time.sleep(2)
    print("\nIn the dimly lit storage room, you find a discarded flamethrower and a broken window leading to the exterior. The alien's presence is imminent. Choose your method of defense:")
    print("Option A: Attempt to repair the flamethrower")
    print("Option B: Escape through the broken window\n")
    
    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'B':
        print("\nThe broken window offers no sanctuary. As you struggle to squeeze through, the alien's swift strike from the darkness ends your desperate bid for freedom.")
        quit()


def chapter5():
    time.sleep(2)
    print("\nAs you flee the storage room, you stumble upon an abandoned communications room. The static of an incoming transmission fills the air. Your pulse quickens. Choose your course of action:")
    print('Option A: Attempt to establish contact with potential rescuers')
    print('Option B: Mute the transmission to avoid detection\n')

    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'A':
        print('\nThe transmission only serves to pinpoint your location. The alien crashes through the ceiling, its elongated arms snaring you in a deadly grasp.')
        quit()


def chapter6():
    time.sleep(2)
    print("\nIn the control room, you discover a functional shuttle ready for launch. The alien's chilling growls echo through the hallway. Time is running out. Choose your escape route:")
    print('Option A: Launch the shuttle and flee the space station')
    print('Option B: Stay and continue searching for answers\n')
    
    while True:
        try:
            option = input("Enter 'A' or 'B': ")
            if option.upper() != 'A' and option.upper() != 'B':
                continue
            else: 
                break
        except Exception as e:
            print("Error {e}")

    if option.upper() == 'B':
        print("\nAs you search the control room, the alien's monstrous form suddenly looms behind you. Its deadly appendage pierces your back, your final moments suffused with a chilling realization.")
        quit()


def ending():
    time.sleep(2)
    print("\nYou muster all your courage and initiate the shuttle launch sequence. The engines roar to life, and the station trembles as you're propelled into the void of space. As you look back, you witness the alien predator lunge towards the shuttle, its monstrous form disappearing into the distance. With a mixture of relief and sorrow, you escape the clutches of the station and the alien's relentless pursuit. Your journey continues, and the truth behind the station's desolation remains shrouded in mystery.\n")

    print("--Story End--")
    print("Thank you for playing the game.")


main()