from abc import ABCMeta, abstractmethod
import unicodedata

def main():
    ch = CharDisplay("a")
    ch.display()
    st = StringDisplay("hello")
    st.display()
    st_jp = StringDisplay("こんにちは")
    st_jp.display()

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def pprint(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()

        for _ in range(5):
            self.pprint()

        self.close()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch:str):
        self.__ch = ch

    def open(self):
        print("<<", end="")

    def pprint(self):
        print(self.__ch, end="")

    def close(self):
        print(">>")

class StringDisplay(AbstractDisplay):
    def __init__(self, string:str):
        self.__string = string
        self.__width = self.get_east_asian_width_count(self.__string)

    def open(self):
        self.__print_line()

    def pprint(self):
        print("|" + self.__string + "|")

    def close(self):
        self.__print_line()

    def get_east_asian_width_count(self, text):
        count = 0
        for c in text:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count

    def __print_line(self):
        print("+", end="")

        for _ in range(self.__width):
            print("-", end="")

        print("+")

if __name__ == '__main__':
    main()
