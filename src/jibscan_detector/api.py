from typing import Protocol

class Detector(Protocol):
    def predict(self, image_uri: str) -> dict:
        """Return a DetectorPrediction-compatible mapping."""
        ...
