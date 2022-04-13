from manim import *

import math

class ThreeSquares(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        left_square = Square(color = BLACK)
        right_square = Square(color = BLACK)
        upper_square = Square(color = BLACK)

        left_square.shift(LEFT)
        right_square.shift(RIGHT)
        upper_square.shift(UP * 2)

        self.play(Create(left_square))
        self.play(Create(right_square))
        self.play(Create(upper_square))
        self.wait()

        dotA = Dot([-1, 3, 0], color = BLACK) #right_square buttom right dot
        dotB = Dot([2, -1, 0], color = BLACK) #upper_square top left dot

        self.play(Create(dotA))
        self.play(Create(dotB))
        self.wait(0.5)

        line1 = Line(dotA.get_center(), dotB.get_center()).set_color(BLACK)

        self.play(Create(line1))

        trapezoid = [(1, 1, 0),
                     (1, 3, 0),
                     (-1, 3, 0),
                     (0.5, 1, 0)]

        #trapezoid2 = [(0, 1, 0),
        #             (0.5, 1, 0),
        #             (2, -1, 0),
        #             (0, -1, 0)]  #make moving trapezoid


        visTrapezoid = Polygon(*trapezoid, color=BLUE, fill_color=BLUE, fill_opacity=0.2)

        self.play(Create(visTrapezoid))
        self.wait()

        triangle = [(2, -1, 0),
                    (2, 1, 0),
                    (0.5, 1, 0)]

        visTriangle = Polygon(*triangle, color=BLUE, fill_color=BLUE, fill_opacity=0.2)

        self.play(Create(visTriangle))
        self.wait()

        angle = math.radians(180)
        animation = Rotate(visTrapezoid, angle=angle)
        self.play(animation)

        visTrapezoid.shift(DOWN * 2)
        visTrapezoid.shift(RIGHT)
        self.wait()




# manim -qk main.py ThreeSquares  #4k
# manim -pql main.py ThreeSquares  #480p






