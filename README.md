# Win or FF un proyecto semestral de ingeniería de datos

**Autores:** Lorenzo Lopez, Eloy Prado

## Descripción General
Este proyecto de Ingeniería de Datos busca desarrollar un modelo predictivo de clasificación binaria para determinar el equipo ganador en una partida competitiva de *League of Legends*, utilizando exclusivamente la información estadística disponible durante los primeros 10 minutos de juego.

## Planteamiento del Problema
En partidas competitivas de *League of Legends*, los jugadores y equipos suelen tomar decisiones estratégicas críticas durante el *early game* (juego temprano) basándose principalmente en la intuición o en percepciones subjetivas de ventaja (como iniciar una votación de rendición temprana o forzar peleas grupales en desventaja). 

Actualmente, existe la necesidad de identificar con precisión matemática qué ventajas concretas obtenidas en esta etapa temprana definen realmente el resultado final de la partida. La falta de claridad sobre el peso real de acciones específicas (como el control de visión versus la ventaja de oro o la captura de objetivos neutrales) dificulta la optimización en la toma de decisiones para maximizar la probabilidad de victoria.

## Instrucciones Generales de Ejecución
Pre-requisitos:
* Tener Python 3.x instalado
* Descomprimir el archivo **high_diamond_ranked_10min.csv.zip** de modo que el archivo CSV quede ubicado exactamente en la ruta **Script/high_diamond_ranked_10min/** para que el código pueda leerlo.
* Contar con una terminal de comandos (PowerShell, CMD o bash) abierta en el directorio raíz del repositorio.

Para ejecutar tanto el código de Python en el directorio **Script** y el contenido del Notebook en el directorio **Notebook** se recomienda utilizar VENV, para lo cual tendrá que abrir una terminal en el directorio raíz del proyecto y ejecutar lo siguiente:

1. **python -m venv env** Este comando crea el ambiente de Python y este ambiente tendrá el nombre **env**.
2. **.\env\Scripts\activate** Este comando inicializa el ambiente de Python y aparecerá en la terminal como que está escribiendo comandos en **(env)** con el resto de la dirección del directorio.
3. **pip install -r .\Script\requirements.txt** Este comando instala todas las librerías necesarias en el ambiente **env** para utilizarlas en el proyecto.
4. Ahora se puede ejecutar el código Python en el directorio **Script** y/o el notebook en el directorio **Notebook**
5. Al terminar se puede cerrar la terminal y se cierra el ambiente o se puede usar el comando **deactivate**

## Instrucciones de Ejecución de Script
Los script de Python en el directorio **Script** no se pueden ejecutar en cualquier orden por lo que si desea correr el código fuente desde la terminal, tendrá que ejecutar los siguientes comandos:

1. **python .\Script\dataFrameMakers\testAndTrainingSetMAker.py** Este script prepara y divide los datos en conjuntos de entrenamiento y prueba generando archivos de cada conjunto.
2. **python .\Script\entrenamiento.py** Este script entrena el modelo Random Forest y genera un archivo con dicho modelo.
3. **python .\Script\testeo.py** Este script evalúa el modelo generado y muestra las métricas de precisión, recall y accuracy.

## Instrucciones de Ejecución de Notebook

### Para Visual Studio Code
Pre-requisitos:
* Instalar extensión oficial de Jupyter Notebook

Para utilizar el Notebook de Jupyter, al abrir el archivo **.ipynb** por primera vez deberá dirigirse a la sección de escoger **Kernel**. Es de suma importancia que seleccione el ambiente VENV llamado **env** que se creó en las instrucciones generales. Una vez hecho esto el Notebook se podrá ejecutar con regularidad sin necesidad de configurar nada más.
