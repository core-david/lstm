from kedro.pipeline import Pipeline, node, pipeline
from .nodes import analyze_data, create_sequences, prepare_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=analyze_data,
            inputs="daily_data",
            outputs="daily_limpio",
            name="data_analysis.analizar_datos_node",
        ),
        node(
            func=create_sequences,
            inputs=["daily_limpio","params:time_step"],
            outputs=["X", "y"],
            name="data_analysis.crear_secuencias_node",
        ),
        node(
            func=prepare_data,
            inputs=["daily_limpio", "params:time_step", "params:test_size", "params:use_rolling"],
            outputs=["X_train", "X_test", "y_train", "y_test", "scaler", "target_column", "last_sequence"],
            name="data_analysis.preparar_datos_node",
        ),
    ])
