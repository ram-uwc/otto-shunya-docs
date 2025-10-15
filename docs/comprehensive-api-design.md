# Otto AI Comprehensive API Design

## Overview

This document provides a comprehensive design for the Otto AI platform API, including detailed input/output parameters for all 45+ endpoints across 13 functional categories. The API supports AI-powered sales intelligence with voice processing, RAG capabilities, personal AI clones, and comprehensive analytics.

## Authentication & Headers

All API requests require the following headers:

- `Authorization: Bearer <jwt_token>` - JWT token containing user info (user_id, role, permissions)
- `X-Company-ID: <company_uuid>` - Required for multi-tenant isolation
- `X-Request-ID: <request_uuid>` - Required for tracing and debugging

## API Categories

1. **System APIs** (1 endpoint)
2. **Call Data Ingestion APIs** (7 endpoints)
3. **Document Data Ingestion APIs** (5 endpoints)
4. **CRM Data Ingestion APIs** (2 endpoints)
5. **Enhanced Summarization APIs** (5 endpoints)
6. **Vector Maintenance APIs** (2 endpoints)
7. **Voice Intelligence APIs** (8 endpoints)
8. **RAG/Ask Otto APIs** (2 endpoints)
9. **Personal AI APIs** (5 endpoints)
10. **Follow-up APIs** (6 endpoints)
11. **SOP Management APIs** (6 endpoints)
12. **Performance & Analytics APIs** (4 endpoints)
13. **Webhooks** (3 endpoints)

---

## 1. System APIs

### 1.1 Health Check

**Endpoint:** `GET /health`

**Description:** Check API health status

**Input Parameters:** None

**Output:**
```json
{
  "status": "healthy",
  "service": "otto-api",
  "version": "1.0.0",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

---

## 2. Call Data Ingestion APIs

### 2.1 Create Call Record

**Endpoint:** `POST /api/v1/calls`

**Description:** Create a new call record for processing

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "call_id": "call_12345",
  "audio_url": "https://s3.amazonaws.com/bucket/audio.wav",
  "caller_phone": "+1234567890",
  "rep_phone": "+0987654321",
  "duration": 300,
  "callrail_id": "cr_12345",
  "metadata": {
    "source": "callrail",
    "campaign": "summer_sale"
  }
}
```

**Output:**
```json
{
  "call_id": "call_12345",
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "audio_file_path": "s3://bucket/audio/call_12345.wav",
  "transcript_file_path": null,
  "speaker_diarization_file_path": null,
  "processing_status": "pending",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

### 2.2 Get Call Details

**Endpoint:** `GET /api/v1/calls/{call_id}`

**Description:** Retrieve call details by ID

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "completed",
  "audio_file_path": "s3://bucket/audio/call_12345.wav",
  "transcript_file_path": "s3://bucket/transcripts/call_12345.txt",
  "speaker_diarization_file_path": "s3://bucket/diarization/call_12345.json",
  "processing_status": "completed",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:35:00Z"
}
```

### 2.3 Update Call Metadata

**Endpoint:** `PUT /api/v1/calls/{call_id}`

**Description:** Update call metadata and status

**Input Parameters:**
- `call_id` (path): Call identifier
- Body:
```json
{
  "status": "processing",
  "metadata": {
    "notes": "High priority lead",
    "tags": ["qualified", "follow_up_needed"]
  }
}
```

**Output:**
```json
{
  "call_id": "call_12345",
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "processing",
  "audio_file_path": "s3://bucket/audio/call_12345.wav",
  "transcript_file_path": null,
  "speaker_diarization_file_path": null,
  "processing_status": "processing",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:32:00Z"
}
```

### 2.4 Get Call Processing Status

**Endpoint:** `GET /api/v1/calls/{call_id}/status`

**Description:** Get detailed processing status for a call

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "status": "processing",
  "progress": 75,
  "stages": {
    "transcription": "completed",
    "diarization": "processing",
    "analysis": "pending"
  },
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:32:00Z"
}
```

### 2.5 Get Audio Playback URL

**Endpoint:** `GET /api/v1/calls/{call_id}/audio`

**Description:** Get signed URL for audio playback

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "audio_url": "https://s3.amazonaws.com/bucket/audio/call_12345.wav?X-Amz-Signature=...",
  "expires_at": "2025-01-15T11:30:00Z"
}
```

### 2.6 Get Transcript

**Endpoint:** `GET /api/v1/calls/{call_id}/transcript`

**Description:** Get transcript content from S3

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "transcript": "Hello, this is John from ABC Company. I'm calling about your recent inquiry...",
  "confidence": 0.95,
  "language": "en-US"
}
```

### 2.7 Get Speaker Diarization

**Endpoint:** `GET /api/v1/calls/{call_id}/diarization`

**Description:** Get speaker diarization results

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "speakers": [
    {
      "speaker_id": "speaker_1",
      "start_time": 0.0,
      "end_time": 15.5,
      "text": "Hello, this is John from ABC Company.",
      "confidence": 0.92
    },
    {
      "speaker_id": "speaker_2",
      "start_time": 15.5,
      "end_time": 30.2,
      "text": "Hi John, thanks for calling. I'm interested in your services.",
      "confidence": 0.88
    }
  ]
}
```

---

## 3. Document Data Ingestion APIs

### 3.1 Ingest SOP Documents

**Endpoint:** `POST /api/v1/ingestion/sop-documents`

**Description:** Ingest Standard Operating Procedure documents for role-based training

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "role": "sales_rep",
  "document_type": "sop",
  "file": "multipart/form-data",
  "metadata": {
    "version": "v2.1",
    "effective_date": "2025-01-15",
    "department": "sales"
  }
}
```

**Output:**
```json
{
  "ingestion_id": "ingest_12345",
  "status": "processing",
  "document_id": "doc_12345",
  "chunks_created": 0,
  "estimated_processing_time": "2-5 minutes"
}
```

### 3.2 Document Upload (UWC)

**Endpoint:** `POST /api/v1/ingestion/documents/upload`

**Description:** Upload documents for processing (UWC - Underwater Computing)

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "document_name": "policy.pdf",
  "document_type": "pdf",
  "url": "https://s3.amazonaws.com/bucket/policy.pdf",
  "namespace": "company_xyz",
  "metadata": {
    "category": "policies",
    "access_level": "internal"
  }
}
```

