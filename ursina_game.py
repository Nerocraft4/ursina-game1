from ursina import *

app = Ursina()

class Wall(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='quad'
        self.color = color.blue
        self.collider = 'box'
        self.x = 3

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='quad'
        self.color = color.red
        self.collider = 'box'

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        '''
        if key == 'space':
            self.animate_y(2, duration=2, curve=curve.out_sine)
            self.animate_y(0, duration=2,delay=1)
        '''
        if key == "escape":
            application.quit()

    def update(self):
        #fix 2 inputs by square-rooting speed, switch case?
        self.x += held_keys['d'] * time.dt * 10
        self.x -= held_keys['a'] * time.dt * 10
        self.y += held_keys['w'] * time.dt * 10
        self.y -= held_keys['s'] * time.dt * 10

player = Player()
box = Wall()

app.run()
