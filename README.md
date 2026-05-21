
# Enterprise Generative AI Customer Feedback Analyzer

## Overview

Enterprise Generative AI project focused on automating customer feedback analysis using Large Language Models (LLMs), Prompt Engineering, and SAP Generative AI technologies.

The system transforms unstructured customer emails into structured, machine-readable JSON outputs that can be integrated into enterprise workflows for automated processing, prioritization, and routing.

This project demonstrates practical enterprise AI concepts including:
- Prompt Engineering
- Prompt Hardening
- Grounding
- Retrieval-Augmented Generation (RAG)
- LLM Evaluation
- AI Workflow Orchestration
- Enterprise AI Integration

---

# Business Problem

Customer support teams spend significant operational time:
- Reading emails manually
- Identifying customer intent
- Categorizing issues
- Extracting business information
- Routing requests to the correct department

This project automates these operations using enterprise-oriented Generative AI workflows.

---

# Main Features

## Automated Customer Email Analysis

The solution automatically performs:
- Customer sentiment detection
- Issue categorization
- Structured information extraction
- Actionable resolution identification
- Priority assignment

---

## Multi-Issue Detection

The system identifies multiple independent issues within a single customer message.

Example:
- Product defect
- Delivery problem
- Account issue
- Refund request

Each issue is extracted and processed independently.

---

## Enterprise-Ready Structured Output

The generated responses are:
- Clean
- Parseable
- Structured
- JSON-compliant
- Suitable for enterprise automation pipelines

---

## Prompt Hardening & Alignment

Security-focused prompt engineering techniques were implemented to:
- Reduce hallucinations
- Restrict off-topic generation
- Prevent sensitive data leakage
- Enforce strict JSON formatting
- Maintain enterprise workflow reliability

---

## Grounding & RAG Concepts

The architecture integrates grounding principles and Retrieval-Augmented Generation (RAG) concepts to improve contextual accuracy and reduce unreliable outputs.

This enables the LLM to remain aligned with enterprise business context and operational constraints.

---

# Technologies & Concepts

## AI / LLM Technologies
- SAP Generative AI Hub
- GPT-4o
- Gemini
- Mistral AI
- Large Language Models (LLMs)

---

## AI Engineering
- Prompt Engineering
- Prompt Hardening
- Few-Shot Prompting
- Multi-Prompting
- Grounding
- Retrieval-Augmented Generation (RAG)
- AI Pipeline Orchestration
- LLM Evaluation & Selection

---

## Data & Processing
- Structured JSON Extraction
- Information Classification
- Sentiment Analysis
- Workflow Automation
- Python Workflow Orchestration
- Data Structuring & Validation

---

## Enterprise Concepts
- Enterprise AI Integration
- Business Workflow Automation
- Customer Support Optimization
- Decision Support Systems
- AI Reliability Optimization

---

# Project Architecture

```text
Customer Email
      ↓
Prompt Template (SAP Generative AI Hub)
      ↓
LLM Processing
      ↓
Information Extraction & Classification
      ↓
Structured JSON Output
      ↓
Business Workflow Routing
````

---

# AI Workflow Orchestration

The project includes a Python-based orchestration layer simulating an enterprise AI workflow pipeline.

Main orchestration components:

* Prompt loading and dynamic injection
* Simulated LLM routing
* Structured JSON validation
* Automated department routing
* Modular AI pipeline architecture

This orchestration layer demonstrates how Generative AI systems can be operationalized within enterprise environments using structured workflows and automation pipelines.

---

# SAP AI SDK Integration

The project integrates SAP AI SDK (`sap-ai-sdk-gen`) concepts to simulate enterprise-grade interaction with Generative AI services.

This includes:
- Prompt execution workflows
- Structured response handling
- AI service orchestration
- Enterprise AI integration concepts
- LLM-driven automation pipelines---

# Example Use Cases

## Product Issues

* Defective products
* Missing items
* Replacement requests
* Refund requests

## Delivery Problems

* Delayed shipments
* Lost packages
* Incorrect delivery status

## Account Issues

* Login failures
* Incorrect order history
* Shipping address update problems

---

# Example JSON Output

```json
{
  "Feedback_ID": "FB-1001",
  "Overall_Customer_Sentiment": "Negative",
  "Issues": [
    {
      "Issue_ID": "ISSUE-A",
      "Main_Category": "Delivery Problem",
      "Priority": "High",
      "Issue_Summary": "Customer did not receive package despite delivery confirmation.",
      "Actionable_Resolution_Points": [
        "Investigate shipment status",
        "Contact shipping provider",
        "Provide customer update"
      ]
    }
  ]
}
```

---

# Comparative LLM Evaluation

Multiple LLMs were comparatively evaluated to identify the most reliable production-oriented model.

Evaluation criteria included:

* JSON consistency
* Classification accuracy
* Sentiment detection quality
* Resolution extraction quality
* Reliability for enterprise workflows

Compared models:

* GPT-4o
* Gemini
* Mistral AI

---

# Repository Structure

```text
enterprise-generative-ai-customer-feedback-analyzer/
│
├── README.md
│
├── prompts/
│   ├── system_prompt_v1.txt
│   ├── hardened_prompt_v2.txt
│   ├── multi_issue_prompt_v3.txt
│
├── examples/
│   ├── sample_customer_emails.txt
│   ├── json_outputs.json
│
├── evaluations/
│   ├── gpt4o_results.json
│   ├── gemini_results.json
│   ├── mistral_results.json
│
├── orchestration/
│   ├── main.py
│   ├── prompt_loader.py
│   ├── llm_router.py
│   ├── validator.py
│   ├── department_router.py
│   └── sample_email.txt
│
├── architecture/
│   └── workflow_diagram.png
│
└── docs/
    └── project_summary.md
```


---

# Prompt Engineering Techniques

The project applies multiple advanced prompt engineering techniques designed for enterprise AI workflows:

- Zero-shot prompting
- Few-shot prompting
- Structured prompting
- Role-based prompting
- Prompt hardening
- JSON-constrained generation
- Grounding techniques
- Retrieval-Augmented Generation (RAG) concepts

These techniques were used to improve:
- output reliability,
- extraction accuracy,
- response consistency,
- workflow automation quality,
- and enterprise AI robustness.

---
# Skills Demonstrated

* Enterprise AI Solution Design
* Generative AI Integration
* AI Workflow Automation
* Prompt Engineering
* AI Pipeline Orchestration
* Structured Data Extraction
* Enterprise Workflow Integration
* LLM Evaluation & Selection
* Business Process Automation
* AI Reliability Optimization

---

# Author

**Rihabe Mounaim**
AI & Data Student — MIAGE
Specialization: Enterprise Systems, Generative AI, Data & Decision Support

```
```
