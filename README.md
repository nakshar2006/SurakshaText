# 🛡️ SurakshaText

### Multilingual Phishing & Scam Detection

**Detect → Explain → Educate → Protect**

SurakshaText is a multilingual text-safety platform designed to help users identify potentially harmful, suspicious, and phishing-related messages before they lead to unsafe actions.

The project focuses on making digital communication safer by not only detecting suspicious messages, but also explaining **why** a message may be risky and helping users make safer decisions.

---

## 📌 Problem Statement

Phishing and scam messages are becoming increasingly difficult to identify. Attackers often use:

* Urgency and pressure
* Financial threats
* Fake rewards and offers
* Requests for OTPs or sensitive information
* Suspicious links or actions
* Messages written in regional or mixed languages

Scam messages can appear similar to genuine communication, making it difficult for users to recognize malicious intent.

Regional-language and mixed-language messages can further increase this difficulty because many existing safety tools are primarily designed around common-language patterns.

A single shared OTP, clicked link, or unsafe action can result in financial or personal loss.

---

## 💡 Our Solution

SurakshaText aims to provide an accessible text-safety platform that analyzes suspicious messages and helps users understand the potential risks.

The overall vision is to move from simply detecting suspicious text to providing an understandable and explainable safety experience.

### Core idea

```text
INPUT
  ↓
ANALYZE
  ↓
DETECT THREATS
  ↓
ASSESS RISK
  ↓
EXPLAIN
  ↓
PROTECT
```

The platform is designed to evolve from typed-text analysis into a broader safety system capable of handling different forms of suspicious content.

---

# 🚀 Current Prototype

The current implementation is a **functional end-to-end prototype** focused on typed or pasted text.

It consists of:

* React + Vite frontend
* FastAPI + Python backend
* REST API communication
* Rule-based phishing and scam detection
* Risk scoring
* SAFE / SUSPICIOUS / DANGEROUS classification
* Detected threat indicators
* Matched keywords
* Safety recommendations
* English, Kannada, and Hindi demonstration examples
* Public deployment through Vercel and Render

The current detection engine is intentionally **rule-based rather than AI/ML-based**, allowing the prototype to provide transparent and explainable results.

---

# 🔍 How the Current System Works

```text
User enters or pastes a message
              ↓
       React Frontend
              ↓
       FastAPI REST API
              ↓
    Rule-Based Detection Engine
              ↓
        Risk Assessment
              ↓
 Classification + Indicators + Explanation
              ↓
        Result shown to user
```

The backend analyzes the message for phishing and scam-related patterns, calculates a risk score, determines a classification, and returns information explaining the result.

---

# 🧠 Detection & Risk Analysis

The current rule-based engine looks for indicators such as:

* OTP and credential requests
* Urgency and pressure
* Account threats
* Financial bait
* Suspicious actions
* Phishing-related keywords and patterns
* Potentially suspicious URLs or message structures

The system combines detected indicators into a risk assessment rather than relying only on a single keyword.

---

# 📊 Message Classification

The prototype provides three main classifications:

### 🟢 SAFE

The message does not contain strong phishing indicators based on the current detection rules.

### 🟠 SUSPICIOUS

The message contains indicators that may require caution or verification.

### 🔴 DANGEROUS

The message contains strong phishing or scam indicators and should be treated with immediate caution.

Along with the classification, the system provides:

* Risk score
* Threat type
* Detected indicators
* Matched keywords
* Safety recommendation

This makes the result more explainable than simply displaying a label.

---

# 🌐 Multilingual Focus

SurakshaText is designed with multilingual digital communication in mind.

The current prototype demonstrates examples in:

* 🇬🇧 English
* 🇮🇳 Kannada
* 🇮🇳 Hindi

The broader goal is to improve phishing and scam awareness for users who communicate in regional languages or mixed-language formats.

Broader language coverage and automatic language identification are planned future improvements.

---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* JavaScript
* CSS

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## Communication

* REST API

## Detection

* Rule-based risk analysis

