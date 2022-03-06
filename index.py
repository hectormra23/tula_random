import random 
from playsound import playsound 
import time
import numpy



valores = ["Si" ,"No" , "Si","No"]



def azar_si_no(valores):

    return numpy.random.choice(valores)



nombre = input("ingresa tu nombre")
medida = random.randint(5,30)
gay_o_no =  random.randint(1,2) 
complemento =" tu tula es..."

if azar_si_no == "Si":
    print(nombre + "..."  "Deja la paja")  
    playsound("meme-plantilla (mp3cut.net).mp3")
else:
    print(nombre + "..."  "Eres gay bro UnU")   
    playsound("gay-meme.mp3")
time.sleep(1.3)



if medida > 15:

    print(nombre + "..." + complemento + "grande" )
    playsound('yamete-kudasai-sound-effect-original.mp3') 
else:
    print(nombre + "..." + complemento + "chica"  )
    playsound('mona sad unu.mp3')



