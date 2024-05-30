class User:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.country = None

    def user_information(self):
        print(self.name + " " + self.surname + " is " + str(self.age)
              + " years old and lives in " + self.country + ".")


john_smith = User()

john_smith.name = input()
john_smith.surname = input()
john_smith.age = int(input())
john_smith.country = input()

john_smith.user_information()