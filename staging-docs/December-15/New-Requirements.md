# Otto AI RAG - Client API Documentation

**Base URL:** `https://otto.shunyalabs.ai`

**Authentication:** All endpoints require JWT Bearer token in the `Authorization` header.

---

## Table of Contents

1. [Call Transcription](#call-transcription)
2. [Call Analysis](#call-analysis)
3. [SMS/Text Analysis](#sms-text-analysis)

---

## Call Transcription

### POST `/api/v1/transcription/transcribe`

Transcribe audio and trigger analysis pipeline.

#### Request

**Headers:**
```
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**
```json
{
  "call_id": 12345,
  "audio_url": "https://s3.amazonaws.com/bucket/audio.mp3",
  "call_type": "csr_call",
  "timezone": "America/Phoenix",
  "call_started_at": "2025-01-15T10:00:00-07:00"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `call_id` | integer | Yes | Unique identifier for the call |
| `audio_url` | string | Yes | Publicly accessible URL to the audio file |
| `call_type` | string | No | Type of call: `"sales_call"` or `"csr_call"` (default: `"sales_call"`) |
| `timezone` | string | No | IANA timezone (e.g., `"America/Phoenix"`). **Recommended** for accurate appointment time parsing. If not provided, analysis will use UTC and confidence scores will be lower (0.3-0.5). |
| `call_started_at` | string | No | ISO 8601 datetime when call started. Can be in local time with timezone (e.g., `"2025-01-15T10:00:00-07:00"`) or UTC (e.g., `"2025-01-15T17:00:00+00:00"`). Must be timezone-aware. Used for parsing relative times like "tomorrow at 4" or "next Friday morning". **RECOMMENDED:** Send in local time with timezone for best accuracy. |

**Example Request:**
```bash
curl -X POST 'https://otto.shunyalabs.ai/api/v1/transcription/transcribe' \
  -H 'Authorization: Bearer YOUR_JWT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "call_id": 12345,
    "audio_url": "https://s3.amazonaws.com/bucket/audio.mp3",
    "call_type": "csr_call",
    "timezone": "America/Phoenix",
    "call_started_at": "2025-01-15T10:00:00-07:00"
  }'
```

#### Response

**Success (200):**
```json
{
  "success": true,
  "message": "Transcription started successfully",
  "transcript_id": 789,
  "task_id": "abc123-def456-ghi789"
}
```

**Error (400/404/500):**
```json
{
  "error": "Error message",
  "message": "Detailed error description"
}
```

---

## Call Analysis

### GET `/api/v1/analysis/complete/{call_id}`

Get complete analysis results for a call, including all analysis components.

#### Request

**Headers:**
```
Authorization: Bearer <JWT_TOKEN>
```

**Path Parameters:**
- `call_id` (integer, required) - The call ID to get analysis for

**Example Request:**
```bash
curl -X GET 'https://otto.shunyalabs.ai/api/v1/analysis/complete/12345' \
  -H 'Authorization: Bearer YOUR_JWT_TOKEN'
```

#### Response

**Success (200):**
```json
{
  "call_id": 12345,
  "status": "completed",
  "summary": {
    "summary": "Customer called to schedule a roof repair appointment...",
    "key_points": [
      "Customer has urgent leak",
      "Scheduled for tomorrow at 2pm",
      "Address: 1234 Main St, Phoenix, AZ"
    ],
    "action_items": ["Follow up on appointment"],
    "next_steps": ["Send confirmation email"],
    "pending_actions": [
      {
        "type": "call_back",
        "due_at": "2025-01-16T14:00:00-07:00",
        "contact_method": "phone",
        "confidence": 0.9,
        "raw_text": "Customer asked to call back tomorrow"
      }
    ],
    "sentiment_score": 0.7,
    "confidence_score": 0.85
  },
  "compliance": {
    "call_id": 12345,
    "target_role": "customer_rep",
    "evaluation_mode": "two_layer",
    "final_outcome": "pass",
    "final_reasoning": "SOP compliance met and positive outcome achieved",
    "primary_factor": "sop_compliance",
    "sop_compliance": {
      "compliance_score": 0.92,
      "compliance_rate": 92,
      "total_stages": 5,
      "stages_followed": 5,
      "stages_missed": 0,
      "positive_behaviors": ["Greeted customer", "Listened actively"],
      "compliance_issues": []
    },
    "outcome_score": {
      "overall_outcome_score": 85,
      "has_critical_error": false,
      "strengths": ["Clear communication"],
      "coaching_recommendations": []
    }
  },
  "objections": {
    "objections": [
      {
        "id": 1,
        "category_id": 5,
        "category_text": "Price Concern",
        "objection_text": "That seems expensive",
        "overcome": true,
        "speaker_id": "home_owner_1",
        "timestamp": 120.5,
        "confidence_score": 0.9,
        "severity": "medium",
        "response_suggestions": ["Emphasize value", "Offer payment plans"],
        "created_at": "2025-01-15T10:05:00Z"
      }
    ],
    "total_count": 1,
    "no_objections_reason": null
  },
  "qualification": {
    "bant_scores": {
      "budget": 0.7,
      "authority": 0.8,
      "need": 0.9,
      "timeline": 0.85
    },
    "overall_score": 0.81,
    "qualification_status": "qualified",
    "decision_makers": ["John Smith"],
    "urgency_signals": ["Urgent leak", "Elderly parents at home"],
    "budget_indicators": ["Fixed income", "Asking about financing"],
    "confidence_score": 0.88,
    "booking_status": "booked",
    "call_outcome_category": "appointment_scheduled",
    "appointment_confirmed": true,
    "appointment_date": "2025-01-16T14:00:00-07:00",
    "appointment_type": "service_call",
    "appointment_timezone": "America/Phoenix",
    "appointment_time_confidence": 0.95,
    "preferred_time_window": "afternoon",
    "service_address_raw": "1234 Main Street, Phoenix, Arizona 85001",
    "service_address_structured": {
      "street": "1234 Main Street",
      "city": "Phoenix",
      "state": "Arizona",
      "zip": "85001",
      "country": "USA"
    },
    "address_confidence": 0.92,
    "appointment_intent": "new_booking",
    "original_appointment_datetime": null,
    "new_requested_time": null,
    "service_requested": "Roof repair",
    "service_not_offered_reason": null,
    "follow_up_required": false,
    "follow_up_reason": null
  },
  "opportunity_analysis": {
    "risk_assessment": {
      "level": "low",
      "score": 0.2,
      "risk_factors": [],
      "positive_factors": ["Strong need", "Urgent timeline"],
      "mitigation_strategies": []
    },
    "upgrade_opportunities": [
      {
        "type": "service_upgrade",
        "description": "Customer may benefit from full roof replacement",
        "confidence": 0.6
      }
    ],
    "missed_opportunities": []
  },
  "rep_details": {
    "rep_name": "Sarah",
    "rep_name_confidence": 0.9
  },
  "created_at": "2025-01-15T10:00:00Z",
  "completed_at": "2025-01-15T10:05:30Z"
}
```

#### Response Fields

**Top Level:**
- `call_id` (integer) - Call identifier
- `status` (string) - Analysis status: `"pending"`, `"processing"`, `"completed"`, `"failed"`
- `created_at` (string) - ISO 8601 timestamp when analysis started
- `completed_at` (string) - ISO 8601 timestamp when analysis completed

**Summary:**
- `summary` (string) - Brief summary of the call
- `key_points` (array) - Key points extracted
- `pending_actions` (array) - Structured pending actions with due dates
- `sentiment_score` (float) - Sentiment score (-1 to 1, where 1 is very positive)
- `confidence_score` (float) - Confidence in the analysis (0-1)

**Qualification (Enhanced Booking Details):**
- `booking_status` (string) - `"booked"`, `"not_booked"`, `"pending"`
- `appointment_date` (string) - ISO 8601 datetime of appointment (timezone-aware)
- `appointment_timezone` (string) - IANA timezone of appointment
- `appointment_time_confidence` (float) - Confidence in appointment time extraction (0-1)
- `preferred_time_window` (string) - Preferred time: `"morning"`, `"afternoon"`, `"evening"`
- `service_address_raw` (string) - Full address as mentioned in call
- `service_address_structured` (object) - Parsed address components:
  - `street` (string)
  - `city` (string)
  - `state` (string)
  - `zip` (string)
  - `country` (string, optional)
- `address_confidence` (float) - Confidence in address extraction (0-1)
- `appointment_intent` (string) - `"new_booking"`, `"reschedule"`, `"cancel"`
- `original_appointment_datetime` (string) - Original appointment time (for reschedules)
- `new_requested_time` (string) - New requested time (for reschedules)

**Rep Details:**
- `rep_details` (object) - Rep identification:
  - `rep_name` (string) - Detected rep name (CSR or sales rep)
  - `rep_name_confidence` (float) - Detection confidence (0-1)

**Error (404):**
```json
{
  "error": "Not Found",
  "message": "Analysis not found for call_id=12345"
}
```

---

## SMS/Text Analysis

### POST `/api/v1/sms/analyze`

Analyze SMS thread and upsert results into summary, objections, qualification tables.

**Note:** App team manages SMS threads. This endpoint receives `conversation_id` and complete thread for processing.

#### Request

**Headers:**
```
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**
```json
{
  "conversation_id": 12345,
  "messages": [
    {
      "message_id": "msg_001",
      "timestamp": "2025-01-15T10:00:00-07:00",
      "sender": "customer",
      "text": "Hi, I saw your ad online. Do you do roof repairs?"
    },
    {
      "message_id": "msg_002",
      "timestamp": "2025-01-15T10:01:00-07:00",
      "sender": "rep",
      "text": "Hi there! Yes, we do roof repairs. My name is Sarah. What kind of issue are you experiencing?"
    },
    {
      "message_id": "msg_003",
      "timestamp": "2025-01-15T10:02:00-07:00",
      "sender": "customer",
      "text": "I have a leak in my roof from the recent storm. Water is coming into my living room."
    },
    {
      "message_id": "msg_004",
      "timestamp": "2025-01-15T10:05:00-07:00",
      "sender": "customer",
      "text": "Can we schedule for tomorrow at 2pm? My address is 1234 Main Street, Phoenix, Arizona 85001"
    }
  ],
  "timezone": "America/Phoenix",
  "conversation_started_at": "2025-01-15T10:00:00-07:00"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `conversation_id` | integer | Yes | Unique identifier for the SMS conversation |
| `messages` | array | Yes | **Complete SMS thread** (all messages in chronological order) |
| `messages[].message_id` | string | Yes | Unique identifier for the message |
| `messages[].timestamp` | string | Yes | ISO 8601 datetime of the message |
| `messages[].sender` | string | Yes | Message sender: `"customer"` or `"rep"` |
| `messages[].text` | string | Yes | Message text content |
| `timezone` | string | No | IANA timezone (e.g., `"America/Phoenix"`). Used for accurate appointment time parsing. |
| `conversation_started_at` | string | No | ISO 8601 datetime when conversation started. Used for parsing relative times. |

**Example Request:**
```bash
curl -X POST 'https://otto.shunyalabs.ai/api/v1/sms/analyze' \
  -H 'Authorization: Bearer YOUR_JWT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "conversation_id": 12345,
    "messages": [
      {
        "message_id": "msg_001",
        "timestamp": "2025-01-15T10:00:00-07:00",
        "sender": "customer",
        "text": "Hi, I need roof repair"
      },
      {
        "message_id": "msg_002",
        "timestamp": "2025-01-15T10:01:00-07:00",
        "sender": "rep",
        "text": "Hi! I can help with that. My name is Sarah."
      }
    ],
    "timezone": "America/Phoenix",
    "conversation_started_at": "2025-01-15T10:00:00-07:00"
  }'
```

#### Response

**Success (200):**
```json
{
  "message": "SMS analysis started successfully",
  "conversation_id": 12345,
  "task_id": "abc123-def456-ghi789",
  "status": "pending"
}
```

**Error (400/500):**
```json
{
  "error": "Error message",
  "message": "Detailed error description"
}
```

---

### GET `/api/v1/sms/status/{conversation_id}`

Get analysis status for an SMS conversation.

#### Request

**Headers:**
```
Authorization: Bearer <JWT_TOKEN>
```

**Path Parameters:**
- `conversation_id` (integer, required) - The conversation ID

#### Response

**Success (200):**
```json
{
  "conversation_id": 12345,
  "status": "completed",
  "analysis_id": "sms_analysis_12345_company_1",
  "summarization_status": "completed",
  "objections_status": "completed",
  "qualification_status": "completed",
  "rep_details": {
    "rep_name": "Sarah",
    "rep_name_confidence": 0.9
  },
  "error_message": null,
  "retry_count": 0,
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-01-15T10:05:30Z",
  "completed_at": "2025-01-15T10:05:30Z"
}
```

---

### GET `/api/v1/sms/complete/{conversation_id}`

Get complete SMS analysis results for a conversation.

#### Request

**Headers:**
```
Authorization: Bearer <JWT_TOKEN>
```

**Path Parameters:**
- `conversation_id` (integer, required) - The conversation ID

#### Response

**Success (200):**
```json
{
  "conversation_id": 12345,
  "status": "completed",
  "summary": {
    "conversation_id": 12345,
    "summary": "Customer inquired about roof repair services...",
    "key_points": [
      "Customer has urgent leak",
      "Scheduled for tomorrow at 2pm"
    ],
    "action_items": ["Follow up on appointment"],
    "next_steps": ["Send confirmation"],
    "pending_actions": [
      {
        "type": "call_back",
        "due_at": "2025-01-16T14:00:00-07:00",
        "contact_method": "phone",
        "confidence": 0.9,
        "raw_text": "Customer asked to call back tomorrow"
      }
    ],
    "sentiment_score": 0.7,
    "confidence_score": 0.85
  },
  "objections": {
    "objections": [
      {
        "id": 1,
        "category_id": 5,
        "category_text": "Price Concern",
        "objection_text": "That seems expensive",
        "overcome": true,
        "sender": "customer",
        "message_id": "msg_005",
        "timestamp": "2025-01-15T10:08:00-07:00",
        "confidence_score": 0.9,
        "severity": "medium",
        "response_suggestions": ["Emphasize value", "Offer payment plans"]
      }
    ],
    "total_count": 1
  },
  "qualification": {
    "conversation_id": 12345,
    "bant_scores": {
      "budget": 0.7,
      "authority": 0.8,
      "need": 0.9,
      "timeline": 0.85
    },
    "overall_score": 0.81,
    "qualification_status": "qualified",
    "decision_makers": ["John Smith"],
    "urgency_signals": ["Urgent leak", "Water damage"],
    "budget_indicators": ["Fixed income", "Asking about financing"],
    "confidence_score": 0.88,
    "booking_status": "booked",
    "call_outcome_category": "appointment_scheduled",
    "appointment_confirmed": true,
    "appointment_date": "2025-01-16T14:00:00-07:00",
    "appointment_type": "service_call",
    "appointment_timezone": "America/Phoenix",
    "appointment_time_confidence": 0.95,
    "preferred_time_window": "afternoon",
    "service_address_raw": "1234 Main Street, Phoenix, Arizona 85001",
    "service_address_structured": {
      "street": "1234 Main Street",
      "city": "Phoenix",
      "state": "Arizona",
      "zip": "85001",
      "country": "USA"
    },
    "address_confidence": 0.92,
    "appointment_intent": "new_booking",
    "original_appointment_datetime": null,
    "new_requested_time": null,
    "service_requested": "Roof repair",
    "service_not_offered_reason": null,
    "follow_up_required": false,
    "follow_up_reason": null,
    "rep_details": {
      "rep_name": "Sarah",
      "rep_name_confidence": 0.9
    }
  }
}
```

**Note:** SMS qualification response includes `rep_details` within the qualification object (not as a separate top-level field).

---

## Additional Endpoints

### GET `/api/v1/analysis/status/{call_id}`

Get analysis status for a call.

**Response:**
```json
{
  "call_id": 12345,
  "status": "completed",
  "analysis_id": "analysis_12345_company_1",
  "summarization_status": "completed",
  "compliance_status": "completed",
  "objections_status": "completed",
  "qualification_status": "completed",
  "opportunity_analysis_status": "completed",
  "error_message": null,
  "retry_count": 0,
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-01-15T10:05:30Z",
  "completed_at": "2025-01-15T10:05:30Z"
}
```

### GET `/api/v1/analysis/qualification/{call_id}`

Get lead qualification results for a call (includes appointment details, address, rep_details).

**Response:** Same structure as `qualification` object in complete analysis response.

### GET `/api/v1/sms/qualification/{conversation_id}`

Get lead qualification results for an SMS conversation.

**Response:** Same structure as `qualification` object in SMS complete analysis response.

---

## Timezone and Time Parsing

### Best Practices

1. **Always provide `timezone`** - Improves appointment time extraction accuracy
2. **Provide `call_started_at` or `conversation_started_at`** - Enables parsing of relative times like "tomorrow at 4" or "next Friday"
3. **Use IANA timezone format** - Examples: `"America/Phoenix"`, `"America/New_York"`, `"America/Los_Angeles"`
4. **Send datetime in local time with timezone** - Recommended format: `"2025-01-15T10:00:00-07:00"` (Phoenix time)

### Impact on Accuracy

- **With timezone + call_started_at:** Confidence scores 0.8-0.95
- **Without timezone:** Confidence scores 0.3-0.5 (uses UTC, may misinterpret relative times)

---

## Error Handling

### Common Error Codes

- **400 Bad Request** - Invalid request parameters
- **401 Unauthorized** - Invalid or missing JWT token
- **404 Not Found** - Resource not found (call_id, conversation_id, etc.)
- **500 Internal Server Error** - Server error during processing

### Error Response Format

```json
{
  "error": "Error Type",
  "message": "Detailed error message",
  "details": {
    "field": "additional context"
  }
}
```

---

## Rate Limiting

API endpoints are rate-limited per user and per company. Rate limits vary by endpoint:

- Transcription: 10 requests/minute per user, 50/minute per company
- Analysis: 30 requests/minute per user
- SMS Analysis: 10 requests/minute per user, 50/minute per company

Rate limit headers are included in responses:
- `X-RateLimit-Limit` - Maximum requests allowed
- `X-RateLimit-Remaining` - Remaining requests in current window
- `X-RateLimit-Reset` - Time when rate limit resets

---

## Quick Reference

### Call Processing Workflow

1. **Transcribe Call:**
   ```bash
   POST /api/v1/transcription/transcribe
   ```
   - Provides `timezone` and `call_started_at` for best accuracy
   - Returns `transcript_id` and `task_id`

2. **Check Status:**
   ```bash
   GET /api/v1/analysis/status/{call_id}
   ```
   - Poll until `status = "completed"`

3. **Get Complete Analysis:**
   ```bash
   GET /api/v1/analysis/complete/{call_id}
   ```
   - Returns all analysis results including appointment, address, rep_details

### SMS Processing Workflow

1. **Analyze SMS Thread:**
   ```bash
   POST /api/v1/sms/analyze
   ```
   - Send complete thread (all messages)
   - Returns `task_id`

2. **Check Status:**
   ```bash
   GET /api/v1/sms/status/{conversation_id}
   ```
   - Poll until `status = "completed"`

3. **Get Complete Analysis:**
   ```bash
   GET /api/v1/sms/complete/{conversation_id}
   ```
   - Returns all analysis results

---

## Support

For API support or questions, contact: support@otto.shunyalabs.ai

---

## Changelog

### 2025-01-15
- ✅ Added `timezone` and `call_started_at` parameters to transcription API
- ✅ Enhanced qualification response with appointment details, address, and rep_details
- ✅ Added SMS/Text analysis endpoints
- ✅ Updated complete analysis response format

