# ---------------------FlyBehavior---------------#
class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I can fly")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyWithRocket(FlyBehavior):
    def fly(self):
        print("I'm flying with rocket")


# ---------------------QuackBehavior---------------#
class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("Nothing")


# ----------------------Duck Abstract class---------#
class Duck:
    flyBehavior = FlyBehavior()
    quackBehavior = QuackBehavior()

    def swim(self):
        print("I can swim")

    def display(self):
        pass

    def perform_fly(self):
        self.flyBehavior.fly()

    def perform_quack(self):
        self.quackBehavior.quack()

    def set_quack_behavior(self, qb):
        self.quackBehavior = qb

    def set_fly_behavior(self, fb):
        self.flyBehavior = fb


# -------------------Duck Types----------------#
class MallardDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = Quack()

    def display(self):
        print("I'm a MallardDuck")


class RedheadDuck(Duck):
    def display(self):
        print("I'm a ReadheadDuck")


class RubberDuck(Duck):
    flyBehavior = FlyNoWay()
    quackBehavior = Squeak()

    def display(self):
        print("I'm a RubberDuck")


class DecoyDuck(Duck):
    def display(self):
        print("I'm a DecoyDuck")


duck = MallardDuck()
duck.display()
duck.perform_fly()
duck.perform_quack()
# ----------print-------------#
# I'm a MallardDuck
# I can fly
# Quack

duck1 = RubberDuck()
duck1.display()
duck1.perform_quack()
duck1.perform_fly()
# ----------print-------------#
# I'm a RubberDuck
# Squeak
# I can't fly

# ---------------Change flying-------------#
duck1.set_fly_behavior(FlyWithRocket())
duck1.perform_fly()

# ----------print-------------#
# I'm a RubberDuck
# Squeak
# I can't fly
# ----------changed part----------#
# I fly with rocket
