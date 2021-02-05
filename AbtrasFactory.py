from __future__ import annotations #Imp libreerias
from abc import ABC, abstractmethod #imp libr


class AbstractFactory(ABC): #Clase abstracta q devuelve metodos abst ( para q sirve self

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):#sub clase


    def create_product_a(self) -> AbstractProductA: ##deef metodo
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):#sub clase para otra familia


    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):#llama a la libreria, metodo abst


    @abstractmethod
    def useful_function_a(self) -> str:#metod para devolver cadena
        pass


class ConcreteProductA1(AbstractProductA):#presenta datos
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):#metodos abstractos self sirve para acceder a los metodos y atributos de esa class

    @abstractmethod
    def useful_function_b(self) -> None:

        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:

        pass




class ConcreteProductB1(AbstractProductB):#crea metodos funcions de las familias para acceder a los metodos y clases
    def useful_function_b(self) -> str:
        return "The result of the product B1."



    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):

        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:

    product_a = factory.create_product_a() #crea un objeto en este caso un product de cada familia
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":#declara el main
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())#productos de familia 1 y 2

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())