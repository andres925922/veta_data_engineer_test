"""
## Programación

Escribe en el código que consideres soluciones a los siguientes problemas

**1) Clases**. Escribe las clases que mejor solucionan lo siguiente:
* Dentro de un instituto hay alumnos y profesores 
* Queremos tener el nombre de los alumnos
* Queremos tener el nombre de los profesores
* Queremos tener el curso de los alumnos donde están matriculados

A continuación, se muestra una posible solución

```Java
public class Alumno {
    private String nombre:
    private int curso;
}
public class Profesor {
    private String nombre:    
}
```
Mejora esta solución adoptada usando herencia

**2) POO**. Ten en cuenta el siguiente código escrito en Java

```Java
public class Jugador {
  private Arma arma;
  private String nombre;

  public Jugador(String nombre, Arma arma) {
    this.nombre = nombre;
    this.arma = arma;
  }

  public void setArma(Arma arma) {
    this.arma = arma;
  }

  public void action() {
    if (this.arma.type == "cuchillo") {
      System.out.println("Ataca con el cuchillo");
    } else {
      if (this.arma.type == "revolver") {
        System.out.println("Ataca con el revolver");
      } else {
        if (this.arma.type == "plasma") {
          System.out.println("ataca con plasma");
        }
      }
    }
  }
}
```

Crea un nuevo diseño de clases si es preciso para resolver unos de los principios SOLID que se está violando

<br/>



"""
class Persona():

    def __init__(self, nombre, apellido) -> None:
        self.__nombre = nombre
        self.__apellido = apellido

    def get_alumno(self) -> str:
        return self.__nombre + " " + self.__apellido
    
class Curso():
    def __init__(self, nombre, id) -> None:
        self.__nombre = nombre
        self.__id = id

class Alumno(Persona):

    def __init__(self, nombre, apellido) -> None:
        super().__init__(self, nombre, apellido)
        self.__curso: list[Curso] = []

    def get_curso(self):
        return self.__apellido
    
    def agregar_curso(self, nuevo_curso: Curso):
        self.__curso.append(nuevo_curso)

    def eliminar_curso(self, curso):
        self.__curso.remove(curso)

class Profesor(Persona):

    def __init__(self, nombre, apellido) -> None:
        super().__init__(self, nombre, apellido)





# Ejercicio 2

class Arma:
    """
    Clase padre de arma que heredan los otros tipos de armas
    """

    def __init__(self, tipo: str) -> None:
        self.__type = tipo

    
    def return_arma_type(self):
        return self.__type
    
    def atacar(self):
        return f"Ataca con {self.__type}"
    

class Cuchillo(Arma):

    def __init__(self) -> None:
        super().__init__("cuchillo")


class Revolver(Arma):

    def __init__(self) -> None:
        super().__init__("revolver")

class Plasma(Arma):

    def __init__(self) -> None:
        super().__init__("plasma")


class Jugador:

    """
    Clase jugador con nombre y arma privados que toma un arma por parámetro y en función del tipo de arma el comportamiento está seteado.

    """

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    def action(self) -> None:
        print(self.__arma.atacar())

    def set_arma(self, arma: Arma) -> None:
        self.__arma = arma

