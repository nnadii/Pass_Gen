import string as str
import secrets
import random  # this is the module used to generate random numbers on your given range


class PasswordGenerator:
    @staticmethod
    # must have  conditions (in a list format), for each member of the list possible_characters
    def gen_sequence(conditions):
        possible_characters = [
            str.ascii_lowercase,
            str.ascii_uppercase,
            str.digits,
            str.punctuation,
        ]
        sequence = ""
        for x in range(len(conditions)):
            # x variable here is the index
            if conditions[x]:
                sequence += possible_characters[x]
            else:
                pass
        return sequence

    @staticmethod
    # static method is a method that belongs to a class, not its instances
    def gen_password(sequence, passlength=8):
        password = "".join((secrets.choice(sequence)
                            for i in range(passlength)))
        return password


class Interface:
    has_characters = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True,
    }

    @classmethod
    # class method is a method that is bound to the class and not its instances
    def change_has_characters(cls, change):
        try:
            # to check if the specified key exists in the dicitonary
            cls.has_characters[change]
        except Exception as err:
            print(f"Invalid \nan Exception: {err}")
        else:
            # automaticly changes to the opposite value already there
            cls.has_characters[change] = not cls.has_characters[change]
            print(f"{change} is now set to {cls.has_characters[change]}")

    @classmethod
    def show_has_characters(cls):
        print(cls.has_characters)  # print the output

    def generate_password(self, length):
        sequence = PasswordGenerator.gen_sequence(
            list(self.has_characters.values()))
        print(PasswordGenerator.gen_password(sequence, length))


def list_to_vertical_string(list):
    to_return = ""
    for member in list:
        to_return += f"{member}\n"
    return to_return


class Run:
    def decide_operation(self):
        user_input = input(": ")
        try:
            int(user_input)
        except:
            Interface.change_has_characters(user_input)
        else:
            # exexcute code when there is no error
            Interface().generate_password(int(user_input))
        finally:
            print("\n\n")

    def run(self):
        menu = f"""Welcome to the Password Generator App!
Commands:
    generate password ->
    <length of the password>
    commands to change the characters to be used to generate passwords:
{list_to_vertical_string(Interface.has_characters.keys())}
                """
        print(menu)
        while True:
            self.decide_operation()


Run().run()
