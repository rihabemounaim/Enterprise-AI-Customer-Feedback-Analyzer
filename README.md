# Enterprise AI Customer Feedback Analyzer

## Overview

Enterprise AI project designed to automate customer email analysis using Large Language Models (LLMs) and SAP Generative AI technologies.

The solution transforms unstructured customer emails into structured, machine-readable JSON outputs that can be integrated into enterprise workflows for faster processing, prioritization, and routing.

This project was developed as part of practical work around SAP Generative AI concepts including:

* Prompt Engineering
* Prompt Hardening
* Retrieval-Augmented Generation (RAG)
* Grounding
* LLM Evaluation
* AI Workflow Automation
* Enterprise AI Integration

---

# Business Problem

Customer service teams often spend significant time:

* Reading emails manually
* Identifying customer intent
* Categorizing issues
* Extracting useful information
* Routing requests to the correct department

This project automates these operations using AI-powered information extraction and classification.

---

# Main Features

## Automated Email Analysis

* Customer sentiment detection
* Issue categorization
* Priority assignment
* Structured information extraction

## Multi-Issue Detection

The system can identify multiple issues inside a single customer message.

Example:

* Product defect
* Delivery issue
* Account problem

Each issue is processed independently.

## Enterprise-Ready JSON Output

The generated output is:

* Clean
* Parseable
* Structured
* Ready for automated workflows

## Prompt Hardening

Implemented security-focused prompt engineering techniques to:

* Reduce hallucinations
* Prevent data leakage
* Restrict non-business outputs
* Enforce strict JSON formatting

## Grounding & RAG Concepts

The architecture integrates grounding concepts to improve response reliability by constraining model outputs around enterprise business context.

---

# Technologies & Concepts

## AI / LLM

* SAP Generative AI Hub
* Large Language Models (LLMs)
* GPT-4o
* Gemini
* Mistral AI

## AI Engineering

* Prompt Engineering
* Prompt Hardening
* Multi-Prompting
* Few-Shot Prompting
* Grounding
* Retrieval-Augmented Generation (RAG)
* LLM Evaluation

## Data & Processing

* JSON Structuring
* Data Extraction
* Information Classification
* Sentiment Analysis
* Workflow Automation

## Enterprise Concepts

* AI Integration in Business Workflows
* Process Automation
* Customer Support Optimization
* Decision Support Systems

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
Business Department Routing
```

---

# Example Use Cases

## Product Issue

* Defective product
* Missing item
* Refund request

## Delivery Problems

* Delayed shipment
* Wrong delivery status
* Lost package

## Account Issues

* Login problems
* Incorrect customer information
* Address update failure

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
        "Investigate shipping status",
        "Contact delivery company",
        "Provide customer update"
      ]
    }
  ]
}
```

---

# LLM Evaluation

Multiple models were evaluated comparatively to identify the most reliable production-ready model.

Evaluation criteria:

* JSON consistency
* Classification accuracy
* Sentiment detection quality
* Actionable resolution extraction
* Enterprise output reliability

Compared models:

* GPT-4o
* Gemini
* Mistral AI

---

# Repository Structure

```text
enterprise-ai-customer-feedback-analyzer/
│
├── README.md
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
├── architecture/
│   ├── workflow_diagram.png
│
└── docs/
    ├── project_summary.md
```

---

# Skills Demonstrated

* Enterprise AI Solution Design
* Generative AI Integration
* AI Workflow Automation
* Prompt Engineering
* AI Reliability Optimization
* Business Process Automation
* Data Structuring & Classification
* LLM Evaluation & Selection
* AI Systems Thinking

---

# Author

Rihabe Mounaim
AI & Data Student — MIAGE
Specialization: Enterprise Systems, Generative AI, Data & Decision Support
