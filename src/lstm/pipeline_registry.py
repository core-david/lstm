from kedro.pipeline import Pipeline
from lstm.pipelines.cleaning2 import pipeline as cleaning2_pipeline
from lstm.pipelines.preprocessing import pipeline as preprocessing_pipeline
from lstm.pipelines.model_LSTM import pipeline as model_lstm_pipeline
from lstm.pipelines.data_analysis import pipeline as data_analysis_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "cleaning2": cleaning2_pipeline.create_pipeline(),
        "preprocessing": preprocessing_pipeline.create_pipeline(),
        "data_analysis": data_analysis_pipeline.create_pipeline(),
        "modeling": model_lstm_pipeline.create_pipeline(),
       "__default__": (
            cleaning2_pipeline.create_pipeline()
            + preprocessing_pipeline.create_pipeline()
            + data_analysis_pipeline.create_pipeline()
            + model_lstm_pipeline.create_pipeline()
        )
    }
