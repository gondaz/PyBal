"""
metrics.py

Metrics class implementations for PyBal
"""

try:
    import prometheus_client
    metrics_implementation = 'prometheus'
except ImportError:
    metrics_implementation = 'dummy'

class DummyMetric(object):
    def __init__(self, *args, **kwargs):
        pass

    def labels(self, **kwargs):
        return self

class DummyCounter(DummyMetric):
    def inc(self, *args, **kwargs):
        pass

class DummyGauge(DummyMetric):
    def set(self, *args, **kwargs):
        pass

if metrics_implementation == 'prometheus':
    Counter = prometheus_client.Counter
    Gauge = prometheus_client.Gauge
else:
    Counter = DummyCounter
    Gauge = DummyGauge
