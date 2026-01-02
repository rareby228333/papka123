import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.check = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.check -= 0.9

    def to_work(self):
        print("I go to work")
        self.check += 1000
        self.gladness -= 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.check <= 0:
            print("I have to go to work")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Check = {round(self.check, 2)}")

    def live(self, day):
        day_info = f"Day {day} of {self.name}'s life"
        print(f"{day_info:=^50}")

        if self.progress <= 1:
            self.to_study()
        elif self.gladness <= 4:
            self.to_sleep()
        elif self.check <= 5:
            self.to_work()
        else:
            self.to_chill()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")

for day in range(367):
    if not nick.alive:
        break
    nick.live(day)

    if(day == 367):
        nick.end_of_day()
print("student have lived for entire year, code shuts down...")
print(nick.name)