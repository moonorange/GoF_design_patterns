from abc import ABCMeta, abstractmethod

class Factory(metaclass=ABCMeta):
    def get_factory(self, class_name: str):
        try:
            factory = globals()[class_name]()
        except NameError:
            print("Can't find class {}".format(class_name))
        except Exception as e:
            print(e)

        return factory

    @abstractmethod
    def create_link(self, caption: str, url: str):
        pass

    @abstractmethod
    def create_tray(self, caption: str):
        pass

    @abstractmethod
    def create_page(self, title: str, author: str):
        pass
