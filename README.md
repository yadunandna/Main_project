# 🧠 ExamPulse AI - Student Mental Wellness Tracker

## Overview

ExamPulse AI is an AI-powered mental wellness assistant designed for students preparing for competitive examinations such as JEE, NEET, UPSC, CAT, and GATE.

The platform helps students identify hidden stress triggers, detect emotional patterns, monitor burnout risk, and receive personalized wellness guidance through AI-powered analysis.

---

## Problem Statement

Students preparing for competitive exams often experience:

* Academic pressure
* Burnout
* Anxiety
* Self-doubt
* Sleep deprivation
* Comparison with peers

Traditional mood trackers only record emotions but fail to uncover deeper emotional patterns and recurring stress triggers.

ExamPulse AI addresses this challenge by using AI to analyze journal entries and provide contextual wellness insights.

---

## Key Features

### 1. Daily Check-In

Students write a journal entry describing their day.

Example:

> I studied for 10 hours today and felt stressed about my mock test performance.

The AI analyzes the entry and provides:

* Mood Assessment
* Stress Level
* Burnout Risk
* Hidden Stress Triggers
* Emotional Patterns
* Personalized Coping Strategies
* Mindfulness Exercises
* Motivational Guidance

---

### 2. Wellness Coach

Interactive AI assistant that allows students to:

* Ask wellness-related questions
* Discuss academic stress
* Seek productivity advice
* Receive emotional support

Example:

Student:

> I am constantly comparing myself to my friends.

AI Coach:

> Comparison often increases unnecessary pressure. Focus on tracking your own progress rather than comparing yourself to others.

---

### 3. Wellness Dashboard

Tracks long-term wellness trends.

Displays:

* Total Journal Entries
* Stress Trends
* Burnout Risk
* Historical Analysis

The dashboard helps students recognize recurring patterns over time.

---

## AI Usage

This project uses Google's Gemini API.

Model:

* Gemini 2.5 Flash

AI is responsible for:

* Journal Analysis
* Emotional Pattern Detection
* Stress Trigger Identification
* Wellness Coaching
* Burnout Insight Generation

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Backend

* FastAPI

### AI

* Google Gemini API

### Storage

* JSON-based local storage

### Deployment

* Vercel

---

## Project Structure

```text
Mental_Wellness_Tracker/

├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ai.py
│   ├── prompts.py
│   ├── storage.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── chat.html
│
├── static/
│   ├── style.css
│   └── app.js
│
├── data/
│   └── journals.json
│
├── tests/
│   └── test_utils.py
│
├── requirements.txt
├── vercel.json
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Mental_Wellness_Tracker
```

### Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

Windows

```bash
myenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Locally

```bash
python -m app.main
```

Application runs on:

```text
http://127.0.0.1:8000
```

---

## API Endpoints

### Home

```text
/
```

### Dashboard

```text
/dashboard
```

### Wellness Coach

```text
/chat
```

### Health Check

```text
/health
```

### Journal Data

```text
/api/journals
```

### Statistics

```text
/api/stats
```

---

## Security Considerations

* API keys stored using environment variables
* No hardcoded secrets
* Input validation on journal submissions
* Local JSON storage without sensitive credential exposure

---

## Assumptions

* Users are students preparing for academic examinations.
* Journal entries are voluntarily provided.
* AI responses are informational and supportive.
* The platform does not provide medical diagnosis or professional mental health treatment.

---

## Future Improvements

* User authentication
* Cloud database integration
* Personalized wellness scores
* Weekly AI wellness reports
* Trigger frequency analytics
* Email wellness summaries
* Advanced burnout prediction

---

## Conclusion

ExamPulse AI transforms traditional journaling into an intelligent wellness companion that helps students understand their emotional patterns, identify hidden stress triggers, and maintain healthier study habits during high-pressure exam preparation.
