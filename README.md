
# AWS Log Analyzer

## Overview

AWS Log Analyzer is a Python-based application that simplifies log analysis by automatically identifying errors, detecting recurring failure patterns, generating root-cause summaries, and providing AI-powered troubleshooting recommendations.

The application is designed to reduce the time spent manually reviewing CloudWatch and application logs, enabling faster issue identification and resolution.

---

## Features

### Log Upload

* Upload `.log` or `.txt` files for analysis.
* Supports application logs, container logs, and AWS service logs.

### Error Detection

Automatically identifies:

* ERROR entries
* Exceptions
* Timeout failures
* Connection issues
* Failed operations

### Failure Pattern Analysis

* Groups similar errors.
* Highlights recurring issues.
* Identifies the most frequent failures.

### AI-Powered Insights

Generates:

* Root-cause summaries
* Troubleshooting recommendations
* Potential remediation steps

### Reporting

Provides:

* Error summaries
* Failure statistics
* Actionable recommendations

---

## Use Cases

* AWS Batch job troubleshooting
* ECS/EKS container debugging
* CloudWatch log analysis
* Application failure investigation
* DevOps and SRE operational support

---

## Architecture

```text
User
  |
Upload Log File
  |
Streamlit UI
  |
Log Parser
  |
Pattern Detection Engine
  |
AI Analysis Module
  |
Insights & Recommendations
```

---

## Tech Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Frontend         | Streamlit         |
| Backend          | Python            |
| AI Analysis      | OpenAI API        |
| Data Processing  | Pandas            |
| Containerization | Docker            |
| Cloud Deployment | AWS ECS / Fargate |

---

## Project Structure

```text
aws-log-analyzer/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── analyzer/
│   ├── parser.py
│   ├── patterns.py
│   └── ai_summary.py
│
├── sample_logs/
│   └── batch_failure.log
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd aws-log-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Running Locally

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Docker Deployment

### Build Image

```bash
docker build -t aws-log-analyzer .
```

### Run Container

```bash
docker run -p 8501:8501 aws-log-analyzer
```

---

## Sample Analysis

### Input

```text
2026-05-20 ERROR Failed to pull image

CannotPullContainerError

Timeout while contacting ECR
```

### Output

**Detected Issues**

* Failed image pull
* Container startup failure
* ECR connectivity timeout

**Root Cause Summary**

* Container image could not be retrieved from Amazon ECR due to connectivity or permission issues.

**Recommended Actions**

1. Verify ECR repository access permissions.
2. Confirm image availability.
3. Check network connectivity between compute environment and ECR.
4. Validate IAM role permissions.

---

## Future Enhancements

* Direct CloudWatch log integration
* AWS Bedrock integration
* PDF report generation
* Historical trend analysis
* Dashboard visualizations
* Email and Slack notifications
* Incident report generation

---

## Learning Objectives

This project demonstrates:

* Python development
* Log parsing and analysis
* AI-powered automation
* AWS troubleshooting workflows
* Docker containerization
* Cloud-native application deployment

---

## Author

Chaitra Thimmaiah

Lead - Data Quality Assurance | QA Automation | AWS | AI & Cloud Enthusiast

