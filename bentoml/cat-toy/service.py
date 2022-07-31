import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON

model = bentoml.sklearn.get("cat_toy:latest").to_runner()

cat_toy_ranking = bentoml.Service("cat_toy_ranking", runners=[model])


@cat_toy_ranking.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = model.predict.run(input_series)
    return result


@cat_toy_ranking.api(input=JSON(), output=JSON())
def jclassify(input_series: str) -> str:
    return "{[1]}"
