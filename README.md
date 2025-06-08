# LSTM 

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
[![Powered by MLflow](https://img.shields.io/badge/MLflow-tracking-0172b2?logo=mlflow)](https://mlflow.org/)
[![Powered by TensorFlow](https://img.shields.io/badge/Built%20with-TensorFlow-orange?logo=tensorflow)](https://www.tensorflow.org/)
[![Powered by Docker](https://img.shields.io/badge/Containerized%20with-Docker-2496ed?logo=docker)](https://www.docker.com/)


This repository contains the implementation of an LSTM model integrated into a structured pipeline using Kedro.  
Este repositorio contiene la implementación de un modelo LSTM integrado en un pipeline estructurado con Kedro.

MLflow is used for experiment tracking, including model versions, metrics, and artifacts. Docker and Docker Compose provide portability and persistent experiment storage.  
Se utiliza MLflow para el seguimiento de experimentos, incluyendo versiones del modelo, métricas y artefactos. Docker y Docker Compose facilitan la portabilidad y el almacenamiento persistente de los experimentos.

---

## Project Objective | Objetivo del Proyecto

To develop a reproducible and scalable architecture for time series forecasting using LSTM, leveraging modern MLOps tools like Kedro and MLflow.  
Desarrollar una arquitectura reproducible y escalable para la predicción de series temporales con LSTM, aprovechando herramientas modernas de MLOps como Kedro y MLflow.

---

## Technologies Used | Tecnologías Utilizadas

- **Kedro**: Framework for structuring data science projects.  
  *Framework para estructurar proyectos de ciencia de datos.*

- **MLflow**: Experiment tracking for parameters, metrics, and model artifacts.  
  *Seguimiento de parámetros, métricas y artefactos de modelos.*

- **Docker + Docker Compose**: Containerization and service orchestration.  
  *Contenerización y orquestación de servicios.*

- **LSTM (Long Short-Term Memory)**: Recurrent neural network for time series using TensorFlow.  
  *Red neuronal recurrente para series temporales usando TensorFlow.*

---

## ⚙️ Installation & Local Execution | Instalación y Ejecución Local

```bash
# Clone the repository / Clonar el repositorio
git clone https://github.com/youruser/project-name.git
cd project-name

# Create and activate virtual environment / Crear y activar entorno virtual
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies / Instalar dependencias
pip install -r requirements.txt
uv sync

# Start MLflow and PostgreSQL / Iniciar MLflow y PostgreSQL
docker-compose up

# Run Kedro pipeline / Ejecutar pipeline de Kedro
kedro run
```

## Results Visualization with MLflow | Visualización de Resultados con MLflow

Once Docker is up with `docker-compose up`, open your browser and go to:  
**Una vez iniciado Docker con `docker-compose up`, abre tu navegador y visita:**  
[http://localhost:5000](http://localhost:5000)

You will be able to explore:  
**Podrás visualizar:**

- **Parameters used in each run**  
  *Parámetros utilizados en cada experimento*

- **Collected metrics**  
  *Métricas obtenidas*

- **Artifacts like trained models**  
  *Artefactos como modelos entrenados*

- **Comparison between executions**  
  *Comparación entre ejecuciones*

All results are stored and versioned in MLflow. | Todos los resultados se almacenan y versionan en MLflow.

---

## Additional Notes | Notas Adicionales

- **The data used in this project is not publicly shared due to privacy reasons.**  
  *Los datos utilizados en este proyecto no se comparten públicamente por motivos de privacidad.*

- **You can modify hyperparameters and paths in `conf/base/`.**  
  *Puedes modificar hiperparámetros y rutas en `conf/base/`.*


