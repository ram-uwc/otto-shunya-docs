# Otto AI - Quick Reference Guide

**TL;DR:** Fast access to all endpoints and workflows

---

## 🚀 Quick Start Workflows

### Workflow 1: Process a Call (Complete)
```bash
# 1. Upload call audio
POST /api/v1/calls/upload

# 2. Wait for processing (automatic)
# System runs: transcription → summary → objections → qualification → property → compliance

# 3. Get all results
GET /api/v1/call-analysis/analysis/complete/{call_id}
```

### Workflow 2: Train Personal Otto
```bash
# 1. Upload training examples (min 10)
POST /api/v1/personal-otto/ingest/training-documents

# 2. Trigger training
POST /api/v1/personal-otto/train

# 3. Check status
GET /api/v1/personal-otto/profile/status

# 4. View profile
GET /api/v1/personal-otto/profile
```

### Workflow 3: Generate Follow-up
```bash
# Personalized (if profile exists)
GET /api/v1/call-analysis/followup-recommendations/{call_id}?personalize=true

# Generic
GET /api/v1/call-analysis/followup-recommendations/{call_id}?personalize=false
```

---

## 📋 All Endpoints Cheat Sheet

### SOP Management
```
POST   /api/v1/ingestion/sop-documents        Upload SOP (PDF/DOCX)
GET    /api/v1/sop/stages                     List all SOP stages
```

### Call Analysis
```
GET    /api/v1/call-analysis/status/{call_id}                   Check processing status
GET    /api/v1/call-analysis/analysis/complete/{call_id}        Get all analyses
GET    /api/v1/call-analysis/summary/{call_id}                  Get summary only
GET    /api/v1/call-analysis/objections/{call_id}               Get objections only
GET    /api/v1/call-analysis/qualification/{call_id}            Get qualification only
GET    /api/v1/call-analysis/property-intelligence/{call_id}    Get property info only
GET    /api/v1/call-analysis/compliance/{call_id}               Get compliance (2-layer)
```

### Lead Qualification
```
POST   /api/v1/lead-qualification/qualify            Trigger qualification
GET    /api/v1/lead-qualification/status/{call_id}   Check qualification status
```

### Meeting Segmentation
```
POST   /api/v1/meeting-segmentation/analyze          Trigger segmentation analysis
GET    /api/v1/meeting-segmentation/analysis/{call_id}   Get segmentation results
GET    /api/v1/meeting-segmentation/status/{call_id}     Check segmentation status
```

### Personal Otto
```
POST   /api/v1/personal-otto/ingest/training-documents    Upload training examples
POST   /api/v1/personal-otto/train                        Trigger training
GET    /api/v1/personal-otto/profile/status               Check training status
GET    /api/v1/personal-otto/profile                      View AI profile
```

### Follow-ups
```
GET    /api/v1/call-analysis/followup-recommendations/{call_id}?personalize=true|false
```

---

## 🎯 Sample Requests

### Upload Training Examples
```bash
curl -X POST "https://api.otto.ai/api/v1/personal-otto/ingest/training-documents" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "training_examples": [
      {
        "message_text": "Hi Sarah! Confirming your appointment at 2pm tomorrow. See you then!",
        "context": "follow_up",
        "outcome": "positive"
      }
    ]
  }'
```

### Get Complete Analysis
```bash
curl -X GET "https://api.otto.ai/api/v1/call-analysis/analysis/complete/12345" \
  -H "Authorization: Bearer <token>"
```

### Get Personalized Follow-up
```bash
curl -X GET "https://api.otto.ai/api/v1/call-analysis/followup-recommendations/12345?personalize=true" \
  -H "Authorization: Bearer <token>"
```

### Trigger Meeting Segmentation
```bash
curl -X POST "https://api.otto.ai/api/v1/meeting-segmentation/analyze" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "call_id": 12345,
    "analysis_type": "full"
  }'
```

---

## 📊 Intent Categories

| Intent | Description |
|--------|-------------|
| `qualified_and_booked` | Ready to buy, appointment set |
| `qualified_unbooked` | Good lead, needs follow-up |
| `not_qualified` | Low BANT scores |
| `qualified_service_not_offered` | Good lead, wrong service |
| `nurture` | Potential, needs time |

