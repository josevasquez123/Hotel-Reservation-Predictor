from pydantic import BaseModel

class ModelInput(BaseModel):
    no_of_adults: int
    no_of_weekend_nights:int
    no_of_week_nights:int
    type_of_meal_plan:str
    room_type_reserved:str
    lead_time:int
    arrival_year:int
    arrival_month:int
    arrival_date:int
    market_segment_type:str
    avg_price_per_room:float
    no_of_special_requests:int