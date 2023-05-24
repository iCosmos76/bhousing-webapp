from typing import Any, List, Optional

from bhousing_model.processing.validation import BHousingInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[float]]


class MultipleBHousingInputs(BaseModel):
    inputs: List[BHousingInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "ID": 7,
                        "CRIM": 0.08829,
                        "ZN": 12.5,
                        "INDUS": 7.87,
                        "CHAS": 0.0,
                        "NOX": 0.524,
                        "RM": 6.012,
                        "AGE": 66.6,
                        "DIS": 5.5605,
                        "RAD": 5.0,
                        "TAX": 311.0,
                        "PTRATIO": 15.2,
                        "B": 395.6,
                        "LSTAT": 12.43,
                    }
                ]
            }
        }
