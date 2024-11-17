
import pandas as pd
import random
import time

# Generate synthetic transaction data
def generate_synthetic_data(output_file='transactions.csv', num_records=10000):
    data = [
        {
            "transaction_id": i,
            "customer_id": random.randint(1, 500),
            "merchant_id": random.randint(1, 100),
            "amount": round(random.uniform(1.0, 500.0), 2),
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6),
            "timestamp": time.time() - random.randint(0, 100000),
        }
        for i in range(num_records)
    ]
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Generated {num_records} records and saved to {output_file}")

# Run the function if executed directly
if __name__ == "__main__":
    generate_synthetic_data()
