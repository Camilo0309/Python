import turtle

window = turtle.Screen()

square = turtle.Turtle()


numero = input("introduce un numero ")

for i in range(4):
 square.forward(numero)
 square.left(90)


turtle.mainloop()




