import random

print("🎯 Bem-vindo ao Jogo de Adivinhação!")
numero_secreto = random.randint(1, 100)
tentativas = 10

while tentativas > 0:
    try:
        palpite = int(input(f"Tentativas restantes ({tentativas}). Digite um número entre 1 e 100: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if palpite < 1 or palpite > 100:
        print("⚠️ O número deve estar entre 1 e 100!")
        continue

    if palpite == numero_secreto:
        print("🎉 Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("🔼 Tente um número maior.")
    else:
        print("🔽 Tente um número menor.")

    tentativas -= 1

if tentativas == 0:
    print(f"❌ Suas tentativas acabaram. O número era {numero_secreto}.")
    print("Obrigado por jogar! Até a próxima! 🎮")