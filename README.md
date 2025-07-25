# Project: Enterprise-Grade AI ChatOps System with MLOps, CI/CD, and Cloud-Native Architecture

##  Goal
Developed a production-ready, scalable AI-powered **ChatOps platform** that integrates with enterprise tools, utilizes cutting-edge NLP models, and supports automated CI/CD, monitoring, and retraining pipelines.

---

##  Technologies & Services Used

### AI/ML Stack:
- **LLMs**: OpenAI GPT-4 / Claude / Custom finetuned LLaMA
- **NLP Models**: Sentence-BERT (intent), Named Entity Recognition (spaCy/Flair)
- **Vector DB**: FAISS or Pinecone for semantic search
- **ML Pipeline**: MLflow, DVC, Weights & Biases

### DevOps & Cloud:
- **Cloud Platform**: AWS (SageMaker, EKS, Lambda, S3, API Gateway)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (EKS)
- **CI/CD**: GitHub Actions + ArgoCD or JenkinsX
- **Monitoring**: Prometheus, Grafana, Sentry
- **Logging**: ELK stack (Elasticsearch, Logstash, Kibana)

### Automation:
- **Model retraining** on drift (data drift detection using Evidently.ai)
- **Event-driven architecture** using AWS EventBridge or Kafka
- **Autoscaling inference APIs** based on traffic

---

##  Core Features

- Real-time chatbot with GPT-4/Claude backend
- Fine-tuned intent classification with Sentence-BERT
- Named Entity Recognition + RAG (retrieval-augmented generation)
- Slack/Teams integration
- Integration with enterprise APIs (e.g., JIRA, Salesforce, Zendesk)
- Self-updating knowledge base via cron jobs + CI pipelines
- ML monitoring and alerts (latency, failure, drift)
- Chat feedback loop integrated into retraining pipeline

---

##  System Architecture

1. **User** sends message via Slack / Web / Teams
2. **API Gateway** routes to FastAPI (on EKS)
3. FastAPI triggers:
   - Sentence-BERT → intent
   - RAG (VectorDB + GPT-4) → answer generation
   - Optional REST calls to JIRA/Salesforce
4. Answer returned to user via webhook
5. Logs/metrics go to ELK + Prometheus/Grafana
6. MLflow monitors model performance
7. GitHub Actions triggers retraining when:
   - new data available
   - drift is detected (Evidently.ai)
   - performance drops below threshold
8. ArgoCD deploys new models automatically

---

##  Code Layout

```
chatops-ai/
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── pipeline.py           # NLP + RAG + routing logic
│   ├── integrations/
│   │   ├── jira.py
│   │   ├── salesforce.py
│   ├── models/
│   │   ├── bert_intent.py
│   │   └── gpt_wrapper.py
│   ├── monitoring.py         # MLflow + Prometheus
│   └── retrain_trigger.py    # Feedback loop + scheduler
├── retraining/
│   └── pipeline.yaml         # DVC/MLflow DAG
├── docker/
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── hpa.yaml
├── .github/
│   └── workflows/ci.yml      # GitHub Actions CI/CD
└── README.md
``



##  Output
- Scalable LLM-powered chatbot deployed on cloud
- CI/CD + retraining pipeline with full observability
- DevOps- and MLOps-enabled end-to-end system

##WORK FLOW##
###
+---------------------+
|    User Interface   |  (Slack, Teams, Web)
+---------+-----------+
          |
          v
+---------------------+
|  FastAPI (main.py)  |
+---------+-----------+
          |
          v
+---------------------+        +----------------+
|    NLP Pipeline     |------->| Enterprise APIs|
|    (pipeline.py)    |<-------| (JIRA, SFDC)   |
+---------+-----------+        +----------------+
          |
          v
+---------------------+
|  Sentence-BERT      |  Intent Classification
|  (bert_intent.py)   |
+---------------------+
          |
          v
+---------------------+        +----------------+
|       GPT-4         |<------>|  Vector DB (RAG)|
|    (gpt_wrapper.py) |        +----------------+
+---------------------+
          |
          v
+---------------------+
|   Response to User  |
+---------------------+

  Monitoring (Prometheus/Grafana)
  |-----------------------------|
  Retraining Trigger (Evidently.ai + MLflow)
  |-----------------------------|
  Deployment (Docker + Kubernetes)

![image](https://github.com/user-attachments/assets/f8f7722a-e1e6-48e5-aef9-8fcbe1dcf5ad)
![image](https://github.com/user-attachments/assets/26732501-abcc-47e9-acfd-81e2cb43f4db)

  ###

# Core dependencies for AI/NLP
transformers==4.28.1
torch==2.0.1
tensorflow==2.11.0
scikit-learn==1.2.2
numpy==1.24.3
pandas==1.5.3

# ChatOps and communication-related tools
slack-sdk==3.21.3
python-telegram-bot==20.3

# CI/CD and cloud-native tools
docker==6.0.1
boto3==1.26.135  # For AWS SDK
kubernetes==26.1.0  # For Kubernetes API
gitpython==3.1.31  # For Git operations

# Monitoring and logging
prometheus-client==0.16.0
loguru==0.7.0

# Web framework (Optional, for serving APIs)
fastapi==0.95.1
uvicorn==0.22.0

# Other utilities
pyyaml==6.0
requests==2.28.2
tqdm==4.65.0
regex==2023.5.2
protobuf>=3.9.2,<3.20  # For TensorFlow compatibility

# Development and testing
pytest==7.3.1
pytest-cov==4.0.0
black==23.3.0
flake8==6.0.0
mypy==1.3.0

# Ensure compatibility with Windows (if applicable)
colorama==0.4.6
sentry-sdk>=1.0.0
