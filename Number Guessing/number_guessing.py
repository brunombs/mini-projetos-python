import random
import time
print('Olá, seja bem-vindo ao jogo! :)')
time.sleep(2)
n = random.randint(1, 10)
print('Um número aleatório foi gerado!!!\nVocê tem 4 chances para adivinhar o número!')

count = 4

while count != 0:
    a = int(input('Adivinhe o número: '))
    if a == n:
        print("Boa!!! Acertou o número!")
        break
    elif a > n:
        print('O número é menor que ', a)
    elif a < n:
        print('O número é maior que ', a)
    count -= 1
if count == 0:
    print('Você não conseguiu adivinhar o número!')