---

## 🎨 Response Structures

### Complete Analysis Response (Simplified)
```json
{
  "success": true,
  "call_id": 12345,
  "analyses": {
    "summary": { "summary_text": "...", "key_points": [] },
    "objections": { "objections": [], "total_count": 0 },
    "qualification": { "bant_scores": {}, "qualification_status": "" },
    "property_intelligence": { "property_address": "" },
    "compliance": { "final_decision": "pass", "overall_score": 85 }
  }
}
```

### Follow-up Response (Personalized)
```json
{
  "success": true,
  "recommendation": {
    "suggested_message": "Hi Kelly! Confirming your appointment...",
    "priority": "high",
    "suggested_timing": "immediate"
  },
  "personalization": {
    "personalized": true,
    "profile_confidence": 0.85
  }
}
```

### AI Profile Response
```json
{
  "success": true,
  "profile": {
    "profile_confidence": 0.85,
    "communication_style": {
      "statistical_features": { "avg_message_length": 145 },
      "llm_features": { "tone": "friendly", "warmth_level": 0.8 }
    },
    "training_examples_count": 25
  }
}
```

### Meeting Segmentation Response
```json
{
  "success": true,
  "call_id": 12345,
  "part1": {
    "duration": 245.5,
    "content": "Rapport building and discovery",
    "key_points": ["Built rapport", "Set agenda", "Identified needs"]
  },
  "part2": {
    "duration": 234.5,
    "content": "Presentation and closing",
    "key_points": ["Presented options", "Closed appointment"]
  },
  "meeting_structure_score": 4,
  "segmentation_confidence": 0.92
}
```

---

## ⚡ Common Use Cases

### Use Case 1: Check if Call is Ready
```bash
GET /api/v1/call-analysis/status/{call_id}

# Look for:
# "status": "completed"
# "progress": 100
```

### Use Case 2: Get Just the Intent
```bash
GET /api/v1/call-analysis/qualification/{call_id}

# Returns:
# "qualification_status": "qualified_and_booked"
```

### Use Case 3: Check if Profile is Trained
```bash
GET /api/v1/personal-otto/profile/status

# Look for:
# "profile_exists": true
# "training_status": "completed"
# "profile_confidence": 0.85
```

### Use Case 4: Force Retrain
```bash
POST /api/v1/personal-otto/train
{
  "force_retrain": true
}
```

### Use Case 5: Check Meeting Structure
```bash
GET /api/v1/meeting-segmentation/analysis/{call_id}

# Evaluate balance:
# Part 1 (Rapport): Should be 40-50% of total time
# Part 2 (Close): Should be 50-60% of total time
# Structure Score: 4-5 is good
```

---

## 🔑 Authentication

All requests need JWT token:
```bash
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

Token contains:
- `user_id`
- `company_id`
- `role`

---

## ❌ Common Errors

| Error | Fix |
|-------|-----|
| `profile_not_found` | Upload training examples and train |
| `insufficient_training_data` | Need minimum 10 examples |
| `training_in_progress` | Wait for current training to finish |
| `call_not_found` | Check call_id exists |
| `analysis_not_ready` | Wait for processing to complete |

---

## 📈 Training Requirements

| Examples | Quality | Confidence |
|----------|---------|------------|
| 10-20 | Minimum | 0.5-0.7 |
| 20-30 | Good | 0.7-0.85 |
| 50+ | Excellent | 0.85-0.95 |

---

## 🎯 Priority & Timing

### Message Priority
- **high** → Send immediately (booked appointments)
- **medium** → Send within 4-24 hours (qualified leads)
- **low** → Send within 48+ hours (nurture leads)

### Suggested Timing
- **immediate** → Within 1 hour
- **4_hours** → Within 4 hours
- **24_hours** → Within 24 hours
- **48_hours** → Within 48 hours

---

## 📱 Message Examples

### Personalized (Warm, Friendly)
```
"Hi Kelly! Confirming your roof inspection tomorrow at 2pm. 
We'll check that leak over the garage. See you then! 😊"
```

### Generic (Professional)
```
"Hi! Confirming your roof inspection tomorrow at 2pm at 
157 S Sunland Gin Rd. Looking forward to helping you!"
```

