import requests
import json
import pickle
pokemon = input("Ingresa un pokemon: ")
#while para pokemon inexistente

url = "https://pokeapi.co/api/v2/pokemon/{0}".format(pokemon) 

try :
    respuesta = requests.get(url,timeout=10)
except requests.Timeout:
    print("Error: El tiempo de espera ha finalizado")

if respuesta.status_code != 200 : 
    print("Pokemon no encontrado" )
else : 
    print(respuesta)

response = requests.get(url)
data = json.loads(response.text)

# print (data)

print("Peso")
print(data["weight"])

print("Tamaño")
print(data["height"])

print("Movimientos:")
for i in range(len(data["moves"])):
    print(data["moves"][i]['move']['name'])

print("Habilidades:")
for i in range(len(data["abilities"])):
    print(data["abilities"][i]['ability']['name'])

print("Tipos:")
for i in range(len(data["types"])):
    print(data["types"][i]['type']['name'])

info = {}
info["Peso"] = data["weight"]

info = {}
info["Tamaño"] = data["height"]

info = {}
info["Movimientos"] = data["moves"]

info = {}
info["Habilidades"] = data["abilities"]

info = {}
info["Tipos"] = data["types"]

print(info)

with open('ejemplo.json', 'wb') as archivo:
    pickle.dump(info, archivo)

# arch = json.loads("C:\Users\MS-XUserPC\Desktop\PHYTON\UCAMP\Modulom\Semanam\ejemplo.json")
# print(arch)