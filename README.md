# SirenBackend
### 🍔 AI-Powered Razorpay Support Agent for Food Delivery App
### 📌 Overview

This project is an AI-powered support agent integrated into a food delivery application to automatically handle Razorpay-related payment issues such as failed payments, delayed refunds, and unclear transaction states.

Instead of relying on manual customer support, the system understands user issues, verifies real payment data from Razorpay, and provides instant resolutions or escalations.

### ❓ Problem Statement

Food delivery platforms frequently face:

Payment failures with money debited

Refund delays and confusion

High support ticket volume

Poor user experience during payment issues

Manual support is slow, inconsistent, and expensive.

### 💡 Solution

We built an intelligent Razorpay Support Agent that:

Understands user payment complaints using AI

Fetches real-time payment & refund status from Razorpay

Applies predefined resolution rules

Responds instantly with clear explanations or escalates when required

This reduces support workload and improves customer trust.

### ⚙️ How It Works (High Level Flow)

User reports a payment issue in the app

Agent classifies the issue (failed, pending, refunded, duplicate, etc.)

Razorpay APIs are queried using Payment ID / Order ID

Decision engine applies resolution logic

User receives a clear response or escalation confirmation

### 🧩 System Modules

User Query Handler – Captures user issue

Intent Classification Agent – Detects payment issue type

Razorpay Integration Layer – Fetches transaction details

Resolution Engine – Applies business rules

Response Generator – Converts data into user-friendly messages

### 📥 Inputs

User payment complaint (text)

Payment ID / Order ID

Timestamp (optional)

### 📤 Outputs

Payment / refund status

Refund ETA (if applicable)

Auto-resolution or escalation notice

### ⚠️ Edge Cases Handled

Missing or invalid payment ID

Payment debited but order failed

Refund pending beyond expected time

Razorpay API failure

Duplicate user requests

### 🛠️ Tech Stack

Frontend: Food App Support UI

Backend: FastAPI / Node.js

AI Layer: LLM + rule-based logic

Payments: Razorpay APIs

Database: SQLite / Redis (session & caching)

Version Control: Git

### 🚀 Key Features

Real-time Razorpay payment verification

Automated refund explanation

Reduced manual support dependency

Scalable agent-based architecture

Hackathon-ready MVP design

### 🎯 Why This Matters

Improves user trust during payment failures

Reduces customer support workload

Ensures consistent and accurate responses

Easily extendable to other payment gateways

### 🏁 Future Enhancements

Webhook-based real-time updates

Multi-language support

Analytics dashboard for payment issues

Auto-refund triggers for eligible cases

### 🧠 Final Note

This is not just a chatbot — it’s an intelligent payment support agent that combines AI reasoning with real Razorpay transaction data to resolve issues automatically.

