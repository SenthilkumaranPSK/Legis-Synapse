# ⚖️ Legis Synapse
**Generative AI for Demystifying Legal Documents**  
*Powered by Google Agent Development Kit (ADK)*  

---

## 🌟 Overview
**Legis Synapse 3.0** is an **AI-powered multi-agent legal assistant** that simplifies, analyzes, and secures legal documents.  
It uses **Google Cloud** and **Agent Development Kit (ADK)** to orchestrate **24 specialized agents**, delivering intelligent document processing and risk-free legal workflows.

> “Simplifying legal complexities, one document at a time.”

---

## 🧩 Problem Statement
- Legal documents are **complex, ambiguous, and time-consuming** to interpret.  
- **Language barriers** make them inaccessible to non-legal users.  
- Manual reviews are **slow and expensive**, leading to **delays and disputes**.  
- Absence of **tamper-proof systems** decreases trust in legal agreements.

---

## 💡 Solution
Legis Synapse tackles these challenges by:
- **Simplifying legal jargon** into plain, understandable language.  
- Automatically **detecting non-compliant or risky clauses**.  
- **Predicting disputes** through negotiation simulations.  
- Creating **tamper-proof blockchain-based smart contracts**.  
- Providing **multi-language and voice interaction** support.

---

## 🎥 Demo Video  
Watch our demo video here:  
[![Watch Demo](https://img.shields.io/badge/Watch%20Video-Click%20Here-blue)](https://drive.google.com/file/d/1VvgaZ-wlL8sxpO-b2mhNzDNU--Cn7a0Q/view)

## Prototype  
Try our Prototype here:  
[![Try Demo]([https://img.shields.io/badge/Watch%20Video-Click%20Here-blue)](https://my-adk-service-114499807475.us-central1.run.app))

---

## 🚀 Key Features
- **24 Specialized AI Agents** working collaboratively.  
- **Document Simplification:** Converts complex clauses into plain text.  
- **Risk & Compliance Checker:** Highlights ambiguous or missing clauses.  
- **Negotiation Simulator:** Predicts dispute outcomes and suggests actions.  
- **Blockchain Smart Contracts:** Tamper-proof and transparent.  
- **Multi-Language Support:** Voice and text support for Indian languages.  
- **Google Cloud Native:** Runs entirely on Google ADK, Vertex AI, and Firebase.  
- **₹0 Hackathon Cost:** Built using free-tier GCP and credits.

---

## 🏗 Architecture
Legis Synapse is built using **Google ADK** for **agent orchestration** and **frontend UI**, fully hosted on **Google Cloud Run**.

UPLOAD DOCUMENT → SIMPLIFY → COMPLIANCE CHECK → NEGOTIATION → SECURE CONTRACT

markdown
Copy code

---

## 🔹 Agents in Legis Synapse

| **#** | **Agent Name** | **Purpose / Functionality** |
|-------|----------------|------------------------------|
| **1** | Document Ingestion Agent | Handles document uploads (PDF, DOCX, images). |
| **2** | OCR Agent | Extracts text from scanned or image-based documents. |
| **3** | Data Cleaning Agent | Removes unnecessary headers, footers, and noise. |
| **4** | Document Classifier Agent | Detects document type (lease, NDA, tax, etc.). |
| **5** | Clause Segmenter Agent | Splits text into clauses for focused analysis. |
| **6** | Entity Recognition Agent | Identifies names, dates, amounts, and places. |
| **7** | Jargon Buster Agent | Explains legal terms in plain English/regional languages. |
| **8** | Clause Simplifier Agent | Simplifies complex legal clauses. |
| **9** | Obligations & Rights Extractor | Lists user obligations and entitlements clearly. |
| **10** | Summarizer Agent | Generates concise summaries of documents. |
| **11** | Risk Assessor Agent | Assigns Red/Yellow/Green risk scores. |
| **12** | Ambiguity Detector Agent | Flags vague or unclear language. |
| **13** | Missing Clause Agent | Detects absence of standard protection clauses. |
| **14** | Jurisdiction Compliance Agent | Checks compliance with local/state regulations. |
| **15** | Q&A Agent | Answers user-specific questions with RAG pipeline. |
| **16** | Report Generator Agent | Creates final structured reports. |
| **17** | Multilingual Translator Agent | Provides regional language translation support. |
| **18** | Orchestrator Agent | Manages overall agent workflow and pipelines. |
| **19** | Privacy Guard Agent | Redacts sensitive or personally identifiable information (PII). |
| **20** | Precedent Analysis Agent | Finds similar cases and outcomes. |
| **21** | Compliance Verification Agent | Deep compliance checks for monetary limits and laws. |
| **22** | Graph Reasoning Agent | Builds relationship graphs between clauses. |
| **23** | Argument Miner Agent | Identifies leverage points for negotiation. |
| **24** | Negotiation Strategist Agent | Drafts negotiation counteroffers and messages. |

---

## 🛠 Tech Stack

| **Layer** | **Technology Used** |
|-----------|---------------------|
| **Frontend / UI** | Google **ADK Dev UI** |
| **AI Engine** | Vertex AI – Gemini Pro, ADK Agent Orchestration |
| **Data Storage** | Firestore, Cloud Storage |
| **Backend** | Google Cloud Run, Docker |
| **Security** | Firebase Auth, Cloud KMS |
| **Blockchain** | Ethereum Sepolia Testnet |
| **Voice & Language** | Google Translate API, Speech-to-Text API |

---

## 📥 Installation

### **Install Google ADK**
The ADK is a Python-first toolkit for building and deploying AI agents.

```bash
pip install google-adk
pip install -r requirements.txt
