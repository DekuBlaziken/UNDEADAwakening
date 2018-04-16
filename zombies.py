from gamelib import *

game = Game(866,487, "UNDEAD Awakening")

#Graphics
p1 = Image("p1.png",game)
p2 = Image("p2.png",game)
p1.y = game.height - 100
p2.y = game.height - 100
p1.x = 80

bg = Image("wave 4.png",game, False)
game.setBackground(bg)

#Sounds
gun = Sound("Gun.wav", 1)

#Zombie Wave 1
zombie = []
for index in range(50):
    zombie.append(Image("zombie2.png",game))
    zombie[index].y = game.height - 110
    zombie[index].resizeBy(50)
    
for index in range(50):
    x = randint(100,700)
    y = randint(100,4000)
    zombie[index].moveTo(x, -y)
    zombie[index].resizeBy(-60)
    s = randint(8,12)
    zombie[index].setSpeed(s,180)

#bullets
plasmaball = Animation("plasmaball1.png",11,game,352/11,32)
plasmaball.resizeBy(-20)
plasmaball.visible = False


#Wave 1
zombiewave1complete = 0
while not game.over:
    game.processInput()
    bg.draw()
    p1.draw()
    plasmaball.move()
    zombie[index].draw()

    if mouse.LeftClick:
        plasmaball.moveTo(p1.x - 20, p2.y - 20)
        plasmaball.setSpeed(24,-90)
        plasmaball.visible = True
        gun.play()

    for index in range(50):
        zombie[index].move()

    if p1.isOffScreen("bottom") or p1.isOffScreen("top") :
        p1.y = game.height - 100

    #if plasmaball.collidedWith(zombie) and zombie[index].visible:
        zombie[index].visible = False


#Player1 Control
    if keys.Pressed[K_UP]:
        p1.y -= 8
    if keys.Pressed[K_DOWN]:
        p1.y += 8
    if keys.Pressed[K_RIGHT]:
        p1.x += 8
    if keys.Pressed[K_LEFT]:
        p1.x -= 8
    game.update(30)
