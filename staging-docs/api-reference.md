# API Reference

## Authentication

All API endpoints require JWT authentication via the `Authorization` header:

```bash
Authorization: Bearer <jwt_token>
```

### Token Generation
```bash
# Generate test token
python scripts/generate-jwt-simple.py --user "test-user" --company "test_company_456" --role "sales_rep" --exp 3600
```

## Authentication Endpoints

### Validate Token
```http
POST /api/v1/auth/validate
Content-Type: application/json

{
  "token": "jwt_token_here"
}
```

**Response:**
```json
{
  "valid": true,
  "user_id": "test-user",
  "company_id": "test_company_456",
  "role": "sales_rep",
  "expires_at": "2024-01-15T11:30:00Z"
}
```

### Get Current User Info
```http
GET /api/v1/auth/me
```

**Response:**
```json
{
  "user_id": "test-user",
  "company_id": "test_company_456",
  "role": "sales_rep",
  "email": "user@example.com"
}
```

### Get Token Info
```http
GET /api/v1/auth/token-info
```

**Response:**
```json
{
  "token_type": "Bearer",
  "expires_at": "2024-01-15T11:30:00Z",
  "issued_at": "2024-01-15T10:30:00Z",
  "user_id": "test-user",
  "company_id": "test_company_456"
}
```

### Get Current Company Info
```http
GET /api/v1/auth/company
```

**Response:**
```json
{
  "company_id": "test_company_456",
  "name": "Test Company",
  "industry": "Technology"
}
```

### Get Available Roles
```http
GET /api/v1/auth/roles
```

**Response:**
```json
{
  "roles": [
    {
      "name": "sales_rep",
      "permissions": ["read", "write"]
    },
    {
      "name": "manager", 
      "permissions": ["read", "write", "manage_users"]
    },
    {
      "name": "admin",
      "permissions": ["read", "write", "delete", "manage_users", "manage_company"]
    }
  ]
}
```

## Document Ingestion APIs

### Document Upload
```http
POST /api/v1/ingestion/documents/upload
Content-Type: multipart/form-data

file: <file>
company_id: "test_company_456"
document_type: "sop"
```

**Response:**
```json
{
  "success": true,
  "document_id": 123,
  "document_name": "example.pdf",
  "status": "processing",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Ingest SOP Documents
```http
POST /api/v1/ingestion/sop-documents
Content-Type: multipart/form-data

file: <file>
company_id: "test_company_456"
```

**Response:**
```json
{
  "success": true,
  "document_id": 124,
  "document_type": "sop",
  "status": "processing"
}
```

### Ingest Training Materials
```http
POST /api/v1/ingestion/training-documents
Content-Type: multipart/form-data

file: <file>
company_id: "test_company_456"
```

**Response:**
```json
{
  "success": true,
  "document_id": 125,
  "document_type": "training",
  "status": "processing"
}
```

### Ingest Reference Documents
```http
POST /api/v1/ingestion/reference-documents
Content-Type: multipart/form-data

file: <file>
company_id: "test_company_456"
```

**Response:**
```json
{
  "success": true,
  "document_id": 126,
  "document_type": "reference",
  "status": "processing"
}
```

### Get Document Status
```http
GET /api/v1/ingestion/{document_id}/status
```

**Response:**
```json
{
  "document_id": 123,
  "status": "completed",
  "processing_stage": "chunking",
  "progress": 100,
  "created_at": "2024-01-15T10:30:00Z",
  "processed_at": "2024-01-15T10:35:00Z"
}
```

## SOP Management APIs

### Get SOP Stages
```http
GET /api/v1/sop/stages
```

**Response:**
```json
{
  "stages": [
    {
      "id": 27,
      "company_id": "test_company_456",
      "stage_name": "Agenda",
      "stage_description": "Take control of the meeting and set expectations. Thank them for the opportunity to serve them. Explain the process for the appointment to them (set the expectation for sitting at the table). Let them know this time is dedicated to them and to stop and ask questions. Share with them that your primary goal is to educate them so that they can make the best decision for their roofing (reduce sales resistance).",
      "stage_order": 2,
      "target_roles": ["sales_rep"],
      "is_role_specific": true,
      "status": "active",
      "approval_status": "pending",
      "approved_by": null,
      "created_at": "2025-10-26T17:36:17.096474Z"
    },
    {
      "id": 28,
      "company_id": "test_company_456",
      "stage_name": "Introduction",
      "stage_description": "Initial greeting and company introduction",
      "stage_order": 1,
      "target_roles": ["sales_rep"],
      "is_role_specific": true,
      "status": "active",
      "approval_status": "approved",
      "approved_by": "admin_user",
      "created_at": "2025-10-26T17:35:00.000000Z"
    }
  ]
}
```

### Create SOP Stage
```http
POST /api/v1/sop/stages
Content-Type: application/json

