from utils.planet import Planet
class Board:
    def __init__(self):
        self.planet_array = [Planet(10, 5, '1'), Planet(90, 95, '2'), Planet(35, 10), Planet(2, 10), Planet(70, 15), Planet(41, 22), Planet(20, 27), Planet(85, 30), Planet(57, 34), Planet(18, 44), Planet(49, 41), Planet(65, 45), Planet(43, 47),
                             Planet(35, 55), Planet(57, 53), Planet(82, 56), Planet(44, 66), Planet(51, 59), Planet(15, 70), Planet(80, 73), Planet(98, 80), Planet(59, 78), Planet(30, 85), Planet(65, 90)]
        self.gui_array = []
        self.object_array = []
        self.frame_actions = []