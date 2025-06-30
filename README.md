## Descripción del Modelo de Conversión de Temperatura

Este proyecto utiliza un modelo de **TensorFlow** entrenado para convertir temperaturas de **Celsius** a **Fahrenheit**. El modelo fue creado y entrenado para recibir una temperatura en grados Celsius como entrada y devolver la temperatura equivalente en grados Fahrenheit como salida.

### Funcionamiento

1. **Entrada**: El modelo recibe una temperatura en **Celsius** como entrada a través de una solicitud **POST** enviada a la API de Django.
   
2. **Procesamiento**: El modelo utiliza una red neuronal **`Dense`** de **TensorFlow Keras** para realizar la conversión, basándose en la relación matemática que existe entre estas dos unidades de temperatura. El modelo fue entrenado con un conjunto de datos que abarca un rango de temperaturas de Celsius a Fahrenheit.

3. **Salida**: El modelo devuelve el valor convertido a **Fahrenheit** como salida en formato JSON. Por ejemplo, si la entrada es **25°C**, la salida será **77°F**.

### Función de la API

La API expone un único endpoint:

- **POST /api/convertir_temperatura/**: Recibe un objeto JSON con la temperatura en **Celsius** y devuelve un objeto JSON con la temperatura convertida a **Fahrenheit**.

### Ejemplo de uso

#### Solicitud:

```json
{
    "celsius": 25
}
```
#### Respuesta:

```json
{
    "celsius": 25,
    "fahrenheit": 76.87620544433594
}
```
### **Descripción del modelo**:

- **Modelo entrenado**: El modelo de **TensorFlow** fue entrenado utilizando un conjunto de datos simple con pares de valores de temperaturas en Celsius y Fahrenheit. Esta red neuronal **`Dense`** tiene una capa de salida que realiza la conversión.
- **Uso práctico**: Aunque la conversión de Celsius a Fahrenheit es una operación matemática sencilla, este modelo demuestra cómo se puede integrar un modelo de **TensorFlow** en un sistema backend para realizar predicciones, incluso con tareas simples como esta.


### **Libreria a instalar**
ver https://www.tensorflow.org/install?hl=es-419
```console
pip install tensorflow
```

