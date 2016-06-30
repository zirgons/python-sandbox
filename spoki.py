#!/usr/bin/python
from random import randint
print('Spoku spēle')
jūtos_drosmīgs = True
rezultāts = 0
while jūtos_drosmīgs:
    spoka_durvis = randint(1,2)
    print('Tev prikšā ir trīs durvis')
    print('Aiz vienām ir spoks')
    print('Kuru durvi atvērsi?')
    durvis = input ('1, 2 vai 3?')
    durvju_num = int(durvis)
    
    if durvju_num == spoka_durvis:
    	print('Spoks')
    	jūtos_drosmīgs = False
    else:
    	print('Spoka nav!')
    	print('Tu vari ienākt nākamejā istabā')
    	rezultāts = rezultāts + 1
print('Bēdz prom!')
print('Spēles beigas tu ieguvi', rezultāts, 'punktus')
