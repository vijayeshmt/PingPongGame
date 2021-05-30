"""
Vijayesh M T

"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update,1.0/60.0)
        game.serve_ball()
        return game

#mnoving ball by calling move function
class PongGame(Widget):
        ball = ObjectProperty(None)
        player1 =ObjectProperty(None)
        player2 = ObjectProperty(None)
        def serve_ball(self):
            self.ball.velocity = Vector(4,0).rotate(randint(0,360))
        def update(self,dt):
            self.ball.move()
            #bounce top and bottom
            if (self.ball.y<0) or (self.ball.y>self.height-50):
                self.ball.velocity_y *= -1
            # bounce left and increase score
            if (self.ball.x < 0):
                self.ball.velocity_x *= -1
                self.player1.score += 1

            # bounce of right and increase score
            if(self.ball.x > self.width-50):
                self.ball.velocity_x *= -1
                self.player2.score += 1


            self.player1.bounce_ball(self.ball)
            self.player2.bounce_ball(self.ball)
#touchscreen
        def on_touch_move(self, touch):
            if touch.x < self.width / 1/4:
                self.player1.center_y = touch.y
            if touch.x > self.width * 3/4:
                self.player2.center_y = touch.y

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.05


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity   = ReferenceListProperty(velocity_x,velocity_y)

    #latest position = current velocity+current position
    def move(self):
        self.pos = Vector(*self.velocity)+(self.pos)






if __name__ == '__main__':
    PongApp().run()