**Output:**
```json
{
  "upload_id": "upload_12345",
  "status": "uploaded",
  "processing_job_id": "job_12345",
  "estimated_completion": "2025-01-15T10:35:00Z"
}
```

### 3.3 Document Processing Complete (UWC)

**Endpoint:** `POST /api/v1/ingestion/documents/complete`

**Description:** Mark document processing as complete (UWC callback)

**Input Parameters:**
```json
{
  "upload_id": "upload_12345",
  "processing_job_id": "job_12345",
  "status": "completed",
  "chunks_created": 25,
  "vector_embeddings": 25,
  "metadata_extracted": {
    "title": "Company Policy Document",
    "pages": 15,
    "language": "en"
  }
}
```

**Output:**
```json
{
  "status": "acknowledged",
  "document_id": "doc_12345",
  "indexing_status": "completed"
}
```

### 3.4 Ingest Training Materials

**Endpoint:** `POST /api/v1/ingestion/training-documents`

**Description:** Ingest training materials and knowledge base documents

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "document_type": "training",
  "file": "multipart/form-data",
  "metadata": {
    "category": "product_knowledge",
    "audience": "sales_team",
    "difficulty_level": "intermediate"
  }
}
```

**Output:**
```json
{
  "ingestion_id": "ingest_12346",
  "status": "processing",
  "document_id": "doc_12346",
  "chunks_created": 0,
  "processing_notes": "Document will be indexed for RAG queries"
}
```

### 3.5 Ingest Reference Documents

**Endpoint:** `POST /api/v1/ingestion/reference-documents`

**Description:** Ingest reference materials and company-specific documentation

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "document_type": "reference",
  "file": "multipart/form-data",
  "metadata": {
    "category": "company_policies",
    "access_level": "internal",
    "last_updated": "2025-01-10"
  }
}
```

**Output:**
```json
{
  "ingestion_id": "ingest_12347",
  "status": "processing",
  "document_id": "doc_12347",
  "chunks_created": 0,
  "indexing_status": "in_progress"
}
```

---

## 4. CRM Data Ingestion APIs

### 4.1 Ingest Entities (UWC)

**Endpoint:** `POST /api/v1/ingestion/entities`

**Description:** Ingest entity data for event sourcing (UWC)

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "entities": [
    {
      "entity_id": "entity_12345",
      "entity_type": "customer",
      "attributes": {
        "name": "John Smith",
        "email": "john@abc.com",
        "phone": "+1234567890",
        "company": "ABC Corp",
        "lead_score": 85
      },
      "timestamp": "2025-01-15T10:30:00Z"
    }
  ]
}
```

**Output:**
```json
{
  "ingestion_id": "ingest_12350",
  "status": "completed",
  "entities_processed": 1,
  "entities_created": 1,
  "entities_updated": 0
}
```

### 4.2 Ingest Events (UWC)

**Endpoint:** `POST /api/v1/ingestion/events`

**Description:** Ingest entity events for event sourcing (UWC)

**Input Parameters:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "events": [
    {
      "event_id": "event_12345",
      "entity_id": "entity_12345",
      "event_type": "call",
      "timestamp": "2025-01-15T10:30:00Z",
      "data": {
        "call_id": "call_12345",
        "duration": 300,
        "outcome": "qualified"
      }
    }
  ]
}
```

**Output:**
```json
{
  "ingestion_id": "ingest_12351",
  "status": "completed",
  "events_processed": 1,
  "events_created": 1
}
```

---

---

## 5. Enhanced Summarization APIs

### 5.1 Generate Daily Summary

**Endpoint:** `POST /api/v1/summary/daily`

**Description:** Generate daily performance recap

**Input Parameters:**
```json
{
  "date": "2025-01-15",
  "rep_id": "rep_12345",
  "summary_type": "detailed"
}
```

**Output:**
```json
{
  "date": "2025-01-15",
  "rep_id": "rep_12345",
  "content": "Today's Performance Summary:\n\n• 5 calls completed\n• 3 qualified leads identified...",
  "metrics": {
    "calls_completed": 5,
    "qualified_leads": 3,
    "appointments_scheduled": 2
  },
  "created_at": "2025-01-15T18:00:00Z"
}
```

### 5.2 Generate Appointment Summary

**Endpoint:** `POST /api/v1/summary/appointment`

**Description:** Generate appointment-specific summary

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "summary_type": "detailed"
}
```

**Output:**
```json
{
  "call_id": "call_12345",
  "rep_id": "rep_12345",
  "content": "Appointment Summary:\n\nCustomer: John Smith (ABC Corp)\nDuration: 45 minutes\nOutcome: Qualified lead - interested in premium package\n\nKey Discussion Points:\n• Current challenges with existing solution\n• Budget range: $50K-$75K annually\n• Decision timeline: Q2 2025\n• Key stakeholders: CTO, CFO\n\nNext Steps:\n• Send detailed proposal by Friday\n• Schedule technical demo for next week\n• Follow up on budget approval process",
  "key_points": [
    "Qualified lead with budget confirmed",
    "Technical demo scheduled"
  ],
  "next_steps": [
    "Send detailed proposal",
    "Schedule technical demo"
  ],
  "created_at": "2025-01-15T10:30:00Z"
}
```

### 5.3 Generate Prep Summary

**Endpoint:** `POST /api/v1/summary/prep`

**Description:** Generate pre-call summary with context and insights

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "rep_id": "rep_12345",
  "customer_context": {
    "name": "John Smith",
    "company": "ABC Corp",
    "previous_interactions": 2,
    "last_objection": "price_concern"
  }
}
```

**Output:**
```json
{
  "call_id": "call_12345",
  "rep_id": "rep_12345",
  "content": "Pre-Call Brief for John Smith (ABC Corp):\n\nPrevious Interactions:\n• Last call: Price objection raised\n• Customer interested in premium package\n\nRecommendations:\n• Focus on ROI and value proposition\n• Address price concerns proactively\n• Prepare flexible payment options",
  "key_insights": [
    "Price-sensitive customer",
    "Interested in premium features",
    "Decision maker identified"
  ],
  "suggested_approach": "Value-focused presentation with flexible payment options"
}
```

