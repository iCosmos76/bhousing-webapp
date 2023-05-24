import pandas as pd
from fastapi.testclient import TestClient

import random

import json

def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.to_dict(orient="records")
    }

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )


    print(payload)

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    print(prediction_data)
    assert all(isinstance(x, float) for x in prediction_data["preds"])
    assert prediction_data["errors"] is None
