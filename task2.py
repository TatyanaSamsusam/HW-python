# 2- Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for X in range (0,2):
    for Y in range (0,2):
        for Z in range (0,2):
            expression1 = not (X and Y and Z)
            expression2 = -X or -Y or -Z
            print (f'{X}/{Y}/{Z} {expression1 == expression2}')

# чтоб быть честной: это задание я просто списала, вникнув в суть 