# Cloud-Native Monitoring App (Flask → Docker → AWS ECR → Kubernetes/EKS)

This project is a complete **DevOps, cloud-native pipeline**:

- Build a monitoring app using **Python + Flask + psutil**
- Containerize it with **Docker**
- Store the image in **AWS ECR**
- Deploy it to **AWS EKS (Kubernetes)**
- Access it through a Kubernetes Service

The app displays **real-time CPU and Memory usage**, and alerts when usage gets high.

---

## 📌 Architecture Overview

User → Service → Deployment → Pods → Container (Flask App)
                       |
                       → Image pulled from AWS ECR
                       |
                       → Runs inside AWS EKS cluster (nodes)

## ✨ Features

- Real-time CPU / Memory monitoring
- Interactive UI (Plotly gauges)
- Docker containerization
- Secure image storage in AWS ECR
- Deployment on Kubernetes (EKS)
- Python automation (boto3 + Kubernetes client)

---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
App | Python, Flask, psutil, Plotly
Containers | Docker
Cloud Registry | AWS ECR
Orchestration | Kubernetes (EKS)
Automation | boto3, Kubernetes Python client
CLI | kubectl, AWS CLI
