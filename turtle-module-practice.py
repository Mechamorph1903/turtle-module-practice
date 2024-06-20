"""

Author: Daniel Anorue

Program Title: The Little Dipper

File Description: A program that creates graphic images with the turtle module
"""



import turtle


from constellation_background import draw_bg

# Randomly adds stars to the background and turns the color black to show the night sky.
draw_bg(500)

# Your Code here.
polaris_coord = (-262.5, -78.75)
yildun_coord = (-131.25, -52.5)
epsilon_coord = (0, 0)
zeta_coord = (52.5, 105)
kochab_coord = (78.75, 210)
pherkad_coord = (157.5, 183.75)
eta_coord = (105, 52.5)



name = "Polaris (Alpha)"
turtle.penup()
turtle.goto(polaris_coord)
turtle.pendown()
turtle.pencolor('#FFFFFF')
turtle.dot(26, '#FFFFFF')
turtle.write(f"{name}\n({polaris_coord[0]},{polaris_coord[1]})\n", align="center")
             
name = "Yildun (Delta)"
turtle.goto(yildun_coord)
turtle.dot(8, '#6666FF')             
turtle.write(f"{name}\n({yildun_coord[0]},{yildun_coord[1]})\n", align="center")

name = "Epsilon"
turtle.goto(epsilon_coord)
turtle.dot(8, '#DDDDDD')
turtle.write(f"{name}\n({epsilon_coord [0]},{epsilon_coord [1]})\n", align="center")


name = "Zeta"
turtle.goto(zeta_coord)
turtle.dot(8, '#6666FF')
turtle.write(f"{name}\n({zeta_coord[0]},{zeta_coord[1]})\n", align="center")

name = "Kochab (Beta)"
turtle.goto(kochab_coord)
turtle.dot(26, '#F2B329')
turtle.write(f"{name}\n({kochab_coord[0]},{kochab_coord[1]})\n", align="center")             

name = "Pherkad (Gamma)"
turtle.goto(pherkad_coord)
turtle.dot(8, '#6666FF')
turtle.write(f"{name}\n({pherkad_coord[0]},{pherkad_coord[1]})\n", align="center")

name = "Eta"
turtle.goto(eta_coord)
turtle.dot(8, '#6666FF')
turtle.write(f"{name}\n({eta_coord[0]},{eta_coord[1]})\n", align="center")

turtle.goto(zeta_coord)

# Keeps the window open if not running in IDLE
turtle.done()

