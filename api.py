from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import pandas as pd
import uvicorn



class ClimateIndicator(BaseModel):
    year: float
    country_name: str
    indicator_name: str
    unit: str


class ClimateSector(BaseModel):
    year: float
    country_name: str
    sector_name: str
    unit: str   

df = pd.read_csv('test.csv')




# --- FastAPI Endpoints ---

app = FastAPI(
    title="Climate Finance Data API",
    version="1.0.0",
    description="API for querying Climate Finance data.",
)

#response_model=List[ClimateSector]
#response_model=List[ClimateIndicator]
@app.get("/sector", )
async def getSectorResponse(
    country:str = Query(None, description="Filter by Country"),
    sector : str = Query(None, description="Filter by Sector")):

    """Retrieve all sector response records"""
    df_temp = df.groupby(['Country','Sector','Unit'])[['2005',
       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
       '2015', '2016', '2017', '2018', '2022']].sum().reset_index()


    if country:
        df_temp = df_temp[df_temp['Country']==country]

    if sector:
        df_temp = df_temp[ddf_tempf['Sector']==sector]

    

    return df_temp[:500].to_dict('records')


@app.get("/indicator", )
async def getIndicatorResponse(
    country:str = Query(None, description="Filter by Country"),
    indicator : str = Query(None, description="Filter by Sector")):

    """Retrieve all sector response records"""
    df_temp = df.groupby(['Country','Indicator','Unit'])[['2005',
       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
       '2015', '2016', '2017', '2018', '2022']].sum().reset_index()


    if country:
        df_temp = df_temp[df_temp['Country']==country]

    if indicator:
        df_temp = df_temp[df_temp['Indicator']==indicator]

    

    return df_temp[:500].to_dict('records')


if __name__ == "__main__":
    uvicorn.run("api_:app", port=5000, log_level="info",reload=True)