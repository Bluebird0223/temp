import dlt
import requests
import os

FLASK_API_URL = os.getenv("FLASK_API_URL", "http://mock-server:5000/api/customers")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@postgres:5432/customer_db")

@dlt.resource(name="customers", write_disposition="merge", primary_key="customer_id")
def fetch_customers():
    page = 1
    limit = 10
    while True:
        response = requests.get(f"{FLASK_API_URL}?page={page}&limit={limit}")
        response.raise_for_status()
        data = response.json()
        
        customers = data.get("data", [])
        if not customers:
            break
            
        yield customers
        
        if len(customers) < limit:
            break
        
        page += 1

def run_ingestion():
    pipeline = dlt.pipeline(
        pipeline_name="customer_ingestion",
        destination="postgres",
        dataset_name="public",
        credentials=DATABASE_URL
    )
    
    info = pipeline.run(fetch_customers())
    return info