### 5.4 Get Summary History

**Endpoint:** `GET /api/v1/summary/{rep_id}/history`

**Description:** Retrieve summary history by representative

**Input Parameters:**
- `rep_id` (path): Representative identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `type` (query): Filter by summary type (daily, appointment, prep)
- `sort` (query): Sort order (created_at, date) (default: created_at)
- `order` (query): Sort direction (asc, desc) (default: desc)

**Output:**
```json
{
  "rep_id": "rep_12345",
  "summaries": [
    {
      "type": "daily",
      "date": "2025-01-15",
      "content": "Today's Performance Summary...",
      "created_at": "2025-01-15T18:00:00Z"
    },
    {
      "type": "appointment",
      "call_id": "call_12345",
      "date": "2025-01-15",
      "content": "Appointment Summary for John Smith...",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ],
  "total": 150,
  "limit": 20,
  "offset": 0
}
```

### 5.5 Get Summary by Call ID

**Endpoint:** `GET /api/v1/summary/call/{call_id}`

**Description:** Retrieve summary for a specific call

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "rep_id": "rep_12345",
  "summary_type": "appointment",
  "content": "Appointment Summary:\n\nCustomer: John Smith (ABC Corp)...",
  "key_points": [
    "Qualified lead with budget confirmed",
    "Technical demo scheduled"
  ],
  "next_steps": [
    "Send detailed proposal",
    "Schedule technical demo"
  ],
  "created_at": "2025-01-15T10:30:00Z"
}
```

---


---

## 6. Vector Maintenance APIs (UWC)

### 6.1 Delete Vector

**Endpoint:** `DELETE /api/v1/maintenance/vectors/{entity_id}`

**Description:** Delete vector embeddings for an entity (UWC)

**Input Parameters:**
- `entity_id` (path): Entity identifier

**Output:**
```json
{
  "entity_id": "entity_12345",
  "vectors_deleted": 15,
  "status": "completed",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

### 6.2 Reindex Vectors

**Endpoint:** `POST /api/v1/maintenance/vectors/reindex`

**Description:** Reindex all vectors for a namespace (UWC)

**Input Parameters:**
```json
{
  "namespace": "company_xyz",
  "force_reindex": false,
  "batch_size": 100
}
```

**Output:**
```json
{
  "reindex_id": "reindex_12345",
  "status": "started",
  "total_entities": 1000,
  "estimated_completion": "2025-01-15T11:00:00Z",
  "progress": 0
}
```

---


---

## 7. Voice Intelligence APIs

### 7.1 Batch Audio Transcription

**Endpoint:** `POST /api/v1/asr/transcribe`

**Description:** Transcribe audio using ASR services

**Input Parameters:**
```json
{
  "audio_url": "https://s3.amazonaws.com/bucket/audio.wav",
  "language": "en-US",
  "model": "nova-2"
}
```

**Output:**
```json
{
  "transcript": "Hello, this is John from ABC Company. I'm calling about your recent inquiry...",
  "confidence": 0.95,
  "language": "en-US",
  "duration": 300.5
}
```

### 7.2 Get Speaker Segments

**Endpoint:** `GET /api/v1/calls/{call_id}/speakers`

**Description:** Get speaker diarization segments

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "speakers": [
    {
      "speaker_id": "speaker_1",
      "start_time": 0.0,
      "end_time": 15.5,
      "text": "Hello, this is John from ABC Company.",
      "confidence": 0.92
    }
  ]
}
```

### 7.3 Get Lead Classification

**Endpoint:** `GET /api/v1/calls/{call_id}/lead-classification`

**Description:** Get AI-powered lead classification results

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "lead_score": 0.85,
  "lead_status": "hot",
  "qualification_reasons": [
    "Expressed immediate need",
    "Budget confirmed",
    "Decision maker identified"
  ],
  "confidence_score": 0.92
}
```

### 7.4 Get Objection Analysis

**Endpoint:** `GET /api/v1/calls/{call_id}/objections`

**Description:** Get detected objections and response suggestions

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "objections": [
    {
      "objection_type": "price",
      "objection_text": "Your price is too high compared to competitors",
      "response_suggestions": [
        "Focus on value proposition",
        "Offer payment plans",
        "Compare ROI with competitors"
      ],
      "severity": "high",
      "confidence": 0.88
    }
  ]
}
```

### 7.5 Get SOP Analysis

**Endpoint:** `GET /api/v1/calls/{call_id}/sop-analysis`

**Description:** Get SOP compliance analysis

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "stages_detected": [
    {
      "stage_name": "Introduction",
      "stage_order": 1,
      "detected_at": "2025-01-15T10:30:15Z",
      "confidence_score": 0.95
    },
    {
      "stage_name": "Needs Assessment",
      "stage_order": 2,
      "detected_at": "2025-01-15T10:30:45Z",
      "confidence_score": 0.88
    }
  ],
  "gaps": [
    "Missing qualification questions",
    "No objection handling"
  ],
  "compliance_score": 0.75
}
```

### 7.6 Get Coaching Feedback

**Endpoint:** `GET /api/v1/calls/{call_id}/coaching`

**Description:** Get real-time coaching feedback

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "feedback": [
    {
      "feedback_type": "rapport_building",
      "feedback_text": "Good job building rapport in the first 2 minutes",
      "improvement_suggestions": [
        "Ask more open-ended questions",
        "Listen actively to responses"
      ],
      "priority": "medium"
    }
  ]
}
```

### 7.7 Get Meeting Segmentation

**Endpoint:** `GET /api/v1/calls/{call_id}/meeting-segments`

**Description:** Get meeting phase segmentation

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "segments": [
    {
      "segment_type": "rapport",
      "start_time": 0.0,
      "end_time": 120.0,
      "duration": 120.0,
      "key_points": [
        "Established personal connection",
        "Discussed weather and local events"
      ]
    },
    {
      "segment_type": "agenda",
      "start_time": 120.0,
      "end_time": 180.0,
      "duration": 60.0,
      "key_points": [
        "Outlined meeting objectives",
        "Set expectations for the call"
      ]
    }
  ]
}
```

### 7.8 Get Rehash Score

**Endpoint:** `GET /api/v1/calls/{call_id}/rehash-score`

