def add(x,y) :
  return x + y

def subtract(x,y) :
    return x - y

def multiply(x,y) :
  return x * y

def divide(x,y) :
  return x / y

print("Selecione a Operação")
print("1. ˚ ꒷Adição")
print("2. ˚ ꒷Subtração")
print("3. ˚ ꒷Multiplicação")
print("4. ˚ ꒷Divisão")
choice = input("Coloque uma das opções: ")

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))

if choice == '1' :
  print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2' :
  print(num1, "-", num2, "=", subtraction(num1,num2))

elif choice == '3' :
  print(num1, "x", num2, "=", multiply(num1,num2))

elif choice == '4' :
  print(num1, "/", num2, "=", divide(num1,num2))
  
else :
  print("Erro.")

# Calculadora Simples mesmo
