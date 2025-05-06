# AWS EBS Volume Governance with CloudWatch and Lambda

## 📌 Project Overview
This project demonstrates an automated governance solution in AWS to ensure compliance and cost-efficiency. It uses **CloudWatch Events** to monitor EBS volume creation, triggering an **AWS Lambda function** that checks if the volume is of type `gp2` and converts it to `gp3` automatically.

The project also includes configurations related to IAM roles and has potential extensions to manage **EC2** and **S3** governance policies.

---

## 📊 Architecture Diagram
![image](https://github.com/user-attachments/assets/7bd04a2f-4226-4d71-9c87-9c397c1eb21b)

---

## ⚙️ Tech Stack
- **AWS Lambda**
- **Amazon CloudWatch (EventBridge)**
- **Amazon EC2 / EBS**
- **AWS IAM**
- **Boto3 (Python SDK)**

---

## 🚀 Flow Description

1. A new **EBS Volume** is created.
2. **CloudWatch Event Rule** detects the `CreateVolume` event.
3. EventBridge triggers the **Lambda Function**.
4. The Lambda function:
   - Parses the event to extract the Volume ID.
   - Checks if the volume type is `gp2`.
   - If so, modifies it to `gp3` using Boto3.
5. IAM roles allow the function to:
   - Read CloudWatch events
   - Modify EC2 volumes
6. Logs and metrics are captured via **CloudWatch Logs**.

---

## 📌 Future Scope


Apply similar governance to EC2 instance types or S3 bucket policies.

Notify via SNS when non-compliant resources are found.

Enforce tagging standards using Lambda.
