from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    get_input_shape,  # 👈 agrega esta línea
    build_model_node,
    train_model_node,
    evaluate_model_node,
    predict_future_node,
    visualizar_resultados,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=get_input_shape,
            inputs="X_train",
            outputs="input_shape",
            name="model_LSTM.get_input_shape_node"
        ),
        node(
            func=build_model_node,
            inputs="input_shape",
            outputs="lstm_model",
            name="model_LSTM.build_model_node"
        ),
        node(
            func=train_model_node,
            inputs=dict(
                model="lstm_model",
                X_train="X_train",
                y_train="y_train",
                X_test="X_test",
                y_test="y_test"
            ),
            outputs="trained_model",
            name="model_LSTM.train_model_node"
        ),
        node(
            func=evaluate_model_node,
            inputs=dict(
                model="trained_model",
                X_test="X_test",
                y_test="y_test",
                scaler="scaler"
            ),
            outputs=["predictions_real", "y_test_real", "mae", "rmse", "r2"],
            name="model_LSTM.evaluate_model_node"
        ),
        node(
            func=predict_future_node,
            inputs=dict(
                model="trained_model",
                scaler="scaler",
                last_sequence="last_sequence",
                n_periods="params:n_periods"
            ),
            outputs="future_predictions",
            name="model_LSTM.predict_future_node"
        ),
        node(
            func=visualizar_resultados,
            inputs=dict(
                df_daily="daily_limpio",
                predictions_real="predictions_real",
                y_test_real="y_test_real",
                time_step="params:time_step",
                target_column="target_column",
                future_predictions="future_predictions"
            ),
            outputs="evaluation_plot",
            name="model_LSTM.visualizar_resultados_node"
        )
    ])
