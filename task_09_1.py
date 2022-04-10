import time
class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self, r, y, g):
        print(TrafficLight.__color[0])
        time.sleep(r)
        print(TrafficLight.__color[1])
        time.sleep(y)
        print(TrafficLight.__color[2])
        time.sleep(g)


a = TrafficLight()
a.running(7, 2, 3)
