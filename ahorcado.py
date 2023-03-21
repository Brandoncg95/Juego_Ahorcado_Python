##Parcial #1

##Realizar un juego de ahorcado con las siguientes condiciones:

##- Digitar la palabra que se va adivinar - input
##- 5 vidas.While
##- La palabra la digita el usuario - input
##- Debe de visulaizar siempre como va el avance del ahorcado. PRINT
##- En cada ciclo del juego debe de aparecer el numero de vidas que tiene y que digite nuevamente la palabra.
##- Debe mostrar las letras digitadas.
##- El juego acaba cuando arme la palabra o se me acabe las vidas.
## Al terminar el juego debe volverse a iniciarse

def iniciar():
    palabra=input("Digite la palabra a adivinar: ").lower()
    vidas=5
    letra_Adivinada=[" _ " for letra in palabra]
    letras_digitadas= []
    
    while vidas > 0 and  " _ " in letra_Adivinada:
        print(f"Adivina la palabra: {''.join(letra_Adivinada)}")
        print(f"vidas restantes: {vidas}")
        letra=input("Digite una letra: ").lower()
        if letra in letras_digitadas:
            print("Ya digitaste la letra, digita otra: ")
        elif letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    letra_Adivinada[i] = letra
            print(f"¡Correcto! La letra {letra} está en la palabra.")
        else:
            vidas -=1
            print(f"Incorrecto, la letra {letra} no esta en la palabra por lo cual  pierdes una vida: ")
     
    if " _ " not in letra_Adivinada:
        print(f"¡Felicidades! Adivinaste la palabra '{palabra}'.")
    else:
        print(f"Perdiste, te quedaste sin vidas . La palabra era '{palabra}'.")  
        
  
iniciar()

