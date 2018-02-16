input = raw_input("Talk to walle: ")

def walle_talk(input):
    if(input == input.lower()):
        print "Dirrrrr-ect-tivvve?"
    else:
        print "EEEEEEEEEEEVAAAAAAAAAA!"
walle_talk(input)

user_input = raw_input("Do you want to ask walle anything?")
def speak_to_walle(user_input):
    if(user_input != "BYE"):
        return user_input
    else:
        break
