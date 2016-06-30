#!/usr/bin/env python

class color:
	black = "\033[30m"
	red = "\033[31m"
	green = "\033[32m"
	yellow = "\033[33m"
	blue = "\033[34m"
	magenta = "\033[35m"
	cyan = "\033[36m"
	white = "\033[37m" 
#limbo


from random  import randint
import sys
burti_uzrakstīti = 0
vārdā_burti = 5
minējumi = 0
print('limbo')

vārdi = ["kaķis", "spoks", "vista", "kauls", "limbo", "vanna", "ķerra", "lapas", "mājas", "vilks", "kāmis", "nazis", 
        "mutes", "žagas", "laiks", "ērces", "solas", "lampa", "atoms", "bulta", "laipa"]
izvēlētais_numurs = randint(0, len(vārdi)-1)
datora_vārds = vārdi[izvēlētais_numurs]

ir_uzvarējis = False

#print("Es iedomājos vārdu: " + datora_vārds)

while not ir_uzvarējis and minējumi < 5:
    print('uzmini vārdu par ko es domāju')
    print( 'pieci burti vārdā')
    vārds = input('Uzmini vārdu: ')
    burti_uzrakstīti = 0
    minējumi = minējumi + 1

    for i in range(5):
        datora_burts = datora_vārds[i]
        burts = vārds[i]

        if burts == datora_burts:
            sys.stdout.write(color.green + burts)
            burti_uzrakstīti = burti_uzrakstīti + 1
        
        elif burts in datora_vārds:
            sys.stdout.write(color.red + burts)
        else:
            sys.stdout.write(color.white + burts)


    print(color.white)
    #  print("Uzminēti burti: ", burti_uzrakstīti)

    if burti_uzrakstīti == vārdā_burti:
        ir_uzvarējis = True


if ir_uzvarējis:
    print('Tu atminēji man vārdu')
    print('tas bija vārds ' + datora_vārds)
else:
     print('Tu neuziminēji manu vārdu kas bija ' + datora_vārds)