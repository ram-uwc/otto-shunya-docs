# Otto AI - Complete API Documentation

**Version:** Phase 1 (Personal Otto + 2-Layer Compliance)  
**Last Updated:** November 2025

---

## Table of Contents

1. [SOP Document Upload](#1-sop-document-upload)
2. [Call Processing Pipeline](#2-call-processing-pipeline)
3. [Complete Analysis API](#3-complete-analysis-api)
4. [Individual Analysis APIs](#4-individual-analysis-apis)
5. [Lead Qualification & Intent Classification](#5-lead-qualification--intent-classification)
6. [Meeting Segmentation](#6-meeting-segmentation)
7. [Property Intelligence](#7-property-intelligence)
8. [Personal Otto Training](#8-personal-otto-training)
9. [Follow-up Recommendations](#9-follow-up-recommendations)
10. [View AI Profile](#10-view-ai-profile)
11. [Sample Payloads](#11-sample-payloads)

---

## 1. SOP Document Upload

Upload Standard Operating Procedures (SOPs) for automatic stage extraction and compliance checking.

### Endpoint
```
POST /api/v1/ingestion/sop-documents
```

### Authentication
- **Header:** `Authorization: Bearer <JWT_TOKEN>`
- Extracts: `user_id`, `company_id`, `role` from JWT

### Request
```http
POST /api/v1/ingestion/sop-documents
Content-Type: multipart/form-data
Authorization: Bearer <token>

file: <PDF/DOCX file>
target_roles: ["sales_rep", "customer_rep"]  # Optional, can be one or both
```

### What Happens
1. **Upload to S3** - File stored in company-specific folder
2. **Text Extraction** - PDF/DOCX converted to plain text
3. **AI Stage Extraction** - LLM extracts structured SOP stages
4. **Database Storage** - Stages saved to `sop_stages` table
5. **Embeddings** - Text chunked and embedded for semantic search

### Response
```json
{
  "success": true,
  "document_id": "doc_a7f3b9c2",
  "company_id": "test_company_1",
  "document_type": "sop",
  "stages_extracted": 5,
  "target_roles": ["sales_rep"],
  "processing_status": "processing",
  "message": "SOP document uploaded and processing started"
}
```

### Target Roles

#### `sales_rep` SOP Stages (Example)
- Connect - Greet customer, verify identity
- Agenda - Set call expectations
- Needs Assessment - Understand customer requirements
- Present Solution - Explain product/service
- Close - Book appointment or get commitment

#### `customer_rep` SOP Stages (Example)
- Greeting - Welcome customer
- Issue Identification - Understand problem
- Resolution Steps - Provide solution
- Follow-up Plan - Schedule next steps
- Closing - Thank and confirm

---

## 2. Call Processing Pipeline

Complete pipeline for processing call audio through multiple analysis steps.

### Step-by-Step Process

#### **Step 1: Upload Call Audio**
```
POST /api/v1/calls/upload
Content-Type: multipart/form-data

file: <audio file>
call_id: 12345
company_id: test_company_1
```

#### **Step 2: Transcription**
- Audio → Text using Deepgram/Whisper
- Saved to `call_transcripts` table
- Status tracked in `call_analysis_status`

#### **Step 3: Automatic Analysis** (Background)

The system automatically triggers:

1. **Summary Generation**
   - Extracts key points, customer name, issue
   - Saved to `call_summaries`

2. **Objection Detection**
   - Identifies price, timing, authority objections
   - Saved to `call_objections`

3. **Lead Qualification (BANT)**
   - Budget, Authority, Need, Timeline scores
   - Intent classification: `qualified_and_booked`, `qualified_unbooked`, etc.
   - Saved to `call_lead_scores`

4. **Property Intelligence** (if applicable)
   - Property address, type, age, condition
   - Saved to `call_property_intelligence`

5. **SOP Compliance** (2-Layer for Sales)
   - **Layer 1:** Stage-by-stage compliance check
   - **Layer 2:** Overall outcome evaluation
   - Saved to `call_compliance_checks` and `call_outcome_scores`

#### **Step 4: Check Analysis Status**
```
GET /api/v1/call-analysis/status/{call_id}
```

Response:
```json
{
  "call_id": 12345,
  "status": "completed",
  "progress": 100,
  "analyses_completed": {
    "transcription": true,
    "summary": true,
    "objections": true,
    "qualification": true,
    "property_intelligence": true,
    "compliance": true
  },
  "completion_time": "2025-11-16T10:30:00Z"
}
```

---

## 3. Complete Analysis API

Get all analysis results in a single API call.

### Endpoint
```
GET /api/v1/call-analysis/analysis/complete/{call_id}
```

### Authentication
```
Authorization: Bearer <JWT_TOKEN>
```

### Response Structure
```json
{
  "success": true,
  "call_id": 12345,
  "company_id": "test_company_1",
  "analyses": {
    "summary": {
      "summary_text": "Customer Kelly called about roof leak...",
      "key_points": ["Roof leak", "Urgent repair needed"],
      "customer_name": "Kelly",
      "issue_description": "Water damage in garage",
      "created_at": "2025-11-16T10:25:00Z"
    },
    
    "objections": {
      "objections": [
        {
          "category": "Price/Cost",
          "objection_text": "That seems expensive",
          "speaker": "customer",
          "severity": "medium",
          "resolution_suggested": "Offer financing options"
        }
      ],
      "total_count": 1,
      "no_objections": false,
      "no_objections_reason": null
    },
    
    "qualification": {
      "bant_scores": {
        "budget": 0.8,
        "authority": 0.9,
        "need": 0.95,
        "timeline": 0.7
      },
      "overall_score": 0.84,
      "qualification_status": "qualified_and_booked",
      "decision_makers": ["Kelly (Homeowner)"],
      "urgency_signals": ["Leak causing damage", "Wants quick resolution"],
      "budget_indicators": ["Discussed financing", "Ready to proceed"],
      "confidence_score": 0.85,
      "service_not_offered_reason": null,
      "follow_up_reason": null
    },
    
    "property_intelligence": {
      "property_address": "157 S Sunland Gin Rd",
      "property_type": "Single Family Home",
      "property_age": "15 years",
      "property_condition": "Good, but needs roof repair",
      "property_value": "~$350,000",
      "additional_notes": "Asphalt shingle roof, garage leak"
    },
    
    "meeting_segmentation": {
      "part1": {
        "duration": 245.5,
        "content": "Rapport building and needs discovery",
        "key_points": ["Built rapport", "Set agenda", "Identified needs"]
      },
      "part2": {
        "duration": 234.5,
        "content": "Presentation and closing",
        "key_points": ["Presented options", "Addressed objections", "Booked appointment"]
      },
      "meeting_structure_score": 4,
      "segmentation_confidence": 0.92
    },
    
    "compliance": {
      "final_decision": "pass",
      "overall_score": 85.0,
      "layer_1": {
        "compliance_score": 88.0,
        "stages_completed": [
          {
            "stage_name": "Connect",
            "status": "completed",
            "score": 95,
            "issues": []
          },
          {
            "stage_name": "Needs Assessment",
            "status": "completed",
            "score": 85,
            "issues": ["Could have asked more probing questions"]
          }
        ]
      },
      "layer_2": {
        "outcome_score": 82.0,
        "call_outcome": "qualified_and_booked",
        "booking_status": "booked",
        "strengths": ["Good rapport", "Clear next steps"],
        "improvement_areas": ["More benefit statements"]
      }
    }
  }
}
```

---

## 4. Individual Analysis APIs

Access individual analysis components separately.

### 4.1 Summary
```
GET /api/v1/call-analysis/summary/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "summary": {
    "summary_text": "Customer Kelly called about roof leak...",
    "key_points": ["Roof leak", "Urgent repair"],
    "customer_name": "Kelly",
    "issue_description": "Water damage in garage"
  }
}
```

### 4.2 Objections
```
GET /api/v1/call-analysis/objections/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "objections": {
    "objections": [
      {
        "category": "Price/Cost",
        "objection_text": "That's expensive",
        "severity": "medium"
      }
    ],
    "total_count": 1,
    "no_objections": false
  }
}
```

### 4.3 Qualification
```
GET /api/v1/call-analysis/qualification/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "qualification": {
    "bant_scores": {
      "budget": 0.8,
      "authority": 0.9,
      "need": 0.95,
      "timeline": 0.7
    },
    "overall_score": 0.84,
    "qualification_status": "qualified_and_booked"
  }
}
```

### 4.4 Property Intelligence
```
GET /api/v1/call-analysis/property-intelligence/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "property_intelligence": {
    "property_address": "157 S Sunland Gin Rd",
    "property_type": "Single Family Home",
    "property_age": "15 years"
  }
}
```

### 4.5 Compliance (2-Layer)
```
GET /api/v1/call-analysis/compliance/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "compliance": {
    "final_decision": "pass",
    "overall_score": 85.0,
    "layer_1": {
      "compliance_score": 88.0,
      "stages_completed": [...]
    },
    "layer_2": {
      "outcome_score": 82.0,
      "call_outcome": "qualified_and_booked"
    }
  }
}
```

### 4.6 Trigger Individual Analysis
```
POST /api/v1/lead-qualification/qualify

{
  "call_id": 12345,
  "analysis_type": "full"
}
```

---

## 5. Lead Qualification & Intent Classification

**File:** `services/api/app/routes/v1/lead_qualification.py`

### Purpose
Qualifies leads using **BANT criteria** (Budget, Authority, Need, Timeline) and classifies **call intent**.

### Intent Categories

| Intent Status | Description | When Used |
|---------------|-------------|-----------|
| `qualified_and_booked` | Lead is qualified and appointment booked | High intent, ready to buy |
| `qualified_unbooked` | Lead is qualified but no appointment yet | Good lead, needs follow-up |
| `not_qualified` | Lead doesn't meet BANT criteria | Low budget/authority/need |
| `qualified_service_not_offered` | Lead is qualified but we don't offer service | Wrong service type |
| `nurture` | Lead has potential but needs time | Follow up later |

### How It Works

1. **Analyzes transcript** using LLM
2. **Scores BANT** (0.0 - 1.0 each)
3. **Calculates overall score** (average of BANT)
4. **Classifies intent** based on:
   - Overall score threshold
   - Appointment booking status
   - Service availability
   - Timeline urgency

### Endpoints

#### Trigger Qualification
```
POST /api/v1/lead-qualification/qualify

{
  "call_id": 12345,
  "analysis_type": "full"
}
```

#### Check Status
```
GET /api/v1/lead-qualification/status/{call_id}
```

Response:
```json
{
  "success": true,
  "call_id": 12345,
  "has_qualification": true,
  "qualification_status": "qualified_and_booked",
  "overall_score": 0.84
}
```

### BANT Score Calculation

```python
# Budget (0.0 - 1.0)
- Budget discussed: +0.5
- Budget confirmed: +0.5
- Financing mentioned: +0.3

# Authority (0.0 - 1.0)
- Decision maker on call: +0.8
- Needs approval: +0.3
- Can't decide: 0.0

# Need (0.0 - 1.0)
- Urgent problem: +0.9
- Nice to have: +0.5
- No clear need: 0.0

# Timeline (0.0 - 1.0)
- Immediate (< 1 week): +0.9
- Short term (1-4 weeks): +0.7
- Long term (> 1 month): +0.3
```

---

## 6. Meeting Segmentation

Segments sales appointments into two distinct parts for better analysis and coaching.

### Purpose
Automatically divides sales appointments into:
- **Part 1: Rapport/Agenda** - Relationship building, agenda setting, needs discovery
- **Part 2: Proposal/Close** - Presentation, proposal delivery, closing

### Use Cases
- **Sales Coaching** - Identify if rep is rushing to close
- **Performance Analysis** - Balance between rapport and presentation
- **Training** - Show examples of proper meeting structure
- **Quality Assurance** - Ensure proper sales process

### Endpoints

#### Trigger Segmentation Analysis
```
POST /api/v1/meeting-segmentation/analyze

{
  "call_id": 12345,
  "analysis_type": "full"
}
```

#### Get Existing Analysis
```
GET /api/v1/meeting-segmentation/analysis/{call_id}
```

#### Check Status
```
GET /api/v1/meeting-segmentation/status/{call_id}
```

### Response Structure
```json
{
  "success": true,
  "call_id": 12345,
  "part1": {
    "start_time": 0.0,
    "end_time": 245.5,
    "duration": 245.5,
    "content": "Rep opened with warm greeting, built rapport discussing customer's recent vacation. Set clear agenda: discuss roof inspection needs, review options, and provide pricing. Conducted thorough needs assessment about current roof condition and leak issues.",
    "key_points": [
      "Built rapport - discussed vacation",
      "Set agenda for call",
      "Identified urgent leak issue",
      "Discussed timeline - wants quick resolution"
    ]
  },
  "part2": {
    "start_time": 245.5,
    "end_time": 480.0,
    "duration": 234.5,
    "content": "Rep presented three roofing options with clear pros/cons. Provided detailed pricing for each. Addressed budget concerns with financing options. Successfully closed by booking inspection appointment for next day at 2pm.",
    "key_points": [
      "Presented 3 options with pricing",
      "Addressed budget objections",
      "Offered financing",
      "Booked appointment for tomorrow 2pm"
    ]
  },
  "segmentation_confidence": 0.92,
  "transition_point": 245.5,
  "transition_indicators": [
    "Rep said: 'Now let me show you what we can do for you'",
    "Shifted from questions to presentation",
    "Started discussing specific products and pricing"
  ],
  "meeting_structure_score": 4,
  "call_type": "sales_appointment",
  "created_at": "2025-11-16T10:30:00Z"
}
```

### What Gets Analyzed

#### Part 1 Indicators
- Greeting and rapport building
- Agenda setting phrases
- Discovery questions
- Needs assessment
- Problem identification
- Timeline discussion

#### Part 2 Indicators
- "Let me show you..."
- Product/service presentation
- Pricing discussion
- Proposal delivery
- Objection handling
- Closing techniques
- Appointment booking

### Meeting Structure Score

| Score | Quality | Description |
|-------|---------|-------------|
| 5 | Excellent | Perfect balance, clear transition, thorough rapport and close |
| 4 | Good | Good structure, may be slightly unbalanced |
| 3 | Fair | Acceptable structure, one part may be weak |
| 2 | Poor | Rushed or unbalanced, missing key elements |
| 1 | Bad | No clear structure, jumped straight to pitch or never closed |

### Segmentation Confidence

| Confidence | Meaning |
|------------|---------|
| 0.9 - 1.0 | Very clear transition point identified |
| 0.7 - 0.9 | Clear transition, some ambiguity |
| 0.5 - 0.7 | Moderate confidence, may have multiple transitions |
| < 0.5 | Low confidence, unclear structure |

### Example Use Cases

#### Use Case 1: Coaching Feedback
```bash
# Get segmentation
GET /api/v1/meeting-segmentation/analysis/12345

# Analyze results
if part1_duration < 120:
    feedback = "Rep rushed through rapport building. Spend more time in discovery."
elif part1_duration > 400:
    feedback = "Rep spent too much time in discovery. Move to proposal sooner."
else:
    feedback = "Good balance between rapport and presentation."
```

#### Use Case 2: Performance Metrics
```python
# Calculate ideal structure
total_duration = part1_duration + part2_duration
part1_percentage = (part1_duration / total_duration) * 100

# Ideal: 40-50% rapport, 50-60% proposal
if 40 <= part1_percentage <= 50:
    structure_quality = "Excellent"
elif 30 <= part1_percentage < 40 or 50 < part1_percentage <= 60:
    structure_quality = "Good"
else:
    structure_quality = "Needs improvement"
```

#### Use Case 3: Training Examples
```bash
# Find calls with excellent structure
GET /api/v1/meeting-segmentation/analysis?meeting_structure_score=5

# Use as training examples for new reps
```

### Analysis Types

| Type | Description | Speed | Use When |
|------|-------------|-------|----------|
| `full` | Complete LLM analysis | Slower | First time or when updating |
| `quick` | Return cached results | Fast | Retrieving existing analysis |

### Integration with Other APIs

Meeting segmentation complements other analysis:

```bash
# Get complete picture
1. GET /api/v1/meeting-segmentation/analysis/{call_id}
2. GET /api/v1/call-analysis/compliance/{call_id}
3. GET /api/v1/call-analysis/qualification/{call_id}

# Analysis flow
Meeting Structure (4/5) → Part 1 had good rapport
                       → Part 2 closed successfully
                       → Overall: qualified_and_booked
```

---

## 7. Property Intelligence

Extracts property information from calls (useful for home services, real estate, etc.).

### Endpoint
```
GET /api/v1/call-analysis/property-intelligence/{call_id}
```

### What It Extracts

- **Property Address** - Full address mentioned in call
- **Property Type** - Single family, condo, commercial, etc.
- **Property Age** - Estimated or stated age
- **Property Condition** - Current state, issues
- **Property Value** - Estimated value (if mentioned)
- **Additional Notes** - Roof type, square footage, etc.

### Example Response
```json
{
  "success": true,
  "call_id": 12345,
  "property_intelligence": {
    "property_address": "157 S Sunland Gin Rd, Mesa, AZ",
    "property_type": "Single Family Home",
    "property_age": "15 years (built 2010)",
    "property_condition": "Good overall, roof needs repair",
    "property_value": "Estimated $350,000",
    "additional_notes": "Asphalt shingle roof, 2-car garage, leak over garage bay"
  }
}
```

### Use Cases

- **Roofing:** Property address, roof type, age
- **HVAC:** Square footage, system age
- **Solar:** Property orientation, roof condition
- **Real Estate:** Property details, value

---

## 8. Personal Otto Training

Train AI clones that learn your communication style for personalized follow-ups.

### Training Pipeline

```
1. Upload Training Samples
   ↓
2. System Extracts Features
   ↓
3. Train AI Profile
   ↓
4. Profile Stored
   ↓
5. Use for Personalization
```

### Step 1: Upload Training Documents

```
POST /api/v1/personal-otto/ingest/training-documents
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>
```

**Request:**
```json
{
  "training_examples": [
    {
      "message_text": "Hi Sarah! Confirming your roof inspection tomorrow at 2pm. We'll check that leak over the garage. See you then!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hey John! Following up on that metal roof quote we discussed. Ready to lock in install dates for next week? 😊",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hi Kelly! Just sent over the revised quote with those upgrade options. Take a look and let me know your thoughts!",
      "context": "follow_up",
      "outcome": "positive"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "user_id": "user_123",
  "company_id": "test_company_1",
  "target_role": "sales_rep",
  "examples_ingested": 3,
  "total_examples": 3,
  "message": "Training examples ingested successfully"
}
```

### Step 2: Trigger Training

```
POST /api/v1/personal-otto/train
Authorization: Bearer <JWT_TOKEN>
```

**Request:**
```json
{
  "force_retrain": false
}
```

**Response:**
```json
{
  "success": true,
  "message": "Training started",
  "job_id": "train_user123_20251116_103045",
  "user_id": "user_123",
  "target_role": "sales_rep",
  "training_examples_count": 10,
  "estimated_time": "2-3 minutes"
}
```

### Step 3: Check Training Status

```
GET /api/v1/personal-otto/profile/status
```

**Response:**
```json
{
  "success": true,
  "user_id": "user_123",
  "target_role": "sales_rep",
  "profile_exists": true,
  "training_status": "completed",
  "profile_confidence": 0.85,
  "training_examples_count": 10,
  "last_training_date": "2025-11-16T10:30:00Z",
  "is_active": true,
  "can_retrain": true
}
```

### Training Requirements

- **Minimum:** 10 training examples
- **Recommended:** 20-30 examples
- **Optimal:** 50+ examples

### What AI Profile Learns

#### Statistical Features (10 metrics)
1. **Average Message Length** - Character count
2. **Emoji Usage** - Frequency (0.0-1.0)
3. **First-Person Percentage** - Use of "I", "my", "me"
4. **Team Voice Percentage** - Use of "we", "our", "us"
5. **Contractions Percentage** - "I'll", "can't", etc.
6. **Uses Name in Greeting** - Frequency
7. **Uses Name in Body** - Frequency
8. **Warmth Word Count** - "great", "excited", etc.
9. **Positive Word Percentage** - Friendly language
10. **Signature Phrases** - Your unique expressions

#### LLM-Extracted Features (8 metrics)
1. **Tone** - friendly, formal, casual, professional
2. **Formality Level** - 0.0 (casual) to 1.0 (formal)
3. **Warmth Level** - 0.0 (transactional) to 1.0 (warm)
4. **Enthusiasm Level** - 0.0 (neutral) to 1.0 (enthusiastic)
5. **Greeting Style** - "Hi [name]!", "Hey there!", etc.
6. **Closing Style** - "Thanks!", "See you then!", etc.
7. **Vocabulary Level** - simple, moderate, advanced
8. **Question Style** - direct, soft, mixed

---

## 9. Follow-up Recommendations

Generate follow-up SMS messages (personalized or generic).

### Endpoint
```
GET /api/v1/call-analysis/followup-recommendations/{call_id}?personalize=true
Authorization: Bearer <JWT_TOKEN>
```

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `personalize` | boolean | `false` | Use AI profile for personalization |

### Use Cases

#### Case 1: Personalized (AI Profile Exists)
```
GET /api/v1/call-analysis/followup-recommendations/12345?personalize=true
```

**Response:**
```json
{
  "success": true,
  "call_id": 12345,
  "recommendation": {
    "type": "follow_up_text",
    "priority": "high",
    "suggested_timing": "immediate",
    "suggested_message": "Hi Kelly! Confirming your roof inspection tomorrow at 2pm. We'll check that leak over the garage. See you then! 😊",
    "reasoning": "Booked appointment needs confirmation, personalized with rep's warm style"
  },
  "personalization": {
    "personalized": true,
    "profile_used": true,
    "profile_confidence": 0.85,
    "style_applied": {
      "tone": "friendly",
      "warmth_level": 0.8,
      "greeting_style": "Hi [name]!",
      "uses_emoji": true
    }
  }
}
```

#### Case 2: Generic Fallback (No AI Profile)
```
GET /api/v1/call-analysis/followup-recommendations/12345?personalize=false
```

**Response:**
```json
{
  "success": true,
  "call_id": 12345,
  "recommendation": {
    "type": "follow_up_text",
    "priority": "high",
    "suggested_timing": "immediate",
    "suggested_message": "Hi! Confirming your roof inspection tomorrow at 2pm at 157 S Sunland Gin Rd. Looking forward to helping you!",
    "reasoning": "Booked appointment confirmation with generic professional tone"
  },
  "personalization": {
    "personalized": false,
    "profile_used": false,
    "fallback_reason": "No AI profile found",
    "style_applied": {
      "tone": "professional",
      "warmth_level": 0.6,
      "greeting_style": "Hi!",
      "uses_emoji": false
    }
  }
}
```

#### Case 3: Low Confidence Fallback
```
GET /api/v1/call-analysis/followup-recommendations/12345?personalize=true
```

**Response:**
```json
{
  "success": true,
  "call_id": 12345,
  "recommendation": {
    "type": "follow_up_text",
    "priority": "medium",
    "suggested_timing": "24_hours",
    "suggested_message": "Hi! Following up on our conversation about your project. Ready to schedule that appointment? Let me know a good time!",
    "reasoning": "Qualified lead needs appointment booking"
  },
  "personalization": {
    "personalized": false,
    "profile_used": false,
    "fallback_reason": "Profile confidence too low (0.45 < 0.7 threshold)",
    "style_applied": {
      "tone": "professional",
      "warmth_level": 0.6
    }
  }
}
```

### Message Types

| Type | Description | Example Use |
|------|-------------|-------------|
| `follow_up_text` | General follow-up | After call ended |
| `schedule_appointment` | Booking request | Qualified but unbooked |
| `detail_request` | More info needed | Missing property details |

### Priority Levels

| Priority | When | Suggested Timing |
|----------|------|------------------|
| `high` | Booked appointment | Immediate |
| `medium` | Qualified lead | 4-24 hours |
| `low` | Nurture lead | 48+ hours |

### Timing Suggestions

- **immediate** - Send within 1 hour
- **4_hours** - Send within 4 hours
- **24_hours** - Send within 24 hours
- **48_hours** - Send within 48 hours

---

## 10. View AI Profile

View the complete AI profile that was trained for a user.

### Endpoint
```
GET /api/v1/personal-otto/profile
Authorization: Bearer <JWT_TOKEN>
```

### Response
```json
{
  "success": true,
  "profile": {
    "profile_id": 456,
    "user_id": "user_123",
    "company_id": "test_company_1",
    "target_role": "sales_rep",
    "version": 3,
    "profile_confidence": 0.85,
    "is_active": true,
    "is_auto_training_enabled": false,
    
    "communication_style": {
      "statistical_features": {
        "avg_message_length": 145,
        "emoji_usage_frequency": 0.7,
        "first_person_percentage": 0.6,
        "team_voice_percentage": 0.2,
        "contractions_percentage": 0.5,
        "uses_name_in_greeting": 0.9,
        "uses_name_in_body": 0.3,
        "warmth_word_count": 8,
        "positive_word_percentage": 0.75,
        "signature_phrases": ["See you then!", "Looking forward to it!"]
      },
      "llm_features": {
        "tone": "friendly",
        "formality_level": 0.4,
        "warmth_level": 0.8,
        "enthusiasm_level": 0.75,
        "greeting_style": "Hi [name]!",
        "closing_style": "See you then!",
        "vocabulary_level": "moderate",
        "question_style": "soft"
      }
    },
    
    "followup_preferences": {
      "preferred_timing": "immediate",
      "preferred_message_length": "medium",
      "include_emoji": true,
      "include_call_details": true
    },
    
    "training_calls_count": 25,
    "last_training_date": "2025-11-16T10:30:00Z",
    "created_at": "2025-11-15T08:00:00Z",
    "updated_at": "2025-11-16T10:30:00Z",
    "training_examples_count": 25,
    "training_status": "completed",
    "training_started_at": "2025-11-16T10:28:00Z"
  }
}
```

### Profile Not Found
```json
{
  "error": "profile_not_found",
  "message": "No AI profile found for user user_123 with role sales_rep",
  "user_id": "user_123",
  "target_role": "sales_rep",
  "suggestion": "Upload training examples and trigger training to create a profile"
}
```

### Understanding Profile Confidence

| Confidence | Quality | Recommendation |
|------------|---------|----------------|
| 0.9 - 1.0 | Excellent | Ready for production |
| 0.7 - 0.9 | Good | Can be used, monitor results |
| 0.5 - 0.7 | Fair | Add more training examples |
| < 0.5 | Poor | Need significantly more data |

---

## 11. Sample Payloads

### 11.1 Training Examples (Personal Otto)

**Minimum Required (10 examples):**
```json
{
  "training_examples": [
    {
      "message_text": "Hi Sarah! Confirming your roof inspection tomorrow at 2pm. We'll check that leak over the garage. See you then!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hey John! Following up on that metal roof quote we discussed. Ready to lock in install dates for next week? 😊",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hi Kelly! Just sent over the revised quote with those upgrade options. Take a look and let me know your thoughts!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Good morning! All set for your 2pm site visit tomorrow at 157 S Sunland Gin Rd. Looking forward to helping you!",
      "context": "appointment_confirmation",
      "outcome": "positive"
    },
    {
      "message_text": "Hey there! Checking in on your roof project. Have you had a chance to review the proposal I sent? Happy to answer any questions!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hi Mike! Thanks for chatting earlier. I'll get that detailed breakdown to you by end of day. Talk soon!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Hey Lisa! Just wanted to confirm we're still on for Thursday at 10am. Excited to show you the material samples! 🏠",
      "context": "appointment_confirmation",
      "outcome": "positive"
    },
    {
      "message_text": "Hi David! Great talking to you today. I'll send over those financing options we discussed. Let me know if you have questions!",
      "context": "follow_up",
      "outcome": "positive"
    },
    {
      "message_text": "Good afternoon! Your estimate is ready. I've included the options we talked about. Take a look and let's schedule that install!",
      "context": "quote_delivery",
      "outcome": "positive"
    },
    {
      "message_text": "Hi Amanda! Following up on your call about the roof warranty. I've got all the details ready. Can we chat tomorrow?",
      "context": "follow_up",
      "outcome": "positive"
    }
  ]
}
```

### 11.2 Meeting Segmentation Request

**Trigger Analysis:**
```json
{
  "call_id": 12345,
  "analysis_type": "full"
}
```

**Quick Retrieval:**
```json
{
  "call_id": 12345,
  "analysis_type": "quick"
}
```

### 11.3 SOP Actions (Approve/Reject Stages)

**Approve Stage:**
```json
{
  "stage_id": 123,
  "action": "approve",
  "approved_by": "manager_456",
  "notes": "Stage description is clear and actionable"
}
```

**Reject Stage:**
```json
{
  "stage_id": 124,
  "action": "reject",
  "rejected_by": "manager_456",
  "reason": "Stage description too vague, needs more specific criteria",
  "suggested_changes": "Add specific questions to ask during needs assessment"
}
```

### 11.4 Complete Call Processing Request

**Upload Call:**
```json
{
  "call_id": 12345,
  "company_id": "test_company_1",
  "audio_url": "s3://otto-calls/12345.mp3",
  "metadata": {
    "caller_phone": "+1234567890",
    "rep_id": "user_123",
    "call_duration": 320,
    "call_date": "2025-11-16T10:00:00Z"
  }
}
```

**Trigger All Analysis:**
```json
{
  "call_id": 12345,
  "analysis_types": [
    "summary",
    "objections",
    "qualification",
    "property_intelligence",
    "compliance"
  ]
}
```

### 11.5 Follow-up Request (All Scenarios)

**Scenario 1: Personalized for Booked Appointment**
```
GET /api/v1/call-analysis/followup-recommendations/12345?personalize=true

Call Context:
- qualified_and_booked
- Appointment: Tomorrow 2pm
- Property: 157 S Sunland Gin Rd
- Issue: Roof leak
```

**Scenario 2: Generic for Qualified Lead**
```
GET /api/v1/call-analysis/followup-recommendations/12346?personalize=false

Call Context:
- qualified_unbooked
- Interested in metal roof
- Needs quote
```

**Scenario 3: Personalized for Service Not Offered**
```
GET /api/v1/call-analysis/followup-recommendations/12347?personalize=true

Call Context:
- qualified_service_not_offered
- Wanted solar panels (we do roofing)
- Good lead, wrong service
```

---

## New Features Summary

### ✅ Feature 1: 2-Layer Compliance Processing (Sales)

**What:** Two-level SOP compliance evaluation
- **Layer 1:** Stage-by-stage adherence check (88% score)
- **Layer 2:** Overall call outcome evaluation (82% score)
- **Final Decision:** Pass/Fail based on both layers

**Endpoint:** `GET /api/v1/call-analysis/compliance/{call_id}`

---

### ✅ Feature 2: Lead Qualification with Intent Classification

**What:** BANT scoring + intent categorization
- **BANT Scores:** Budget, Authority, Need, Timeline (0.0-1.0 each)
- **Intent Categories:** `qualified_and_booked`, `qualified_unbooked`, `not_qualified`, `qualified_service_not_offered`, `nurture`

**Endpoint:** `POST /api/v1/lead-qualification/qualify`

---

### ✅ Feature 3: Property Intelligence Extraction

**What:** Extracts property details from call
- Address, type, age, condition, value
- Useful for home services (roofing, HVAC, solar)

**Endpoint:** `GET /api/v1/call-analysis/property-intelligence/{call_id}`

---

### ✅ Feature 4: Meeting Segmentation

**What:** Segments sales appointments into two parts
- **Part 1:** Rapport/Agenda (40-50% ideal)
- **Part 2:** Proposal/Close (50-60% ideal)
- Structure scoring (1-5 scale)
- Coaching and training insights

**Endpoints:**
- `POST /api/v1/meeting-segmentation/analyze`
- `GET /api/v1/meeting-segmentation/analysis/{call_id}`

---

### ✅ Feature 5: Personal Otto Training

**What:** Train AI clones from communication samples
- Learns 18 style features (10 statistical + 8 LLM)
- Minimum 10 examples, optimal 50+
- Version control and confidence scoring

**Endpoints:**
- `POST /api/v1/personal-otto/ingest/training-documents`
- `POST /api/v1/personal-otto/train`

---

### ✅ Feature 6: Personalized Follow-up Generation

**What:** Generate follow-ups in rep's style
- Personalized if AI profile exists (confidence > 0.7)
- Fallback to generic professional tone
- Context-aware (appointment, quote, nurture)

**Endpoint:** `GET /api/v1/call-analysis/followup-recommendations/{call_id}?personalize=true`

---

### ✅ Feature 7: View AI Profile

**What:** Inspect trained AI profile
- Communication style details
- Training metadata
- Confidence score

**Endpoint:** `GET /api/v1/personal-otto/profile`

---

### ✅ Feature 8: SOP Processing & Actions

**What:** Upload, extract, approve/reject SOP stages
- Automatic stage extraction from PDFs
- Role-based targeting (sales_rep, customer_rep)
- Approval workflow

**Endpoint:** `POST /api/v1/ingestion/sop-documents`

---

## Authentication

All endpoints require JWT token:

```
Authorization: Bearer <JWT_TOKEN>
```

**Token contains:**
- `user_id` - User identifier
- `company_id` - Company identifier
- `role` - User role (sales_rep, customer_rep, manager, etc.)

---

## Error Responses

### Standard Error Format
```json
{
  "error": "error_code",
  "message": "Human-readable error message",
  "details": {
    "field": "Additional context"
  }
}
```

### Common Errors

| Code | Status | Description |
|------|--------|-------------|
| `profile_not_found` | 404 | No AI profile exists for user |
| `insufficient_training_data` | 400 | Less than 10 training examples |
| `training_in_progress` | 409 | Training already running |
| `call_not_found` | 404 | Call ID doesn't exist |
| `analysis_not_ready` | 404 | Analysis not completed yet |
| `invalid_token` | 401 | JWT token invalid or expired |

---

## Rate Limits

| Endpoint Type | Limit | Window |
|---------------|-------|--------|
| Training | 5 requests | 1 hour |
| Analysis | 100 requests | 1 minute |
| Follow-ups | 1000 requests | 1 hour |

---

## Support

For questions or issues:
- Documentation: `/docs` (Swagger UI)
- API Health: `GET /health`
- Version: `GET /version`

---

**End of Documentation**  
Version: Phase 1 - Personal Otto + 2-Layer Compliance  
Last Updated: November 16, 2025

