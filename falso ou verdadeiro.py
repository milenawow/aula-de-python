nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
matriculado = input("voce esta matriculado? (s/n): ")

if matriculado.upper() == "s":
   matriculado = True
print(f"nome: {nome}")
print(f"idade: {idade} ")
print(f"matriculado: {'sim' if matriculado else 'não'}")
      
            