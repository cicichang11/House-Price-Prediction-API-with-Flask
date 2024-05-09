from fastapi import FastAPI
from pydantic import BaseModel
import dill
import pandas as pd
from utils import Preprocessor

# Create api
app = FastAPI()

# Load GB Model
with open('gb.pkl', 'rb') as f: 
    model = dill.load(f) 

# Type checking class through Pydantic
class ScoringItem(BaseModel): 
    TransactionDate: str
    HouseAge: float
    DistanceToStation: float
    NumberOfPubs: float
    PostCode: str 

@app.post('/')
async def scoring_endpoint(item:ScoringItem): 
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat = model.predict(df)
    return {"prediction":int(yhat)}