from abc import ABCMeta, abstractmethod

def main():
    pb = PrintBanner("Hello")
    pb.print_weak()
    pb.print_strong()

class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print("({})".format(self.__string))

    def show_with_aster(self):
        print("*{}*".format(self.__string))

class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass    

    @abstractmethod
    def print_strong(self):
        pass

class PrintBanner(Banner, Print):
    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()

if __name__ == '__main__':
    main()
