# Otto AI - Client Demo Guide

**Date:** October 30, 2025  
**Purpose:** Step-by-step guide for demonstrating Otto AI RAG system to clients  
**Valid Until:** November 6, 2025 (1 week)

---

## 📋 Table of Contents

1. [Setup & Authentication](#setup--authentication)
2. [Demo Flow Overview](#demo-flow-overview)
3. [Step 1: List Approved SOP Stages](#step-1-list-approved-sop-stages-for-csr-role)
4. [Step 2: Upload Audio for Transcription](#step-2-upload-audio-url-for-transcription)
5. [Step 3: Check Analysis Status](#step-3-check-status-of-all-analysis)
6. [Step 4: Get Complete Analysis](#step-4-get-complete-analysis)
7. [Step 5: Get Individual Analysis](#step-5-get-individual-analysis)
8. [Troubleshooting](#troubleshooting)

---

## 🔐 Setup & Authentication

### Demo Credentials

**JWT Token (Valid for 1 week - Expires: November 6, 2025)**

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g
```

**User Details:**
```json
{
  "user_id": "demo-csr-user",
  "email": "",
  "name": null,
  "role": "customer_rep",
  "company_id": "test_company_1",
  "permissions": ["read"],
  "api_version": "v1"
}
```

### Accessing Swagger UI

1. **Open Swagger in Browser:**
   ```
   https://otto.shunyalabs.ai/docs
   ```
   
2. **Authorize in Swagger:**
   - Click the **"Authorize"** button (🔓) at the top right
   - In the **"HTTPBearer (http, Bearer)"** field, paste the JWT token above
   - Click **"Authorize"**
   - Click **"Close"**

✅ You're now authenticated for all API requests!

---

## 🎯 Demo Flow Overview

```
1. List SOP Stages (CSR Role)
   ↓
2. Upload Audio URL for Transcription
   ↓
3. Wait & Check Analysis Status
   ↓
4. Get Complete Analysis Results
   ↓
5. View Individual Analysis Components
```

**Estimated Demo Time:** 15-20 minutes

---

## Step 1: List Approved SOP Stages for CSR Role

**Purpose:** Show the SOP stages that are approved for customer service representatives.

### Using Swagger UI

1. **Locate Endpoint:**
   - Scroll to **"SOP"** section
   - Find: **GET** `/api/v1/sop/stages`

2. **Execute Request:**
   - Click **"Try it out"**
   - **Query Parameters:**
     - `target_role`: `customer_rep` (or leave empty to see all)
     - `status`: `approved` (optional)
   - Click **"Execute"**

3. **Expected Response:**
   ```json
   {
     "success": true,
     "stages": [
       {
         "id": 1,
         "stage_name": "Initial Greeting",
         "description": "Welcome the customer and establish rapport",
         "stage_order": 1,
         "target_roles": ["customer_rep"],
         "status": "approved",
         "rules": ["Always greet warmly", "Use customer's name"]
       },
       {
         "id": 2,
         "stage_name": "Issue Identification",
         "description": "Understand customer's problem or request",
         "stage_order": 2,
         "target_roles": ["customer_rep"],
         "status": "approved"
       }
     ],
     "total": 2
   }
   ```

### Using cURL

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/sop/stages?target_role=customer_rep&status=approved" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

**🎯 Demo Talking Points:**
- Show how SOPs are role-specific
- Explain the stage order and compliance checking
- Mention how these are extracted from uploaded SOP documents

---

## Step 2: Upload Audio URL for Transcription

**Purpose:** Submit a call recording for transcription and automated analysis.

### Using Swagger UI

1. **Locate Endpoint:**
   - Scroll to **"Transcription"** section
   - Find: **POST** `/api/v1/transcription/transcribe`

2. **Execute Request:**
   - Click **"Try it out"**
   - **Request Body:**
     ```json
     {
       "call_id": 3001,
       "audio_url": "https://otto-call-recording.s3.us-east-1.amazonaws.com/req_call_0001.mp3",
       "call_type": "csr_call"
     }
     ```
   - Click **"Execute"**

3. **Expected Response:**
   ```json
   {
     "success": true,
     "message": "Transcription task started successfully",
     "task_id": "celery-task-abc123"
   }
   ```

### Using cURL

```bash
curl -X POST "https://otto.shunyalabs.ai/api/v1/transcription/transcribe" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g" \
  -H "Content-Type: application/json" \
  -d '{
    "call_id": 3001,
    "audio_url": "https://otto-call-recording.s3.us-east-1.amazonaws.com/req_call_0001.mp3",
    "call_type": "csr_call"
  }'
```

**🎯 Demo Talking Points:**
- Audio is processed asynchronously using Celery workers
- Transcription uses Shunya Labs / Whisper ASR
- After transcription, analysis pipeline is automatically triggered
- Process includes: Summarization, Compliance, Objections, Lead Qualification

**⏱️ Processing Time:** Typically 30 seconds - 2 minutes depending on audio length

---

## Step 3: Check Status of All Analysis

**Purpose:** Monitor the progress of transcription and all analysis components.

### Option A: Check Transcription Status

1. **Locate Endpoint:**
   - **GET** `/api/v1/transcription/status/{call_id}`

2. **Execute Request:**
   - Click **"Try it out"**
   - Enter `call_id`: `3001`
   - Click **"Execute"**

3. **Expected Response:**
   ```json
   {
     "success": true,
     "transcript_id": 789,
     "call_id": 3001,
     "status": "completed",
     "created_at": "2025-10-30T12:00:00Z",
     "processed_at": "2025-10-30T12:01:30Z"
   }
   ```

### Option B: Check Overall Analysis Status

1. **Locate Endpoint:**
   - Scroll to **"Call Analysis"** section
   - Find: **GET** `/api/v1/call-analysis/status/{call_id}`

2. **Execute Request:**
   - Click **"Try it out"**
   - Enter `call_id`: `3001`
   - Click **"Execute"**

3. **Expected Response:**
   ```json
   {
     "success": true,
     "call_id": 3001,
     "company_id": "test_company_1",
     "overall_status": "completed",
     "analysis_components": {
       "summarization": "completed",
       "compliance": "completed",
       "objections": "completed",
       "qualification": "completed",
       "rehash": "completed",
       "segmentation": "completed"
     },
     "created_at": "2025-10-30T12:00:00Z",
     "completed_at": "2025-10-30T12:02:00Z"
   }
   ```

### Using cURL

```bash
# Check transcription status
curl -X GET "https://otto.shunyalabs.ai/api/v1/transcription/status/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"

# Check analysis status
curl -X GET "https://otto.shunyalabs.ai/api/v1/call-analysis/status/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

**🎯 Demo Talking Points:**
- Real-time status tracking for all analysis components
- Each analysis runs independently for resilience
- Status values: `pending`, `processing`, `completed`, `failed`

---

## Step 4: Get Complete Analysis

**Purpose:** Retrieve all analysis results in a single comprehensive response.

### Using Swagger UI

1. **Locate Endpoint:**
   - Scroll to **"Call Analysis"** section
   - Find: **GET** `/api/v1/call-analysis/{call_id}`

2. **Execute Request:**
   - Click **"Try it out"**
   - Enter `call_id`: `3001`
   - Click **"Execute"**

3. **Expected Response:**
   ```json
   {
     "success": true,
     "call_id": 3001,
     "company_id": "test_company_1",
     "transcript": "Full call transcript here...",
     "summary": {
       "overview": "Customer called regarding billing issue...",
       "key_points": ["Billing discrepancy", "Requested refund"],
       "action_items": ["Process refund request", "Update billing system"],
       "sentiment": "neutral"
     },
     "compliance": {
       "compliant": true,
       "sop_adherence_score": 85,
       "violations": [],
       "recommendations": ["Consider mentioning warranty terms"]
     },
     "objections": [
       {
         "objection": "Price too high",
         "category": "price",
         "response": "Explained value proposition",
         "outcome": "resolved"
       }
     ],
     "lead_qualification": {
       "score": 75,
       "qualification": "qualified",
       "budget": "confirmed",
       "authority": "confirmed",
       "need": "confirmed",
       "timeline": "within_3_months"
     },
     "rehash_analysis": {
       "rehash_score": 4,
       "what_went_wrong": "Customer needs more time to evaluate",
       "rehash_strategy": "Follow up in 2 weeks with case studies"
     },
     "meeting_segmentation": {
       "part1_duration": 45,
       "part2_duration": 120,
       "transition_point": 45,
       "meeting_structure_score": 4
     }
   }
   ```

### Using cURL

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/call-analysis/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

**🎯 Demo Talking Points:**
- Single API call returns all analysis results
- AI-powered insights for every call
- Actionable recommendations for follow-up
- Compliance checking against company SOPs

---

## Step 5: Get Individual Analysis

**Purpose:** Retrieve specific analysis components separately.

### 5.1 Get Transcript Only

**Endpoint:** `GET /api/v1/transcription/transcript/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/transcription/transcript/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

**Response:**
```json
{
  "success": true,
  "call_id": 3001,
  "transcript": "Full transcript with speaker labels...",
  "speaker_segments": [
    {
      "speaker": "Agent",
      "text": "Hello, how can I help you?",
      "start_time": 0.0,
      "end_time": 2.5
    }
  ]
}
```

---

### 5.2 Get Summary Only

**Endpoint:** `GET /api/v1/summarization/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/summarization/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

### 5.3 Get Compliance Check

**Endpoint:** `GET /api/v1/call-analysis/compliance/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/call-analysis/compliance/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

### 5.4 Get Objection Detection

**Endpoint:** `GET /api/v1/objection-detection/analysis/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/objection-detection/analysis/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

### 5.5 Get Lead Qualification

**Endpoint:** `GET /api/v1/lead-qualification/analysis/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/lead-qualification/analysis/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

### 5.6 Get Rehash Analysis

**Endpoint:** `GET /api/v1/rehash-analysis/analysis/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/rehash-analysis/analysis/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

### 5.7 Get Meeting Segmentation

**Endpoint:** `GET /api/v1/meeting-segmentation/analysis/{call_id}`

```bash
curl -X GET "https://otto.shunyalabs.ai/api/v1/meeting-segmentation/analysis/3001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtby1jc3ItdXNlciIsImNvbXBhbnlfaWQiOiJ0ZXN0X2NvbXBhbnlfMSIsInJvbGUiOiJjdXN0b21lcl9yZXAiLCJleHAiOjE3NjI0MTE4MDgsImlhdCI6MTc2MTgwNzAwOCwidHlwZSI6ImFjY2VzcyJ9.iig12X4SaHM-NMIEF2UFXKO1xck-AWAYSJxADo9z_0g"
```

---

## 🔍 Troubleshooting

### Issue: "Unauthorized" Error

**Solution:**
1. Check if JWT token is copied correctly (no extra spaces)
2. Ensure you clicked "Authorize" in Swagger UI
3. Verify token hasn't expired (valid until November 6, 2025)

---

### Issue: "Call not found"

**Solution:**
1. Verify the `call_id` is correct
2. Ensure the call belongs to `test_company_1`
3. Check if transcription has completed first

---

### Issue: Analysis showing "pending"

**Solution:**
1. Wait 30-60 seconds for processing
2. Check Celery workers are running: `docker ps | grep worker`
3. Check logs: `docker logs <worker-container-id>`

---

### Issue: Empty results

**Solution:**
1. Confirm transcription completed successfully
2. Check if analysis pipeline was triggered
3. Verify call_type matches expected analysis (e.g., sales_call for lead qualification)


---


---

**Good luck with your demo! 🚀**

