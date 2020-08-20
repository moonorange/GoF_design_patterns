from abc import ABCMeta, abstractmethod

def main():
    # ch = CharDisplay("a")
    # ch.display()
    st = StringDisplay("hello")
    st.display()

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch:str) -> str:
        self.__ch = ch

    def open(self):
        print("<<", end="")

    def print(self):
        print(self.__ch, end="")

    def close(self):
        print(">>")

class StringDisplay(AbstractDisplay):
    def __init__(self, string:str):
        self.__string = string
        self.__width = len(self.__string)

    def open(self):
        self.__print_line()

    def print(self):
        print("|" + self.__string + "|")

    def close(self):
        self.__print_line()

    def __print_line(self):
        print("+", end="")
        for i in range(self.__width):
            print("-", end="")
        print("+")

if __name__ == '__main__':
    main()
