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

## Architecture

```text
Student
   │
   ▼
Daily Check-In / Wellness Coach
   │
   ▼
FastAPI Backend
   │
   ├── Gemini AI
   │      ├── Journal Analysis
   │      ├── Stress Detection
   │      └── Wellness Coaching
   │
   └── Supabase PostgreSQL
          └── Journal History Storage

   ▼
Dashboard & Insights
```

---

## AI Usage

This project uses Google's Gemini API.

### Model

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

### Database

* Supabase PostgreSQL

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
│   ├── database.py
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
├── requirements.txt
├── vercel.json
├── README.md
└── .env.example
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

### Activate Virtual Environment

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
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

SUPABASE_URL=YOUR_SUPABASE_PROJECT_URL

SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY
```

---

## Supabase Setup

Create a table named:

```sql
create table journals (
    id bigint generated always as identity primary key,
    created_at timestamp default now(),
    journal text,
    analysis text
);
```

---

## Run Locally

```bash
python -m app.main
```

Application runs at:

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

## Sample Test Cases

### Daily Check-In

#### Test Case 1 – Academic Stress

```text
I studied for 10 hours today but my mock test score was lower than expected. I keep comparing myself to my friends and I am worried about my JEE rank.
```

#### Test Case 2 – Burnout Risk

```text
I have been studying 12 hours every day for the last week. I sleep only 5 hours and feel exhausted. I cannot concentrate anymore.
```

#### Test Case 3 – Positive Day

```text
Today was productive. I completed my study targets and felt confident during practice tests. I also took breaks and exercised.
```

#### Test Case 4 – Exam Anxiety

```text
My exam is next month and I feel nervous all the time. Even when I study, I worry that I will forget everything during the exam.
```

#### Test Case 5 – Family Pressure

```text
My parents keep asking about my marks and college admissions. I feel pressured and stressed whenever these conversations happen.
```

---

### Wellness Coach

#### Test Case 1

```text
How can I stop comparing myself with my friends?
```

#### Test Case 2

```text
I am scared that I will fail my exam.
```

#### Test Case 3

```text
How can I improve focus during long study sessions?
```

#### Test Case 4

```text
Can you give me a quick mindfulness exercise?
```

#### Test Case 5

```text
How do I recover from burnout during exam preparation?
```

---

## Security Considerations

* API keys stored using environment variables
* No hardcoded secrets
* Input validation on journal submissions
* Data stored securely in Supabase PostgreSQL
* Database credentials managed through environment variables

---

## Assumptions

* Users are students preparing for academic examinations
* Journal entries are voluntarily provided
* AI responses are informational and supportive
* The platform does not provide medical diagnosis or professional mental health treatment

---

## Future Improvements

* User Authentication
* Personalized Wellness Scores
* Weekly AI Wellness Reports
* Trigger Frequency Analytics
* Email Wellness Summaries
* Advanced Burnout Prediction
* Mobile Application Support

---

## Deployment

The application is deployed on Vercel and uses:

* FastAPI Backend
* Gemini AI API
* Supabase PostgreSQL Database

---

## Conclusion

ExamPulse AI is an AI-powered student wellness platform that combines Gemini AI, FastAPI, Supabase PostgreSQL, and Vercel deployment to help students identify hidden stress triggers, monitor burnout risk, and receive personalized wellness guidance.

By transforming simple journal entries into actionable insights, the platform supports healthier study habits and improved emotional well-being during high-pressure exam preparation.
