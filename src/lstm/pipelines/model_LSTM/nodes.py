# src/lstm/pipelines/model_LSTM/nodes.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

def build_model_node(input_shape):
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.3),
        LSTM(32, return_sequences=True),
        Dropout(0.3),
        LSTM(16),
        Dropout(0.2),
        Dense(8, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
    return model


def train_model_node(model, X_train, y_train, X_test, y_test):
    callbacks = [
        EarlyStopping(patience=15, restore_best_weights=True),
        ReduceLROnPlateau(patience=7, factor=0.5, min_lr=1e-7)
    ]
    model.fit(
        X_train,
        y_train,
        epochs=100,
        batch_size=32,
        validation_data=(X_test, y_test),
        callbacks=callbacks,
        verbose=1
    )
    return model


def evaluate_model_node(model, X_test, y_test, scaler):
    predictions = model.predict(X_test)
    y_test_real = scaler.inverse_transform(y_test.reshape(-1, 1))
    predictions_real = scaler.inverse_transform(predictions)
    mae = mean_absolute_error(y_test_real, predictions_real)
    rmse = np.sqrt(mean_squared_error(y_test_real, predictions_real))
    r2 = r2_score(y_test_real, predictions_real)
    print(f"MAE: {mae}, RMSE: {rmse}, R2: {r2}")
    return predictions_real, y_test_real, mae, rmse, r2


def predict_future_node(model, scaler, last_sequence, n_periods):
    predictions = []
    current_seq = np.array(last_sequence).copy()

    for _ in range(n_periods):
        pred = model.predict(current_seq.reshape(1, -1, 1), verbose=0)
        predictions.append(pred[0, 0])
        current_seq = np.append(current_seq[1:], pred[0, 0])

    return scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()




def visualizar_resultados(df_daily, predictions_real, y_test_real, time_step, target_column, future_predictions):
    fig, ax = plt.subplots(figsize=(15, 10))  # Create figure and axes objects
    
    ax.plot(df_daily.index, df_daily['ocupacion_total'], label='Ocupación Original', alpha=0.5)

    if 'ocupacion_rolling_7d' in df_daily.columns:
        ax.plot(df_daily.index, df_daily['ocupacion_rolling_7d'], label='Rolling 7 días', color='green')

    start_test_idx = len(df_daily) - len(y_test_real) - 1
    test_dates = df_daily.index[start_test_idx:start_test_idx + len(y_test_real)]
    ax.plot(test_dates, y_test_real, label='Valores Reales (Rolling 7d)', color='darkgreen')
    ax.plot(test_dates, predictions_real, label='Predicciones LSTM', color='red')

    if future_predictions is not None:
        future_dates = pd.date_range(start=df_daily.index.max() + pd.Timedelta(days=1),
                                     periods=len(future_predictions), freq='D')
        ax.plot(future_dates, future_predictions, label='Futuro', color='orange', linestyle='--')

    ax.set_title(f'Predicción LSTM usando {target_column}')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Ocupación')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    
    return fig  # Now fig is properly defined


def get_input_shape(X_train):
    return (X_train.shape[1], 1)  # LSTM espera forma (timesteps, features)
