from pydantic import BaseModel

class Data(BaseModel):
    gravity:float
    ph:float
    cond:float
    calc:float
    osmo:int
    urea:int
    """oxalate_concentration:float
    calc_to_oxalate_ratio:float
    ion_balance:float
    sg_to_osmo_ratio:float
    urea_to_creatinine_ratio:float
    pH_balance:int
    osmo_to_cond_ratio:float"""
