# Infraestructuras Virtuales

## Sobre el proyecto

La mayoría de personas tiene unas cuantas imágenes que le gustaría usar de fondo de escritorio. Sin embargo, éstas suelen acabar en una carpeta amontonadas, con nombres aleatorios. ¿No sería estupendo si pudieramos clasificarlas automáticamente? Es más: ¿y si aumentáramos la calidad a la misma vez?

## ¿Qué es Vin?

*Variant Image Network* es una aplicación desarrollada en Python que permite clasificar fondos de escritorio basándose en el contenido presente en éstas. Utiliza KNN por debajo para conseguirlo.

**Este proyecto todavía no está listo para su uso.**

## Documentación

Visita la carpeta [docs](./docs) para conocer más información.

## Contenedor

Para pasar los test, se puede utilizar el contenedor publicado en Dockerhub. Para ello, simplemente ejecútalo y automáticametne deberían dispararse.

Está basado en la imagen oficial de Python.

### Guía de uso

> poetry run check, poetry run test

Para ejecutar la aplicación, ejecuta la orden

```
poetry run vin
```

Para pasar los tests,
```
poetry run task test
```

Para comprobar la sintaxis,
```
poetry run task check
```