**Description:** Get rehash scoring for follow-up prioritization

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "call_id": "call_12345",
  "rehash_score": 4,
  "confidence": 0.85,
  "reasons": [
    "High engagement level",
    "Specific next steps discussed",
    "Budget and timeline confirmed"
  ]
}
```

---

## 8. RAG/Ask Otto APIs

### 8.1 Natural Language Query (WebSocket)

**Endpoint:** `WS /api/v1/rag/query`

**Description:** Real-time interactive chat with Ask Otto using WebSocket connection

**WebSocket Connection:**
```javascript
// Client-side WebSocket connection
const ws = new WebSocket('wss://api.otto.ai/api/v1/rag/query', {
  headers: {
    'Authorization': 'Bearer <jwt_token>',
    'X-Company-ID': '<company_uuid>',
    'X-Request-ID': '<request_uuid>'
  }
});

// Send query message
ws.send(JSON.stringify({
  "type": "query",
  "message": "What were the top objections from last week's calls?",
  "rep_id": "rep_12345",
  "call_type": "sales"
  },
  "session_id": "session_12345"
}));
```

**WebSocket Message Types:**

**Client → Server Messages:**
```json
// Initial connection
{
  "type": "connect",
  "session_id": "session_12345",
  "user_context": {
    "user_id": "user_12345",
    "role": "manager",
    "permissions": ["view_analytics", "ask_otto"]
  }
}

// Send query
{
  "type": "query",
  "message": "What were the top objections from last week's calls?",
  "context": {
    "date_range": {
      "start": "2025-01-08",
      "end": "2025-01-15"
    }
  },
  "session_id": "session_12345"
}

// Follow-up question
{
  "type": "follow_up",
  "message": "Which CSR handles price objections best?",
  "previous_query_id": "query_67890",
  "session_id": "session_12345"
}

// End session
{
  "type": "disconnect",
  "session_id": "session_12345"
}
```

**Server → Client Messages:**
```json
// Connection established
{
  "type": "connected",
  "session_id": "session_12345",
  "status": "ready",
  "timestamp": "2025-01-15T10:30:00Z"
}

// Query processing started
{
  "type": "processing",
  "query_id": "query_67890",
  "status": "searching",
  "timestamp": "2025-01-15T10:30:01Z"
}

// Streaming response chunks
{
  "type": "response_chunk",
  "query_id": "query_67890",
  "chunk": "Based on last week's calls, the top objections were:",
  "chunk_index": 0,
  "total_chunks": 3,
  "timestamp": "2025-01-15T10:30:02Z"
}

{
  "type": "response_chunk",
  "query_id": "query_67890",
  "chunk": "1) Price concerns (45% of calls), 2) Timing issues (30% of calls), 3) Authority questions (25% of calls).",
  "chunk_index": 1,
  "total_chunks": 3,
  "timestamp": "2025-01-15T10:30:03Z"
}

// Final response with citations
{
  "type": "response_complete",
  "query_id": "query_67890",
  "answer": "Based on last week's calls, the top objections were: 1) Price concerns (45% of calls), 2) Timing issues (30% of calls), 3) Authority questions (25% of calls). The most effective responses were focusing on ROI and offering flexible payment terms.",
  "citations": [
    {
      "source": "call_transcript_12345",
      "page": 1,
      "confidence": 0.92,
      "excerpt": "Customer mentioned price was too high compared to competitors..."
    }
  ],
  "confidence": 0.88,
  "suggested_follow_ups": [
    "Which CSR handles price objections best?",
    "What's the average deal size for price objections?",
    "Show me the objection handling training materials"
  ],
  "timestamp": "2025-01-15T10:30:05Z"
}

// Error handling
{
  "type": "error",
  "query_id": "query_67890",
  "error": "insufficient_data",
  "message": "Not enough call data for the specified date range",
  "suggestion": "Try expanding the date range or checking a different time period",
  "timestamp": "2025-01-15T10:30:02Z"
}

