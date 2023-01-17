# Hotel-Reservation-Predictor

Project for prediction if someone will cancel its hotel reservation or not

## How To Use

For a simple way to use hotel reservation predictor, you have to install Docker and then, run the following command line in the same project folder root

```
docker compose up
```

After, you can consume the API in localhost with port 8000, also you can edit this port by changing it in Dockerfile

## API JSON Structure

The structure of JSON input for API is the following

```
{
    "no_of_adults":2,
    "no_of_weekend_nights":1,
    "no_of_week_nights":2,
    "type_of_meal_plan":"Meal Plan 1",
    "room_type_reserved":"Room_Type 1",
    "lead_time":224,
    "arrival_year":2017,
    "arrival_month":10,
    "arrival_date":2,
    "market_segment_type":"Offline",
    "avg_price_per_room":65.0,
    "no_of_special_requests":0
}
```
This is an example of API input structure, on the other hand the output is 0 or 1, 0 represent that user probably won't cancel his reservation and 1 represent that user probably will cancel his reservation 
