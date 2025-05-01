import os
from mlflow import start_run, log_metric, log_params
from subprocess import run

def retrain_model():
    with start_run():
        log_params({"trigger": "auto"})
        try:
            result = run(["bash", "retraining/retrain.sh"], check=True)
            log_metric("status", 1)
        except Exception as e:
            log_metric("status", 0)
            print(f"Retrain failed: {e}")
