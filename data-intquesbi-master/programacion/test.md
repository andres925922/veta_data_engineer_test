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