// Session timeout
{
  "type": "timeout",
  "session_id": "session_12345",
  "message": "Session will expire in 5 minutes due to inactivity",
  "timestamp": "2025-01-15T10:35:00Z"
}
```

**WebSocket Features:**
- **Real-time streaming**: Responses are streamed as they're generated
- **Session management**: Maintains conversation context across multiple queries
- **Follow-up questions**: Natural conversation flow with context retention
- **Suggested follow-ups**: AI suggests related questions
- **Error handling**: Graceful error messages with suggestions
- **Session timeout**: Automatic cleanup of inactive sessions
- **Connection management**: Automatic reconnection and heartbeat

### 8.2 Get Query History

**Endpoint:** `GET /api/v1/rag/queries`

**Description:** Retrieve query history with pagination

**Input Parameters:**
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (created_at, query_text) (default: created_at)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `search` (query): Search in query text (optional)

**Output:**
```json
{
  "queries": [
    {
      "query_id": "query_67890",
      "query_text": "What were the top objections from last week's calls?",
      "response_text": "Based on last week's calls, the top objections were...",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ],
  "total": 150,
  "limit": 20,
  "offset": 0
}
```
---

## 9. Personal AI APIs

### 9.1 Get Clone Profile

**Endpoint:** `GET /api/v1/clone/{rep_id}/profile`

**Description:** Retrieve clone profile and characteristics

**Input Parameters:**
- `rep_id` (path): Representative identifier

**Output:**
```json
{
  "rep_id": "rep_12345",
  "profile": {
    "clone_id": "clone_12345",
    "is_trained": true,
    "training_status": "completed",
    "model_version": "v1.2.3",
    "characteristics": {
      "tone": "professional_friendly",
      "writing_style": "concise_direct",
      "communication_preferences": ["email", "sms"]
    },
    "performance_metrics": {
      "drafts_generated": 150,
      "approval_rate": 0.85,
      "user_satisfaction": 0.92
    },
    "last_trained": "2025-01-15T09:00:00Z"
  }
}
```

### 9.2 Generate Content with Personal Clone

**Endpoint:** `POST /api/v1/clone/{rep_id}/generate`

**Description:** Generate content using personal AI clone

**Input Parameters:**
- `rep_id` (path): Sales rep identifier
- Body:
```json
{
  "content_type": "email",
  "prompt": "Write a follow-up email for a qualified lead who showed interest in our premium package",
  "context": {
    "customer_name": "John Smith",
    "company": "ABC Corp",
    "previous_interaction": "Initial discovery call"
  }
}
```

**Output:**
```json
{
  "content": "Hi John,\n\nThank you for taking the time to speak with me yesterday about your company's needs. I was impressed by your insights into the challenges ABC Corp is facing...",
  "confidence": 0.92,
  "draft_id": "draft_12345"
}
```

### 9.3 Get Generated Drafts

**Endpoint:** `GET /api/v1/clone/{rep_id}/drafts`

**Description:** Retrieve generated content drafts

**Input Parameters:**
- `rep_id` (path): Sales rep identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (created_at, content_type) (default: created_at)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `content_type` (query): Filter by content type (email, sms, call_script) (optional)
- `status` (query): Filter by status (ready, draft, sent) (optional)

**Output:**
```json
{
  "drafts": [
    {
      "draft_id": "draft_12345",
      "content_type": "email",
      "content": "Hi John,\n\nThank you for taking the time...",
      "created_at": "2025-01-15T10:30:00Z",
      "status": "ready"
    }
  ]
}
```

### 9.4 Train Personal Clone

**Endpoint:** `POST /api/v1/clone/{rep_id}/train`

**Description:** Train personal AI clone with communication samples

**Input Parameters:**
- `rep_id` (path): Sales rep identifier
- Body:
```json
{
  "communication_samples": [
    {
      "content": "Hi there! Thanks for your interest in our services...",
      "type": "email"
    },
    {
      "content": "Hello, this is Sarah from ABC Company...",
      "type": "call_transcript"
    }
  ]
}
```

**Output:**
```json
{
  "training_id": "training_12345",
  "status": "started"
}
```

### 9.5 Get Clone Training Status

**Endpoint:** `GET /api/v1/clone/{rep_id}/status`

**Description:** Check personal clone training status

**Input Parameters:**
- `rep_id` (path): Sales rep identifier

**Output:**
```json
{
  "rep_id": "rep_12345",
  "is_trained": true,
  "training_status": "completed",
  "last_trained": "2025-01-15T09:00:00Z",
  "model_version": "v1.2.3"
}
```


---

## 10. Follow-up APIs

### 10.1 Generate Follow-up Draft

**Endpoint:** `POST /api/v1/ai/followup/draft`

**Description:** Generate AI-powered follow-up content

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "followup_type": "nurture",
  "tone": "professional",
  "channel": "email"
}
```

**Output:**
```json
{
  "draft_id": "draft_12345",
  "content": "Subject: Thank you for your time today\n\nHi John,\n\nThank you for taking the time to speak with me about ABC Corp's needs. I enjoyed our conversation about your current challenges and how our solution could help...",
  "channel": "email",
  "suggested_send_time": "2025-01-15T14:00:00Z"
}
```

### 10.2 Generate Nurture Follow-up

**Endpoint:** `POST /api/v1/ai/followup/nurture`

**Description:** Generate nurture follow-up for CSR

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "customer_info": {
    "name": "John Smith",
    "company": "ABC Corp",
    "industry": "Technology"
  }
}
```

**Output:**
```json
{
  "draft_id": "draft_12345",
  "content": "Hi John,\n\nI wanted to follow up on our conversation about your company's growth plans. Based on what you shared, I think our solution could really help ABC Corp scale efficiently...",
  "strategy": "Value-focused nurturing with industry insights"
}
```

### 10.3 Generate Rehash Follow-up

**Endpoint:** `POST /api/v1/ai/followup/rehash`

**Description:** Generate rehash follow-up for sales rep

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "rehash_score": 4
}
```

**Output:**
```json
{
  "draft_id": "draft_12345",
  "content": "Hi John,\n\nI've been thinking about our conversation and wanted to share some additional insights that might be relevant to your situation...",
  "approach": "High-value re-engagement with new angle"
}
```

### 10.4 Get Follow-up Tasks

**Endpoint:** `GET /api/v1/calls/{call_id}/follow-up-tasks`

**Description:** Retrieve follow-up tasks for a call

**Input Parameters:**
- `call_id` (path): Call identifier

