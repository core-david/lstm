# LSTM

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

# Predicción con LSTM usando Kedro, MLflow y Docker  
**LSTM Forecasting with Kedro, MLflow, and Docker**

Este repositorio contiene la implementación de un modelo LSTM integrado en un pipeline estructurado con Kedro.  
This repository contains the implementation of an LSTM model integrated into a structured pipeline using Kedro.

Se utiliza MLflow para el seguimiento de ejecuciones y Docker con Docker Compose para facilitar la portabilidad y el almacenamiento de los experimentos.  
MLflow is used for experiment tracking, and Docker with Docker Compose provides portability and experiment storage.

---

## Objetivo del proyecto | Project Objective

Desarrollar una arquitectura reproducible y escalable para la predicción de series temporales con LSTM, aprovechando herramientas modernas de MLOps como Kedro y MLflow.  
To develop a reproducible and scalable architecture for time series forecasting using LSTM, leveraging modern MLOps tools like Kedro and MLflow.

---

## Tecnologías utilizadas | Technologies Used

- **Kedro**: Framework para estructurar proyectos de ciencia de datos.  
  *Framework for structuring data science projects.*

- **MLflow**: Seguimiento de ejecuciones, parámetros, métricas y artefactos.  
  *Experiment tracking: parameters, metrics, and artifacts.*

- **Docker + Docker Compose**: Contenerización y orquestación de servicios.  
  *Containerization and service orchestration.*

- **LSTM (Long Short-Term Memory)**: Red neuronal recurrente para series temporales usando Tensorflow.  
  *Recurrent neural network for time series using TensorFlow.*

---

## Estructura del proyecto | Project Structure

├── conf/ # Configuración del pipeline / Pipeline config
├── data/ # Datos en crudo y procesados / Raw & processed data
├── docs/ # Documentación del proyecto / Documentation
├── notebooks/ # Análisis exploratorio / EDA notebooks
├── src/ # Código fuente del pipeline / Source code
├── tests/ # Pruebas automatizadas / Unit tests
├── .gitignore # Exclusiones de Git / Git ignored files
├── docker-compose.yml # Servicios Docker / Docker services config
├── Dockerfile # Imagen base / Base Docker image
├── pyproject.toml # Configuración de Kedro / Kedro setup
├── requirements.txt # Dependencias / Python dependencies
├── README.md # Este archivo / This file
├── uv.lock # Lockfile de dependencias / Lockfile


---

## ⚙️ Instalación y ejecución local  
**Installation & Local Execution**

```bash
# Clonar el repositorio / Clone the repository
git clone https://github.com/youruser/project-name.git
cd project-name

# Crear y activar un entorno virtual / Create and activate virtual env
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalar dependencias / Install dependencies
pip install -r requirements.txt
uv sync

# Iniciar MLflow y PostgreSQL con Docker / Start MLflow and PostgreSQL
docker-compose up

# Ejecutar el pipeline / Run the Kedro pipeline
kedro run
```

## Visualización de resultados con MLflow  
**Results Visualization with MLflow**

Una vez iniciado Docker con `docker-compose up`, abre tu navegador y visita:  
Once Docker is up with `docker-compose up`, open your browser and go to: http://localhost:5000

Desde ahí podrás ver:  
From there, you can see:

- **Parámetros utilizados en cada experimento**  
  *Parameters used in each run*

- **Métricas obtenidas**  
  *Collected metrics*

- **Artefactos como modelos entrenados**  
  *Artifacts like trained models*

- **Comparación entre ejecuciones**  
  *Comparison between runs*

---

## Notas adicionales | Additional Notes

- **Los datos utilizados en este proyecto no se comparten públicamente por motivos de privacidad.**  
  *The data used in this project is not publicly shared due to privacy reasons.*

- **Puedes modificar hiperparámetros y rutas en `conf/base/`.**  
  *You can modify hyperparameters and paths in `conf/base/`.*


