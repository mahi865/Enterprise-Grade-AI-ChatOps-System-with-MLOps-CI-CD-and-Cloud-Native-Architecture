import logging
import sentry_sdk

sentry_sdk.init(dsn="your_sentry_dsn")

def log_request_metrics(message: str, intent: str):
    logging.info(f"User Message: {message} | Intent: {intent}")
    try:
        # Placeholder for sending metrics to Prometheus, etc.
        pass
    except Exception as e:
        sentry_sdk.capture_exception(e)