## Deployment

* Vercel — Frontend
* Render — Backend

---

# 🏗️ Technical Architecture

```text
                 USER
                   │
                   ▼
          ┌─────────────────┐
          │ React + Vite    │
          │    Frontend     │
          └────────┬────────┘
                   │
                   │ REST API
                   ▼
          ┌─────────────────┐
          │ FastAPI Backend │
          │    /analyze     │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Rule-Based      │
          │ Detection Engine│
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Risk Assessment │
          └────────┬────────┘
                   │
                   ▼
       ┌─────────────────────────┐
       │ Classification           │
       │ Indicators               │
       │ Risk Score               │
       │ Recommendation           │
       └────────────┬────────────┘
                    │
                    ▼
             USER-FRIENDLY
                RESULT
```

---

# 📁 Project Structure

```text
SurakshaText/
│
├── backend/
│   ├── main.py
│   ├── rules.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

# ▶️ Running the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/nakshar2006/SurakshaText.git
cd SurakshaText
```

---

## 2. Run the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The FastAPI backend will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 3. Run the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Vite will provide the local development URL.

---

# 🌍 Live Prototype

### Frontend

https://suraksha-text.vercel.app/

The live frontend communicates with the deployed FastAPI backend and provides real-time message analysis.

### Live API

The backend is deployed using Render and exposes the FastAPI API, including the `/analyze` endpoint and interactive `/docs` documentation.

---

# 🧪 Example Messages

### SAFE

```text
Hey, are we still meeting at 5 PM today?
```

### SUSPICIOUS

```text
Congratulations! You won a prize. Claim your reward now.
```

### DANGEROUS

```text
Your bank account will be blocked. Share your OTP immediately.
```

The prototype can also demonstrate equivalent examples in Kannada and Hindi.

---

# 📱 Live Prototype & QR Access

The deployed prototype can be accessed directly through the public website.

A QR code is also provided in the project presentation so that users can:

```text
SCAN
  ↓
OPEN SURAKSHATEXT
  ↓
ENTER A MESSAGE
  ↓
ANALYZE
  ↓
VIEW THE RISK
```

No installation is required to try the live prototype.

---

# 🗺️ Future Roadmap

The current prototype focuses on typed-text analysis. The broader SurakshaText vision includes expanding the system to understand suspicious content wherever users encounter it.

### Phase 1 — Current

**Text Analysis**

* React + FastAPI
* Rule-based detection
* Risk scoring
* Explainable results

### Phase 2 — Planned

**Screenshot Analysis**

* Screenshot upload
* OCR-based text extraction
* Analysis of extracted message content

### Phase 3 — Planned

**Language Intelligence**

* Automatic language identification
* Expanded regional-language support
* Improved multilingual pattern handling

### Phase 4 — Planned

**Advanced Detection**

* ML-based contextual analysis
* Improved false-positive handling
* More advanced phishing and scam detection

### Phase 5 — Long-Term Vision

**Real-World Deployment**

* Browser integration
* Mobile integration
* Wider real-world communication safety applications

---

# ⚠️ Current Implementation Note

The current prototype uses a **rule-based detection engine and is not an AI/ML model**.

This provides transparent and explainable results during the current development stage.

ML-based contextual analysis is part of the future roadmap.

---

# 👥 Team

## Team EdgeMinds

**Project:** SurakshaText

**Multilingual Phishing & Scam Detection**

---

# 📌 Project Status

### 🟢 Functional End-to-End Prototype

The current prototype has:

* A working React frontend
* A working FastAPI backend
* REST API integration
* Rule-based risk analysis
* SAFE / SUSPICIOUS / DANGEROUS classification
* Explainable results
* Multilingual demonstration
* Public deployment
* Mobile testing
* QR-based access to the live prototype

---

## 🎯 Vision

> **Detect → Explain → Educate → Protect**

SurakshaText aims to make digital communication safer by helping users recognize suspicious messages, understand the risks behind them, and make safer decisions before taking action.
