from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=1)

def update():   # update gets automatically called.
    if(held_keys['j']!=0):
        sprint = 2
    else:
        sprint = 1
    player.x += held_keys['d'] * .1 * sprint
    player.x -= held_keys['a'] * .1 * sprint
    player.y += held_keys['w'] * .1 * sprint
    player.y -= held_keys['s'] * .1 * sprint
    player.z += held_keys['q'] * .1 * sprint
    player.z -= held_keys['e'] * .1 * sprint
		
app.run()
