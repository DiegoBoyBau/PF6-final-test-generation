import json
import requests

def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    diccionario_plato = json.loads(response.content)
    return diccionario_plato

def main():
  print("Hello learners!")
  numero = input("Ingresa el numero del plato: ")
  resultado = dish_fetch(numero)
  print("Nombre:", resultado["name"])
  print("Descripción:", resultado["description"])

if __name__=="__main__":
  main()