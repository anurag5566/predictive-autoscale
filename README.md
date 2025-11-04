# 🚀 Predictive Auto Scaling using AWS CloudWatch and Flask

### 📄 Overview
This project demonstrates a **predictive auto-scaling model** built on **AWS EC2** using **Flask** and **CloudWatch**.  
It analyzes **real-time CPU utilization metrics** and uses a lightweight predictive algorithm to forecast upcoming load trends.  
Based on these predictions, it recommends whether to **scale up**, **scale down**, or **maintain** server capacity — simulating a smart auto-scaling system.

---

### 🧠 Key Features
- Fetches **real-time CPUUtilization metrics** from AWS CloudWatch  
- Uses **NumPy** for simple trend-based prediction  
- Provides a **REST API endpoint (`/predict`)** for real-time recommendations  
- Lightweight and deployable on any **AWS EC2 instance**

---

### ⚙️ Technologies Used
- **Python 3**
- **Flask** — REST API framework  
- **NumPy** — for CPU trend prediction  
- **AWS EC2** — compute instance for hosting the app  
- **AWS CloudWatch** — for monitoring CPU metrics  
- **AWS CLI** — for fetching data programmatically  

---

### 🧩 API Endpoint

#### 🔹 `/predict`
**Method:** `GET`  
**Description:** Returns the current average CPU utilization, predicted next value, and scaling recommendation.

**Example Response:**
```json
{
  "current_avg": 5.19,
  "predicted_next": 5.96,
  "recommendation": "Scale Down"
}
