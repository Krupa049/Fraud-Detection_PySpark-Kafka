# **Real-Time Fraud Detection System**

## **Overview**
This project demonstrates a **real-time fraud detection system** built using **PySpark**. The system ingests, processes, and analyzes transactional data to detect potentially fraudulent activities. It leverages **streaming data processing**, **feature engineering**, and **unsupervised machine learning** to flag anomalies in financial transactions.

The repository is designed to help you understand and implement a scalable, end-to-end data pipeline with PySpark for real-world applications.

---

## **Key Features**
- **Real-Time Data Ingestion**: Simulates transactional data using streaming platforms like Kafka.
- **Data Preprocessing**: Cleans and enriches data, including handling missing values and outliers.
- **Feature Engineering**: Generates meaningful metrics such as transaction velocity and rolling averages.
- **Anomaly Detection**: Uses KMeans clustering for unsupervised detection of anomalous transactions.
- **Result Persistence**: Saves flagged transactions to CSV for further analysis.
- **Scalability**: Designed to handle large-scale, real-time transactional data.

---

## **Tech Stack**
- **Apache PySpark**: Distributed data processing and machine learning.
- **Google Colab**: Development environment for building and testing the pipeline.
- **Python**: For feature engineering, data simulation, and custom logic.
- **Apache Kafka** (optional): For simulating real-time data ingestion.
- **Pandas**: For generating and saving synthetic data.
- **Matplotlib** (optional): For visualizing results and transaction patterns.

---

## **System Architecture**
1. **Data Ingestion**:
   - Simulates transactional data using Python.
   - Streams data using Apache Kafka or processes static data from a CSV file.

2. **Data Preprocessing**:
   - Cleans data (e.g., handles missing values).
   - Converts timestamps into human-readable formats.
   - Generates derived features such as transaction velocity and rolling averages.

3. **Anomaly Detection**:
   - Uses `VectorAssembler` to create feature vectors.
   - Applies KMeans clustering to group transactions into normal and suspicious clusters.

4. **Result Persistence**:
   - Saves suspicious transactions into a CSV file for further analysis.
   - Provides easy export for integration with dashboards or external analysis tools.

---

## **Installation and Setup**
Follow these steps to set up the project on your local environment or Google Colab.

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/real-time-fraud-detection.git
cd real-time-fraud-detection
```

### **2. Install Dependencies**
Ensure the following libraries are installed:
- **Required Libraries**:
  - `pyspark`
  - `findspark`
  - `pandas`
  - `matplotlib`

Install them using:
```bash
pip install pyspark findspark pandas matplotlib
```

If you're using **Google Colab**, set up the environment as follows:
```python
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!pip install pyspark findspark pandas matplotlib
```

### **3. Set Up PySpark**
Initialize PySpark in your environment:
```python
import findspark
findspark.init()
```

### **4. Environment Requirements**
- **Operating System**: Linux/MacOS/Windows (or Colab for cloud execution).
- **Python Version**: 3.7 or higher.
- **Java Version**: OpenJDK 8 or later (required for PySpark).
- **Apache Spark Version**: Spark 3.0 or later.

---

## **Usage**

### **1. Generate Synthetic Data**
The project includes a script to generate synthetic transactional data:
```python
data = [
    {
        "transaction_id": i,
        "customer_id": random.randint(1, 500),
        "merchant_id": random.randint(1, 100),
        "amount": random.uniform(1.0, 500.0),
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180, 180),
        "timestamp": time.time() - random.randint(0, 100000),
    }
    for i in range(10000)
]
```

### **2. Process Data in PySpark**
Run the PySpark pipeline to:
1. Load and preprocess the data.
2. Generate features like `transaction_velocity` and `avg_amount`.
3. Apply KMeans clustering to detect anomalies.

### **3. Save Results**
Flagged transactions are saved in `suspicious_transactions.csv`:
```python
suspicious_transactions.write.csv("suspicious_transactions.csv", mode="overwrite", header=True)
```

---

## **Project Files**
| File Name                  | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `generate_data.py`         | Script to generate synthetic transactional data.                           |
| `pyspark_pipeline.py`      | Main PySpark pipeline for preprocessing, feature engineering, and modeling.|
| `requirements.txt`         | List of required Python libraries for the project.                        |
| `README.md`                | Documentation for the repository.                                         |

---

## **How It Works**

### **Step 1: Data Preprocessing**
- Cleans raw transaction data.
- Converts timestamps into readable formats.
- Calculates derived features like `transaction_velocity` and `avg_amount`.

### **Step 2: Feature Engineering**
- Combines numerical columns into a vector using `VectorAssembler`.
- Prepares data for machine learning models.

### **Step 3: Anomaly Detection**
- Trains a KMeans model with `k=2` to cluster transactions into normal and anomalous groups.
- Assigns a cluster label (`prediction`) to each transaction.

---

## **Example Output**
| transaction_id | customer_id | merchant_id | amount | transaction_velocity | avg_amount | prediction |
|----------------|-------------|-------------|--------|-----------------------|------------|------------|
| 1              | 101         | 20          | 150.0  | 1.5                   | 145.0      | 0          |
| 2              | 102         | 35          | 300.0  | 3.0                   | 285.0      | 1          |

---

## **Future Enhancements**
- Integrate with **Kafka** for real-time streaming.
- Add a dashboard for visualization (e.g., using Tableau or Superset).
- Use advanced anomaly detection algorithms (e.g., Isolation Forest, Autoencoders).
- Implement automated alerting for flagged transactions.

---

## **Contributing**
Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

---
