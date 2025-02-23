# 📰 Discord Bot Shared

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://github.com/jkassel/DiscordBotShared/actions/workflows/deploy.yml/badge.svg)](https://github.com/jkassel/DiscordBotShared/actions)
[![AWS CDK](https://img.shields.io/badge/built%20with-AWS%20CDK-orange)](https://aws.amazon.com/cdk/)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)

## 🌟 Overview

**DiscordBotShared** is a foundational repository that provides the shared **API Gateway**, **IAM roles**, and **Secrets Manager integrations** for multiple Discord bot projects. This allows individual bots, such as `DiscordNewsBot`, to **reuse a single API Gateway** while keeping infrastructure centralized.

👉 **Key Features:**
- ⚡ **Centralized API Gateway** for all Discord bots.
- 🔒 **Shared AWS Secrets Manager configuration** for bot credentials.
- 🛠 **Reusable AWS CDK Constructs** for easy bot deployments.
- 🎯 **Optimized for multi-repo support** (each bot references this stack).

---

## 📂 Project Structure

```
📦 DiscordBotShared
├── 💁 src
│   ├── 💁 cdk                           # AWS CDK Infrastructure
│   │   ├── app.py                       # CDK entry point
│   │   ├── cdk.json                     # CDK configuration
│   │   ├── discord_bot_shared_stack.py  # Defines API Gateway, Secrets, IAM roles
│   │   └── outputs.py                   # Exports values for dependent repos
├── 💁 .github/workflows       # CI/CD automation
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation (YOU ARE HERE)
└── Makefile                   # Simplified setup and deployment
```

---

## 🚀 Deployment Guide

### **1️⃣ Prerequisites**
- ✅ Python 3.11+ installed ([Download](https://www.python.org/downloads/))
- ✅ AWS CLI installed and configured (`aws configure`)
- ✅ AWS CDK installed:
  ```sh
  npm install -g aws-cdk
  ```

---

### **2️⃣ Installation**
Clone the repository and install dependencies:
```sh
git clone https://github.com/jkassel/DiscordBotShared.git
cd DiscordBotShared
pip install -r requirements.txt
```

---

### **3️⃣ Deploy to AWS**
```sh
cdk bootstrap
cdk deploy
```

Upon successful deployment, this stack will:
- **Provision an API Gateway** to be shared across Discord bots.
- **Export API Gateway ID and Endpoint** for dependent repos.
- **Create a shared IAM role** for bot execution.
- **Store Discord bot credentials securely in AWS Secrets Manager.**

---

## 🔒 Exports for Dependent Repositories
After deployment, the following values will be available for use by other repositories:

| Export Name           | Description |
|----------------------|-------------|
| **`ApiGatewayId`**  | The ID of the shared API Gateway. |
| **`ApiGatewayEndpoint`**  | The HTTP endpoint for API requests. |

---

## 🌟 Integrating with Other Bots
For example, in **DiscordNewsBot**, you can reference this shared infrastructure:

```python
from aws_cdk import Fn

# Import shared API Gateway from DiscordBotShared
api_gateway_id = Fn.import_value("ApiGatewayId")
api_gateway_endpoint = Fn.import_value("ApiGatewayEndpoint")
```

Ensure that **DiscordBotShared is deployed first**, so dependent repositories can access these values.

---

## 🛠 Troubleshooting

| Issue | Solution |
|--------|------------|
| **`ResourceNotFound` when referencing `ApiGatewayId`** | Ensure **DiscordBotShared** is deployed **before** dependent bot projects. Run `cdk deploy` again if needed. |

---

## 💬 Support

Need help? **Join the Discord support server** or open a [GitHub Issue](https://github.com/YOUR_GITHUB_USERNAME/DiscordBotShared/issues).

---

## 🚀 Star ⭐ this repo if you found it useful!

