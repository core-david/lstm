# kedro_lstm_pipeline/src/lstm/pipelines/data_analysis/nodes.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple


def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    # Asegura que la columna 'ds' es datetime y úsala como índice
    df['ds'] = pd.to_datetime(df['ds'])
    df.set_index('ds', inplace=True)

    # Limpieza e imputación de valores faltantes
    if df['ocupacion_total'].isnull().sum() > 0:
        df['ocupacion_total'] = df['ocupacion_total'].interpolate()

    df['ocupacion_rolling_7d'] = (
        df['ocupacion_total']
        .rolling(window=7, center=True)
        .mean()
        .bfill()
        .ffill()
    )

    return df

def create_sequences(df: pd.DataFrame, time_step: int) -> Tuple[np.ndarray, np.ndarray]:
    data = df[['ocupacion_rolling_7d']].values  # 👈 convertir a array NumPy
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

def prepare_data(df: pd.DataFrame, time_step: int, test_size: float, use_rolling: bool):
    # Usa 'ocupacion_rolling_7d' si está disponible
    column = 'ocupacion_rolling_7d' if use_rolling else 'ocupacion_total'

    scaler = MinMaxScaler()
    data = scaler.fit_transform(df[[column]])

    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    X, y = np.array(X), np.array(y)

    split_idx = int(len(X) * (1 - test_size))
    last_sequence = data[-time_step:].flatten()
    return (
        X[:split_idx],
        X[split_idx:],
        y[:split_idx],
        y[split_idx:],
        scaler,
        column,
        last_sequence  # 👈 nueva salida
    )

