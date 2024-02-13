todos = ["Comprar Pan", "Sacar a pasear al perro", "Comprar Agua"]

persona = {
    "nombre": "",
    "apellido": "",
    "direccion": ""
}



tablero = [0,0,0,0,0,0,0,0,0]


tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(tablero[2][1])

for row in tablero:
    for col in row:
        print(col)
        

stack = []
queue = []

stack.append(1)
stack.append(2)
stack.append(3)

config = {
    "db": {
        "host": "127.0.0.1",
        "port": "5432",
        "user": "postgres",
        "pass": "postgres"
    },
    "api": {
        "host": "127.0.0.1",
        "port": "5000"
    }
}


config["db"]["host"]