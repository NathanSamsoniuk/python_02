# Instruções:
BONUS_CONSTANT = 1000
# O programa 1. deve começar solicitando ao usuário que insira seu nome.
user_name = str(input("Please enter your name: "))

if user_name.isdigit():
    print("You entered your name incorrectly.Try again.")
    exit()
elif len(user_name) == 0:
    raise ValueError("O nome não pode estar vazio.")
    exit()

elif len(user_name) == 0:
    print("You didn't enter anything. Please try again.")
    exit()
elif user_name.isspace():
    print("You entered only spaces. Please try again.")
    exit()



# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
user_salary = float(input("Please enter your salary: "))
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
user_bonus = float(input("Please enter your bonus percentage: "))
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus_value = BONUS_CONSTANT + user_salary * user_bonus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Hello {user_name}, your bonus amount is {bonus_value:.2f}.")