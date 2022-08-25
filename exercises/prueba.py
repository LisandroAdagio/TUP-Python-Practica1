Compras={
    "Mario Pedernera" : ["cafetera", "TV 50 pulgadas", "mouse gamer"],
    "Ezequiel Castello" : ["ipad", "ipod", "iphone"],
    "Pablo Piristrelli" : ["Reproductor de CD", "Videograbadora"],
}
print(Compras)

assert (
    (Compras["Mario Pedernera"] == ["cafetera", "TV 50 pulgadas", "mouse gamer"])
    and (Compras["Ezequiel Castello"] == ["ipad", "ipod", "iphone"])
    and (Compras["Pablo Piristrelli"] == ["Reproductor de CD", "Videograbadora"])
)