**Output:**
```json
{
  "tasks": [
    {
      "task_id": "task_12345",
      "task_type": "email",
      "description": "Send detailed proposal to John Smith",
      "priority": "high",
      "status": "pending",
      "due_date": "2025-01-16T17:00:00Z",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

### 10.5 Create Follow-up Task

**Endpoint:** `POST /api/v1/calls/{call_id}/follow-up-tasks`

**Description:** Create new follow-up task

**Input Parameters:**
- `call_id` (path): Call identifier
- Body:
```json
{
  "task_type": "call",
  "description": "Follow up on technical questions",
  "priority": "medium",
  "due_date": "2025-01-16T14:00:00Z"
}
```

**Output:**
```json
{
  "task_id": "task_12345",
  "task_type": "call",
  "description": "Follow up on technical questions",
  "priority": "medium",
  "status": "pending",
  "due_date": "2025-01-16T14:00:00Z",
  "created_at": "2025-01-15T10:30:00Z"
}
```

### 10.6 Get All Follow-up Drafts

**Endpoint:** `GET /api/v1/followup/{rep_id}/drafts`

**Description:** Get all follow-up drafts for a rep

**Input Parameters:**
- `rep_id` (path): Sales rep identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (created_at, call_id, content_type) (default: created_at)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `content_type` (query): Filter by content type (email, sms, call_script) (optional)
- `status` (query): Filter by status (ready, draft, sent) (optional)
- `call_id` (query): Filter by specific call (optional)

**Output:**
```json
{
  "drafts": [
    {
      "draft_id": "draft_12345",
      "call_id": "call_12345",
      "content_type": "email",
      "content": "Hi John,\n\nThank you for your time...",
      "status": "ready",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

---

## 11. SOP Management APIs

### 11.1 Configure Company SOP Stages

**Endpoint:** `POST /api/v1/sop/stages`

**Description:** Configure SOP stages for a company

**Input Parameters:**
```json
{
  "stages": [
    {
      "stage_name": "Introduction",
      "stage_order": 1,
      "stage_description": "Introduce yourself and company",
      "is_active": true
    },
    {
      "stage_name": "Needs Assessment",
      "stage_order": 2,
      "stage_description": "Understand customer needs and pain points",
      "is_active": true
    }
  ]
}
```

**Output:**
```json
{
  "sop_id": "sop_12345",
  "stages": [
    {
      "stage_id": "stage_1",
      "stage_name": "Introduction",
      "stage_order": 1,
      "stage_description": "Introduce yourself and company",
      "is_active": true,
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

### 11.2 Get Company SOP Stages

**Endpoint:** `GET /api/v1/sop/stages`

**Description:** Retrieve company SOP stages

**Input Parameters:**
- `company_id` (query): Company identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (stage_order, created_at, stage_name) (default: stage_order)
- `order` (query): Sort direction (asc, desc) (default: asc)
- `is_active` (query): Filter by active status (true, false) (optional)

**Output:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "stages": [
    {
      "stage_id": "stage_1",
      "stage_name": "Introduction",
      "stage_order": 1,
      "stage_description": "Introduce yourself and company",
      "is_active": true,
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

### 11.3 Update SOP Stage

**Endpoint:** `PUT /api/v1/sop/stages/{stage_id}`

**Description:** Update specific SOP stage

**Input Parameters:**
- `stage_id` (path): Stage identifier
- Body:
```json
{
  "stage_name": "Introduction",
  "stage_order": 1,
  "stage_description": "Introduce yourself, company, and purpose of call",
  "is_active": true
}
```

**Output:**
```json
{
  "stage_id": "stage_1",
  "stage_name": "Introduction",
  "stage_order": 1,
  "stage_description": "Introduce yourself, company, and purpose of call",
  "is_active": true,
  "updated_at": "2025-01-15T10:35:00Z"
}
```

### 11.4 Delete SOP Stage

**Endpoint:** `DELETE /api/v1/sop/stages/{stage_id}`

**Description:** Delete SOP stage

**Input Parameters:**
- `stage_id` (path): Stage identifier

**Output:** 204 No Content

### 11.5 Get Compliance Analytics

**Endpoint:** `GET /api/v1/sop/compliance/{company_id}`

**Description:** Get SOP compliance analytics

**Input Parameters:**
- `company_id` (path): Company identifier
- `date_range` (query): Optional date range filter

**Output:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "overall_compliance": 0.78,
  "stage_compliance": {
    "Introduction": 0.85,
    "Needs Assessment": 0.72,
    "Proposal": 0.65
  },
  "rep_performance": [
    {
      "rep_id": "rep_12345",
      "compliance_score": 0.82,
      "improvement_areas": [
        "Needs Assessment questions",
        "Objection handling"
      ]
    }
  ]
}
```

### 11.6 Analyze Call Compliance

**Endpoint:** `POST /api/v1/sop/compliance/analyze`

**Description:** Analyze specific call for SOP compliance

**Input Parameters:**
```json
{
  "call_id": "call_12345",
  "sop_id": "sop_12345"
}
```

**Output:**
```json
{
  "call_id": "call_12345",
  "compliance_score": 0.75,
  "stages_completed": [
    "Introduction",
    "Needs Assessment"
  ],
  "stages_missing": [
    "Proposal",
    "Close"
  ],
  "recommendations": [
    "Add more qualification questions",
    "Include objection handling"
  ]
}
```

---

## 12. Performance & Analytics APIs

### 12.1 Get Performance Metrics

**Endpoint:** `GET /api/v1/analytics/performance/{company_id}`

**Description:** Get company-wide performance metrics

**Input Parameters:**
- `company_id` (path): Company identifier
- `date_range` (query): Optional date range filter

**Output:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "total_calls": 150,
  "conversion_rate": 0.25,
  "average_call_duration": 18.5,
  "lead_quality_score": 0.78,
  "objection_rate": 0.35
}
```

### 12.2 Get Rep Performance

**Endpoint:** `GET /api/v1/analytics/reps/{company_id}`

**Description:** Get individual rep performance data

**Input Parameters:**
- `company_id` (path): Company identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (performance_score, calls_handled, conversion_rate) (default: performance_score)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `min_performance_score` (query): Filter by minimum performance score (optional)
- `date_range` (query): Filter by date range (optional)

**Output:**
```json
{
  "reps": [
    {
      "rep_id": "rep_12345",
      "name": "Sarah Johnson",
      "performance_score": 0.85,
      "calls_handled": 45,
      "conversion_rate": 0.31,
      "coaching_recommendations": [
        "Improve objection handling",
        "Focus on qualification questions"
      ]
    }
  ]
}
```

### 12.3 Get Objection Analytics

**Endpoint:** `GET /api/v1/analytics/objections/{company_id}`

**Description:** Get objection frequency and impact analysis

**Input Parameters:**
- `company_id` (path): Company identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (frequency, impact_score, objection_type) (default: frequency)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `min_frequency` (query): Filter by minimum frequency count (optional)
- `date_range` (query): Filter by date range (optional)

**Output:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "objection_frequency": {
    "price": 45,
    "timing": 30,
    "authority": 25
  },
  "objection_impact": {
    "price": 0.65,
    "timing": 0.45,
    "authority": 0.35
  },
  "top_objections": [
    {
      "objection_type": "price",
      "frequency": 45,
      "impact_score": 0.65
    }
  ]
}
```

### 12.4 Get Lead Analytics

**Endpoint:** `GET /api/v1/analytics/leads/{company_id}`

**Description:** Get lead quality and source analytics

**Input Parameters:**
- `company_id` (path): Company identifier
- `limit` (query): Number of results (default: 20, max: 100)
- `offset` (query): Pagination offset (default: 0)
- `sort` (query): Sort order (quality_score, source, created_at) (default: quality_score)
- `order` (query): Sort direction (asc, desc) (default: desc)
- `quality_filter` (query): Filter by lead quality (hot, warm, cold) (optional)
- `source_filter` (query): Filter by lead source (optional)
- `date_range` (query): Filter by date range (optional)

**Output:**
```json
{
  "company_id": "550e8400-e29b-41d4-a716-446655440000",
  "lead_quality_distribution": {
    "hot": 25,
    "warm": 45,
    "cold": 30
  },
  "lead_sources": {
    "website": 40,
    "referral": 30,
    "cold_call": 20,
    "social": 10
  },
  "average_lead_score": 0.72
}
```

---

## 13. Webhooks

### 13.1 CallRail Call Completed

**Endpoint:** `POST /webhooks/callrail/call-completed`

**Description:** Handle CallRail webhook for completed calls

**Input Parameters:**
```json
{
  "event": "call.completed",
  "timestamp": "2025-01-15T10:30:00Z",
  "data": {
    "call_id": "call_12345",
    "company_id": "550e8400-e29b-41d4-a716-446655440000",
    "audio_url": "https://s3.amazonaws.com/callrail/audio.wav",
    "duration": 300,
    "caller_phone": "+1234567890"
  }
}
```

**Output:**
```json
{
  "status": "processed",
  "processing_id": "proc_12345"
}
```

### 13.2 CallRail Call Started

**Endpoint:** `POST /webhooks/callrail/call-started`

**Description:** Handle CallRail webhook for started calls

**Input Parameters:**
```json
{
  "event": "call.started",
  "timestamp": "2025-01-15T10:30:00Z",
  "data": {
    "call_id": "call_12345",
    "company_id": "550e8400-e29b-41d4-a716-446655440000",
    "caller_phone": "+1234567890"
  }
}
```

**Output:**
```json
{
  "status": "processed"
}
```

### 13.3 CallRail Recording Ready

**Endpoint:** `POST /webhooks/callrail/recording-ready`

**Description:** Handle CallRail webhook for recording availability

**Input Parameters:**
```json
{
  "event": "recording.ready",
  "timestamp": "2025-01-15T10:30:00Z",
  "data": {
    "call_id": "call_12345",
    "company_id": "550e8400-e29b-41d4-a716-446655440000",
    "recording_url": "https://s3.amazonaws.com/callrail/recording.wav"
  }
}
```

**Output:**
```json
{
  "status": "processed"
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "error": "bad_request",
  "message": "Invalid request parameters",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

### 401 Unauthorized
```json
{
  "error": "unauthorized",
  "message": "Invalid or missing authentication token",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

### 404 Not Found
```json
{
  "error": "not_found",
  "message": "Resource not found",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

### 429 Rate Limited
```json
{
  "error": "rate_limit_exceeded",
  "message": "Rate limit exceeded. Retry after 60 seconds.",
  "retry_after": 60,
  "timestamp": "2025-01-15T10:30:00Z"
}
```

### 500 Internal Server Error
```json
{
  "error": "internal_server_error",
  "message": "An unexpected error occurred",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

---

## Summary

This comprehensive API design covers all 45+ endpoints across 13 functional categories, providing detailed input/output parameters for:

- **System**: 1 endpoint for health monitoring
- **Call Data Ingestion**: 7 endpoints for call processing and metadata management
- **Document Data Ingestion**: 5 endpoints for SOP, training, reference documents, and UWC document processing
- **CRM Data Ingestion**: 2 endpoints for entity/event sourcing (contacts and opportunities handled via generic APIs)
- **Enhanced Summarization**: 5 endpoints for daily summaries, appointment summaries, prep briefs, history, and retrieval
- **Vector Maintenance**: 2 endpoints for vector deletion and reindexing (UWC)
- **Voice Intelligence**: 8 endpoints for AI-powered voice analysis
- **RAG/Ask Otto**: 2 endpoints for WebSocket-based natural language queries and query history
- **Personal AI**: 5 endpoints for AI clones and content generation
- **Follow-up**: 6 endpoints for task management and draft generation
- **SOP Management**: 6 endpoints for compliance tracking and analytics
- **Analytics**: 4 endpoints for performance metrics and business intelligence
- **Webhooks**: 3 endpoints for external system integration

Each endpoint includes comprehensive input/output schemas, error handling, and follows RESTful design principles with proper HTTP status codes and authentication requirements.

---

## API Endpoints Mapping to Otto Requirements

The following table maps each API endpoint to the Otto AI platform requirements and user roles:

| Category | API Endpoint | Description | User Role | Business Value |
|----------|--------------|-------------|-----------|----------------|
| **System** | `GET /health` | API health monitoring | All | System reliability |
| **Call Data Ingestion** | `POST /api/v1/calls` | Create call record from CallRail/VOIP | CSR, Manager | Ensures no leads are missed |
| **Call Data Ingestion** | `GET /api/v1/calls/{call_id}` | Retrieve call details and metadata | CSR, Rep, Manager | Complete call visibility |
| **Call Data Ingestion** | `PUT /api/v1/calls/{call_id}` | Update call status and metadata | CSR, Manager | Track call progression |
| **Call Data Ingestion** | `GET /api/v1/calls/{call_id}/status` | Get processing status | CSR, Rep, Manager | Monitor AI processing |
| **Call Data Ingestion** | `GET /api/v1/calls/{call_id}/audio` | Get signed URL for audio playback | CSR, Rep, Manager | Audio review and training |
| **Call Data Ingestion** | `GET /api/v1/calls/{call_id}/transcript` | Get transcript from S3 | CSR, Rep, Manager | Text analysis and coaching |
| **Call Data Ingestion** | `GET /api/v1/calls/{call_id}/diarization` | Get speaker diarization | CSR, Rep, Manager | Identify who spoke when |
| **Document Data Ingestion** | `POST /api/v1/ingestion/sop-documents` | Ingest SOP files for role-based training | Manager | Standardize sales processes |
| **Document Data Ingestion** | `POST /api/v1/ingestion/training-documents` | Ingest training materials | Manager | Knowledge base for coaching |
| **Document Data Ingestion** | `POST /api/v1/ingestion/reference-documents` | Ingest reference materials | Manager | Company-specific context |
| **Voice Intelligence** | `POST /api/v1/asr/transcribe` | Batch audio transcription | CSR, Rep | Convert speech to text |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/speakers` | Get speaker segments | CSR, Rep, Manager | Identify conversation participants |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/lead-classification` | Get lead qualification results | CSR, Manager | Identify qualified vs unqualified leads |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/objections` | Get objection analysis | CSR, Rep, Manager | Track and overcome objections |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/sop-analysis` | Get SOP compliance analysis | CSR, Rep, Manager | Ensure process adherence |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/coaching` | Get real-time coaching feedback | CSR, Rep | Improve performance |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/meeting-segments` | Get meeting phase segmentation | Rep, Manager | Structure appointment analysis |
| **Voice Intelligence** | `GET /api/v1/calls/{call_id}/rehash-score` | Get rehash scoring (1-5) | Rep, Manager | Prioritize follow-up attempts |
| **RAG/Ask Otto** | `WS /api/v1/rag/query` | Real-time interactive chat with Ask Otto | Manager, Executive | "Ask Otto" for insights with streaming responses |
| **RAG/Ask Otto** | `GET /api/v1/rag/queries` | Query history | Manager, Executive | Track AI interactions |
| **Personal AI** | `POST /api/v1/clone/{rep_id}/generate` | Generate content with personal clone | CSR, Rep | Personalized follow-ups |
| **Personal AI** | `GET /api/v1/clone/{rep_id}/drafts` | Get generated drafts | CSR, Rep | Review AI-generated content |
| **Personal AI** | `POST /api/v1/clone/{rep_id}/train` | Train personal clone | CSR, Rep | Improve AI personalization |
| **Personal AI** | `GET /api/v1/clone/{rep_id}/status` | Get clone training status | CSR, Rep, Manager | Monitor AI training |
| **Follow-up** | `POST /api/v1/ai/followup/draft` | Generate follow-up drafts | CSR, Rep | Automated follow-up content |
| **Follow-up** | `POST /api/v1/ai/followup/nurture` | Generate nurture follow-ups | CSR | Lead nurturing sequences |
| **Follow-up** | `POST /api/v1/ai/followup/rehash` | Generate rehash follow-ups | Rep | Re-engagement strategies |
| **Follow-up** | `GET /api/v1/calls/{call_id}/follow-up-tasks` | Get follow-up tasks | CSR, Rep, Manager | Task management |
| **Follow-up** | `POST /api/v1/calls/{call_id}/follow-up-tasks` | Create follow-up task | CSR, Rep, Manager | Task creation |
| **Follow-up** | `GET /api/v1/followup/{rep_id}/drafts` | Get all follow-up drafts | CSR, Rep | Draft management |
| **SOP Management** | `POST /api/v1/sop/stages` | Configure company SOP stages | Manager | Define sales processes |
| **SOP Management** | `GET /api/v1/sop/stages` | Get company SOP stages | CSR, Rep, Manager | Access process guidelines |
| **SOP Management** | `PUT /api/v1/sop/stages/{stage_id}` | Update SOP stage | Manager | Process optimization |
| **SOP Management** | `DELETE /api/v1/sop/stages/{stage_id}` | Delete SOP stage | Manager | Process maintenance |
| **SOP Management** | `GET /api/v1/sop/compliance/{company_id}` | Get compliance analytics | Manager | Track process adherence |
| **SOP Management** | `POST /api/v1/sop/compliance/analyze` | Analyze call compliance | Manager | Individual performance review |
| **Analytics** | `GET /api/v1/analytics/performance/{company_id}` | Get performance metrics | Manager, Executive | Business intelligence |
| **Analytics** | `GET /api/v1/analytics/reps/{company_id}` | Get rep performance | Manager | Individual coaching insights |
| **Analytics** | `GET /api/v1/analytics/objections/{company_id}` | Get objection analytics | Manager | Objection handling insights |
| **Analytics** | `GET /api/v1/analytics/leads/{company_id}` | Get lead analytics | Manager | Lead quality insights |
| **Webhooks** | `POST /webhooks/callrail/call-completed` | CallRail webhook for completed calls | System | Automated call processing |
| **Webhooks** | `POST /webhooks/callrail/call-started` | CallRail webhook for started calls | System | Real-time call tracking |
| **Webhooks** | `POST /webhooks/callrail/recording-ready` | CallRail webhook for recording availability | System | Audio processing trigger |

---

## Key Business Outcomes by API Category

### **Call Data Ingestion APIs**
- **Otto Save**: Automatic follow-up when CSR misses calls
- **No Leads Lost**: Every call is captured and processed
- **Complete Visibility**: Full call lifecycle tracking

### **Document Data Ingestion APIs**
- **Standardized Processes**: SOP enforcement across teams
- **Knowledge Base**: Training materials and reference docs
- **Role-Based Training**: Specific guidance for CSRs vs Reps


### **Voice Intelligence APIs**
- **Lead Classification**: Identify qualified vs unqualified leads
- **Objection Detection**: Track and overcome common objections
- **SOP Compliance**: Ensure process adherence
- **Real-Time Coaching**: Immediate feedback for improvement
- **Rehash Scoring**: Prioritize follow-up attempts (1-5 scale)

### **RAG/Ask Otto APIs**
- **Real-time Interactive Chat**: WebSocket-based "Ask Otto" for natural conversations
- **Streaming Responses**: Real-time answer generation with immediate feedback
- **Conversation Context**: Maintains session context for follow-up questions
- **Knowledge Retrieval**: Access to all company data with citations
- **Intelligent Suggestions**: AI suggests related questions and follow-ups

### **Personal AI APIs**
- **Personalized Content**: AI clones generate content in user's style
- **Daily Recaps**: Performance summaries and insights
- **Appointment Prep**: Pre-meeting briefs for reps
- **Adaptive Learning**: AI improves with user interaction

### **Follow-up APIs**
- **Centralized Tasks**: All follow-ups in one place
- **Automated Drafts**: AI-generated follow-up content
- **Nurture Sequences**: CSR lead nurturing
- **Rehash Strategies**: Rep re-engagement approaches

### **SOP Management APIs**
- **Process Definition**: Configure company-specific sales processes
- **Compliance Tracking**: Monitor adherence to processes
- **Performance Analytics**: Individual and team performance insights

### **Analytics APIs**
- **Performance Metrics**: Comprehensive business intelligence
- **Objection Analytics**: Objection frequency and impact analysis
- **Lead Analytics**: Lead quality and source analysis

### **Webhooks**
- **Real-time Integration**: CallRail and VOIP system integration
- **Automated Processing**: Trigger AI analysis on call completion
- **Event-driven Architecture**: Responsive to external events