{
  "stage_name": "Follow-up",
  "stage_description": "Follow-up procedures and next steps",
  "stage_order": 3,
  "target_roles": ["sales_rep"],
  "is_role_specific": true,
  "status": "active"
}
```

**Response:**
```json
{
  "success": true,
  "stage_id": 29,
  "stage_name": "Follow-up",
  "stage_order": 3,
  "target_roles": ["sales_rep"],
  "is_role_specific": true,
  "status": "active",
  "approval_status": "pending",
  "created_at": "2025-10-26T17:37:00.000000Z"
}
```

### Get SOP Stage
```http
GET /api/v1/sop/stages/{stage_id}
```

**Response:**
```json
{
  "id": 27,
  "company_id": "test_company_456",
  "stage_name": "Agenda",
  "stage_description": "Take control of the meeting and set expectations. Thank them for the opportunity to serve them. Explain the process for the appointment to them (set the expectation for sitting at the table). Let them know this time is dedicated to them and to stop and ask questions. Share with them that your primary goal is to educate them so that they can make the best decision for their roofing (reduce sales resistance).",
  "stage_order": 2,
  "target_roles": ["sales_rep"],
  "is_role_specific": true,
  "status": "active",
  "approval_status": "pending",
  "approved_by": null,
  "created_at": "2025-10-26T17:36:17.096474Z"
}
```

### SOP Health Check
```http
GET /api/v1/sop/health
```

**Response:**
```json
{
  "status": "healthy",
  "total_stages": 5,
  "active_stages": 5,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

## Transcription APIs

### Transcribe Audio
```http
POST /api/v1/transcription/transcribe
Content-Type: application/json

{
  "call_id": 2009,
  "audio_url": "https://example.com/audio.mp3",
  "call_type": "sales_call"
}
```

**Response:**
```json
{
  "success": true,
  "call_id": 2009,
  "transcript_id": 123,
  "status": "processing"
}
```

### Get Transcript Status
```http
GET /api/v1/transcription/status/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "status": "completed",
  "transcript": "Hello, this is John from ABC Company...",
  "speaker_segments": [
    {
      "speaker_id": "SPEAKER_01",
      "start_time": 0.0,
      "end_time": 7.0,
      "text": "Thank you for calling Arizona Roofers..."
    }
  ],
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Get Transcript
```http
GET /api/v1/transcription/transcript/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "transcript": "Hello, this is John from ABC Company...",
  "speaker_segments": [
    {
      "speaker_id": "SPEAKER_01",
      "start_time": 0.0,
      "end_time": 7.0,
      "text": "Thank you for calling Arizona Roofers..."
    }
  ],
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Call Analysis APIs

### Start Call Analysis
```http
POST /api/v1/analysis/start/{call_id}
```

**Response:**
```json
{
  "success": true,
  "call_id": 2009,
  "analysis_types": ["objection_detection", "lead_qualification", "compliance_check", "summarization"],
  "status": "processing"
}
```

### Get Analysis Status
```http
GET /api/v1/analysis/status/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "status": "completed",
  "analysis_types": {
    "objection_detection": "completed",
    "lead_qualification": "completed",
    "compliance_check": "completed",
    "summarization": "completed"
  },
  "created_at": "2024-01-15T10:30:00Z",
  "completed_at": "2024-01-15T10:35:00Z"
}
```

### Get Call Summary
```http
GET /api/v1/analysis/summary/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "summary": "Customer called about roof repair services. Expressed interest in getting a quote but had concerns about pricing.",
  "key_points": [
    "Customer needs roof repair",
    "Pricing concerns raised",
    "Follow-up scheduled"
  ],
  "action_items": [
    "Send detailed quote",
    "Schedule site visit"
  ],
  "next_steps": [
    "Follow up in 2 days",
    "Prepare pricing options"
  ],
  "sentiment_score": 0.7,
  "confidence_score": 0.9
}
```

### Get Compliance Check
```http
GET /api/v1/analysis/compliance/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "compliance_score": 0.85,
  "violations": [
    {
      "stage": "Introduction",
      "violation": "Did not mention company name",
      "severity": "low"
    }
  ],
  "recommendations": [
    "Always introduce company name in first 30 seconds",
    "Ask qualifying questions early in conversation"
  ],
  "sop_references": ["intro_script", "qualifying_questions"]
}
```

### Get Objections
```http
GET /api/v1/analysis/objections/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "objections": [
    {
      "id": 1,
      "category_id": 1,
      "category_text": "Pricing",
      "objection_text": "That seems expensive",
      "speaker_id": "SPEAKER_02",
      "timestamp": 45.5,
      "overcome": false
    }
  ]
}
```

### Get Lead Qualification
```http
GET /api/v1/analysis/qualification/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "overall_score": 0.75,
  "bant_scores": {
    "budget": 0.8,
    "authority": 0.7,
    "need": 0.9,
    "timeline": 0.6
  },
  "decision_makers": ["John Smith", "Sarah Johnson"],
  "urgency_signals": ["immediate need", "budget approved"],
  "budget_indicators": ["$50k budget", "Q1 timeline"]
}
```

### Get Complete Analysis
```http
GET /api/v1/analysis/complete/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "transcript": {
    "status": "completed",
    "transcript": "Hello, this is John from ABC Company...",
    "speaker_segments": [...]
  },
  "summary": {
    "summary": "Customer called about roof repair services...",
    "key_points": [...],
    "action_items": [...],
    "sentiment_score": 0.7
  },
  "objections": [
    {
      "category_text": "Pricing",
      "objection_text": "That seems expensive",
      "overcome": false
    }
  ],
  "qualification": {
    "overall_score": 0.75,
    "bant_scores": {...}
  },
  "compliance": {
    "compliance_score": 0.85,
    "violations": [...],
    "recommendations": [...]
  }
}
```

## Call Summarization APIs

### Summarize Call
```http
POST /api/v1/summarization/summarize
Content-Type: application/json

{
  "call_id": 2009,
  "transcript_id": 123
}
```

**Response:**
```json
{
  "success": true,
  "call_id": 2009,
  "summary": "Customer called about roof repair services. Expressed interest in getting a quote but had concerns about pricing. Rep provided detailed information about services and scheduled follow-up call.",
  "key_points": [
    "Customer needs roof repair",
    "Pricing concerns raised",
    "Follow-up scheduled"
  ],
  "action_items": [
    "Send detailed quote",
    "Schedule site visit"
  ],
  "next_steps": [
    "Follow up in 2 days",
    "Prepare pricing options"
  ],
  "sentiment_score": 0.7,
  "confidence_score": 0.9,
  "created_at": "2024-01-15T10:50:00Z"
}
```

### Get Summarization Status
```http
GET /api/v1/summarization/status/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "status": "completed",
  "summary": "Customer called about roof repair services...",
  "key_points": [...],
  "action_items": [...],
  "sentiment_score": 0.7,
  "created_at": "2024-01-15T10:50:00Z"
}
```

## Objection Detection APIs

### Detect Objections
```http
POST /api/v1/objection-detection/detect
Content-Type: application/json

{
  "call_id": 2009,
  "transcript_id": 123
}
```

**Response:**
```json
{
  "success": true,
  "call_id": 2009,
  "objections": [
    {
      "id": 1,
      "category_id": 1,
      "category_text": "Pricing",
      "objection_text": "That seems expensive",
      "speaker_id": "SPEAKER_02",
      "timestamp": 45.5,
      "overcome": false
    }
  ],
  "created_at": "2024-01-15T10:35:00Z"
}
```

### Get Objection Detection Status
```http
GET /api/v1/objection-detection/objections/status/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "status": "completed",
  "objections_found": 2,
  "categories_detected": ["Pricing", "Timing"],
  "created_at": "2024-01-15T10:35:00Z"
}
```

## Lead Qualification APIs

### Qualify Lead
```http
POST /api/v1/lead-qualification/qualify
Content-Type: application/json

{
  "call_id": 2009,
  "transcript_id": 123,
  "target_role": "sales_rep"
}
```

**Response:**
```json
{
  "success": true,
  "call_id": 2009,
  "qualification": {
    "overall_score": 0.75,
    "bant_scores": {
      "budget": 0.8,
      "authority": 0.7,
      "need": 0.9,
      "timeline": 0.6
    },
    "decision_makers": ["John Smith", "Sarah Johnson"],
    "urgency_signals": ["immediate need", "budget approved"],
    "budget_indicators": ["$50k budget", "Q1 timeline"]
  },
  "created_at": "2024-01-15T10:40:00Z"
}
```

### Get Qualification Status
```http
GET /api/v1/lead-qualification/status/{call_id}
```

**Response:**
```json
{
  "call_id": 2009,
  "status": "completed",
  "overall_score": 0.75,
  "bant_scores": {
    "budget": 0.8,
    "authority": 0.7,
    "need": 0.9,
    "timeline": 0.6
  },
  "created_at": "2024-01-15T10:40:00Z"
}
```

## Search and Chunk Management APIs

### Search Documents
```http
GET /api/v1/search/query?q=roofing+procedures&company_id=test_company_456
```

**Response:**
```json
{
  "query": "roofing procedures",
  "results": [
    {
      "document_id": 1,
      "chunk_id": 5,
      "content": "Standard roofing procedures include...",
      "score": 0.95,
      "metadata": {
        "document_name": "Roofing SOP",
        "page_number": 3
      }
    }
  ],
  "total_results": 1
}
```

### Chunk Feedback
```http
POST /api/v1/chunks/feedback
Content-Type: application/json

{
  "chunk_id": 5,
  "feedback_score": 4,
  "feedback_text": "Very helpful information"
}
```

**Response:**
```json
{
  "success": true,
  "chunk_id": 5,
  "feedback_score": 4,
  "feedback_text": "Very helpful information",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

## Error Responses

### Standard Error Format
```json
{
  "detail": "Error message describing what went wrong",
  "error_code": "VALIDATION_ERROR",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Common HTTP Status Codes
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

