from prometheus_client import start_http_server, Counter

# Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
ERROR_COUNT = Counter('error_count', 'Total number of errors')

def start_monitoring_server():
    """
    Start a Prometheus HTTP server for metrics.
    """
    start_http_server(8000)