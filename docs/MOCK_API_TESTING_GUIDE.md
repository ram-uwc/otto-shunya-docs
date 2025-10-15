# 🧪 Otto AI Mock API - Complete Testing Guide

## 📋 **Mock Company Information**

### **Company Details**
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`
- **Company Name**: "Otto AI Test Company"
- **Industry**: Technology
- **Domain**: `otto-test.com`
- **Size**: Enterprise
- **Created**: 2023-01-15

---

## 👥 **Mock Users & Roles**

### **1. Admin User**
- **User ID**: `user_admin_001`
- **Name**: "John Admin"
- **Email**: `admin@otto-test.com`
- **Role**: `admin`
- **Permissions**: Full access to all endpoints
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`

### **2. Sales Manager**
- **User ID**: `user_mgr_001`
- **Name**: "Sarah Manager"
- **Email**: `manager@otto-test.com`
- **Role**: `sales_manager`
- **Permissions**: Manage team, view analytics, manage SOP
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`

### **3. Sales Rep**
- **User ID**: `user_rep_001`
- **Name**: "Mike Sales"
- **Email**: `sales@otto-test.com`
- **Role**: `sales_rep`
- **Permissions**: Handle calls, create follow-ups, view analytics
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`

### **4. CSR (Customer Service Representative)**
- **User ID**: `user_csr_001`
- **Name**: "Lisa Support"
- **Email**: `support@otto-test.com`
- **Role**: `csr`
- **Permissions**: Handle calls, view analytics
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`

### **5. Executive**
- **User ID**: `user_exec_001`
- **Name**: "David Executive"
- **Email**: `exec@otto-test.com`
- **Role**: `executive`
- **Permissions**: View analytics, view reports, manage company
- **Company ID**: `550e8400-e29b-41d4-a716-446655440000`

---

## 🔑 **JWT Token Generation**

### **Generate Tokens Using Mock API**

Instead of using hardcoded tokens, generate fresh tokens dynamically using the mock API:

#### **Available Roles**
- `admin` - System Administrator (full access)
- `sales_manager` - Sales Manager (team management, analytics, SOP)
- `sales_rep` - Sales Representative (calls, follow-ups, analytics)
- `csr` - Customer Service Representative (calls, analytics)
- `executive` - Executive (analytics, reports, company management)

#### **Generate Token for Any Role**
```bash
# Generate Admin Token
TOKEN_ADMIN=$(curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token')

# Generate Sales Manager Token
TOKEN_MANAGER=$(curl -s "$BASE_URL/mock/token?role=sales_manager" | jq -r '.token')

# Generate Sales Rep Token
TOKEN_REP=$(curl -s "$BASE_URL/mock/token?role=sales_rep" | jq -r '.token')

# Generate CSR Token
TOKEN_CSR=$(curl -s "$BASE_URL/mock/token?role=csr" | jq -r '.token')

# Generate Executive Token
TOKEN_EXEC=$(curl -s "$BASE_URL/mock/token?role=executive" | jq -r '.token')
```

#### **Token Response Format**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "role": "sales_rep",
  "expires_in": "30 minutes",
  "usage": "Add to Authorization header as 'Bearer <token>'"
}
```

#### **Quick Token Generation Script**
```bash
#!/bin/bash
# Generate all tokens at once
echo "🔑 Generating Mock API Tokens..."

export TOKEN_ADMIN=$(curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token')
export TOKEN_MANAGER=$(curl -s "$BASE_URL/mock/token?role=sales_manager" | jq -r '.token')
export TOKEN_REP=$(curl -s "$BASE_URL/mock/token?role=sales_rep" | jq -r '.token')
export TOKEN_CSR=$(curl -s "$BASE_URL/mock/token?role=csr" | jq -r '.token')
export TOKEN_EXEC=$(curl -s "$BASE_URL/mock/token?role=executive" | jq -r '.token')

echo "✅ All tokens generated successfully!"
echo "Admin Token: ${TOKEN_ADMIN:0:50}..."
echo "Manager Token: ${TOKEN_MANAGER:0:50}..."
echo "Rep Token: ${TOKEN_REP:0:50}..."
echo "CSR Token: ${TOKEN_CSR:0:50}..."
echo "Executive Token: ${TOKEN_EXEC:0:50}..."
```

---

## 🌐 **API Base URLs**

### **Local Development (Mock API)**
```bash
BASE_URL="http://localhost:8001"
```

### **Production**
```bash
BASE_URL="https://otto.shunyalabs.ai"
```

---

## 🔧 **Token Generation Examples**

### **Individual Token Generation**
```bash
# Generate tokens for specific roles
ADMIN_TOKEN=$(curl -s "http://localhost:8001/mock/token?role=admin" | jq -r '.token')
MANAGER_TOKEN=$(curl -s "http://localhost:8001/mock/token?role=sales_manager" | jq -r '.token')
REP_TOKEN=$(curl -s "http://localhost:8001/mock/token?role=sales_rep" | jq -r '.token')
CSR_TOKEN=$(curl -s "http://localhost:8001/mock/token?role=csr" | jq -r '.token')
EXEC_TOKEN=$(curl -s "http://localhost:8001/mock/token?role=executive" | jq -r '.token')

# Test token generation
echo "Admin Token: ${ADMIN_TOKEN:0:50}..."
echo "Manager Token: ${MANAGER_TOKEN:0:50}..."
```

### **Batch Token Generation Script**
```bash
#!/bin/bash
# generate_tokens.sh - Generate all mock API tokens

BASE_URL="http://localhost:8001"

echo "🔑 Generating Mock API Tokens..."
echo "Base URL: $BASE_URL"

# Generate all tokens
TOKEN_ADMIN=$(curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token')
TOKEN_MANAGER=$(curl -s "$BASE_URL/mock/token?role=sales_manager" | jq -r '.token')
TOKEN_REP=$(curl -s "$BASE_URL/mock/token?role=sales_rep" | jq -r '.token')
TOKEN_CSR=$(curl -s "$BASE_URL/mock/token?role=csr" | jq -r '.token')
TOKEN_EXEC=$(curl -s "$BASE_URL/mock/token?role=executive" | jq -r '.token')

# Export for use in other scripts
export TOKEN_ADMIN TOKEN_MANAGER TOKEN_REP TOKEN_CSR TOKEN_EXEC

echo "✅ All tokens generated successfully!"
echo "Admin: ${TOKEN_ADMIN:0:30}..."
echo "Manager: ${TOKEN_MANAGER:0:30}..."
echo "Rep: ${TOKEN_REP:0:30}..."
echo "CSR: ${TOKEN_CSR:0:30}..."
echo "Executive: ${TOKEN_EXEC:0:30}..."
```

### **Token Validation**
```bash
# Test if a token is valid by calling an authenticated endpoint
TOKEN=$(curl -s "http://localhost:8001/mock/token?role=admin" | jq -r '.token')

# Test the token
curl -H "Authorization: Bearer $TOKEN" \
     "http://localhost:8001/api/v1/auth/me" | jq .

# Expected response should include user info, not 401 Unauthorized
```

### **🎯 Generate Tokens Using Swagger UI (FastAPI Docs)**

For users who prefer a graphical interface, you can generate tokens directly from the Swagger UI:

#### **Step 1: Access Swagger UI**
```bash
# Local Development
http://localhost:8001/docs

# Production
https://otto.shunyalabs.ai/docs
```

#### **Step 2: Find the Mock Token Endpoint**
1. Navigate to the **System APIs** section
2. Look for **"Get Mock Token"** endpoint
3. Click on it to expand the details

#### **Step 3: Generate Token**
1. Click the **"Try it out"** button
2. In the **role** parameter field, enter one of these values:
   - `admin` - for admin access
   - `sales_manager` - for sales manager access  
   - `sales_rep` - for sales representative access
   - `csr` - for customer service representative access
   - `executive` - for executive access
3. Click **"Execute"**

#### **Step 4: Copy the Token**
The response will show:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "role": "admin",
  "expires_in": "30 minutes",
  "usage": "Add to Authorization header as 'Bearer <token>'"
}
```

#### **Step 5: Use Token in Swagger UI**
1. Click the **"Authorize"** button at the top of the Swagger UI
2. In the **"Value"** field, enter: `Bearer YOUR_TOKEN_HERE`
3. Click **"Authorize"**
4. Now you can test any authenticated endpoint directly in the UI!

#### **Visual Guide**
```
Swagger UI → System APIs → Get Mock Token → Try it out → 
Enter role → Execute → Copy token → Authorize → 
Enter "Bearer <token>" → Test endpoints
```

#### **Pro Tips for Swagger UI**
- **Multiple Tokens**: Generate tokens for different roles to test role-based access
- **Token Refresh**: Generate new tokens when they expire (30 minutes)
- **Copy & Paste**: Use the copy button in Swagger UI for easy token copying
- **Test All Endpoints**: Once authorized, you can test any endpoint directly in the UI

---

## 🧪 **Complete cURL Test Commands**

### **🔐 Authentication Endpoints**

#### **Get Current User Info**
```bash
# Admin
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/auth/me"

# Sales Manager
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/auth/me"

# Sales Rep
curl -H "Authorization: Bearer $TOKEN_REP" \
     "$BASE_URL/api/v1/auth/me"
```

#### **Health Check**
```bash
curl "$BASE_URL/api/v1/health"
```

---

### **📞 Call Management Endpoints**

#### **Get All Calls**
```bash
# Admin - All calls
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/calls/?company_id=550e8400-e29b-41d4-a716-446655440000"

# Sales Manager - Team calls
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/calls/?company_id=550e8400-e29b-41d4-a716-446655440000"

# Sales Rep - Own calls
curl -H "Authorization: Bearer $TOKEN_REP" \
     "$BASE_URL/api/v1/calls/?company_id=v"
```

#### **Get Specific Call**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/calls/call_12345"
```

#### **Get Call Transcript**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/calls/call_12345/transcript"
```

#### **Get Call Analysis**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/calls/call_12345/analysis"
```

---

### **📋 SOP (Standard Operating Procedures) Endpoints**

#### **Get SOP Stages** (Admin/Manager only)
```bash
# Admin
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/sop/stages?company_id=550e8400-e29b-41d4-a716-446655440000"

# Sales Manager
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/sop/stages?company_id=550e8400-e29b-41d4-a716-446655440000"
```

#### **Get SOP Analysis for Call**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/sop/call_12345/analysis"
```

#### **Create/Update SOP Stage** (Admin only)
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -H "Content-Type: application/json" \
     -H "x-company-id: 550e8400-e29b-41d4-a716-446655440000" \
     -H "x-request-id: request-001" \
     -d '{
       "stages": [
         {
           "stage_name": "Greeting",
           "stage_order": 1,
           "stage_description": "Greeting",
           "is_active": true
         }
       ]
     }' \
     "$BASE_URL/api/v1/sop/stages"
```

---

### **📊 Analytics Endpoints**

#### **Get Company Analytics** (Manager/Executive/Admin)
```bash
# Admin
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/analytics/550e8400-e29b-41d4-a716-446655440000"

# Sales Manager
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/analytics/550e8400-e29b-41d4-a716-446655440000"

# Executive
curl -H "Authorization: Bearer $TOKEN_EXEC" \
     "$BASE_URL/api/v1/analytics/550e8400-e29b-41d4-a716-446655440000"
```

#### **Get Performance Metrics**
```bash
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/analytics/performance/550e8400-e29b-41d4-a716-446655440000"
```

#### **Get Rep Performance**
```bash
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/analytics/reps/550e8400-e29b-41d4-a716-446655440000"
```

---

### **🤖 RAG (Retrieval-Augmented Generation) Endpoints**

#### **Query RAG System**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -H "Content-Type: application/json" \
     -d '{
       "query": "What are the top objections this week?",
       "company_id": "550e8400-e29b-41d4-a716-446655440000"
     }' \
     "$BASE_URL/api/v1/rag/query"
```

#### **Get RAG History**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/rag/history?company_id=550e8400-e29b-41d4-a716-446655440000"
```

---

### **📄 Document Management Endpoints**

#### **Upload Document**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -F "file=@document.pdf" \
     -F "file_type=sop" \
     -F "company_id=550e8400-e29b-41d4-a716-446655440000" \
     "$BASE_URL/api/v1/documents/upload"
```

#### **Get Documents**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/documents/?company_id=550e8400-e29b-41d4-a716-446655440000"
```

#### **Get Document Content**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/documents/doc_12345/content"
```

---

### **🎯 Follow-up Management Endpoints**

#### **Get Follow-ups**
```bash
curl -H "Authorization: Bearer $TOKEN_REP" \
     "$BASE_URL/api/v1/followup/?company_id=550e8400-e29b-41d4-a716-446655440000"
```

#### **Create Follow-up**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_REP" \
     -H "Content-Type: application/json" \
     -d '{
       "call_id": "call_12345",
       "follow_up_type": "callback",
       "scheduled_date": "2025-10-20T14:00:00Z",
       "notes": "Follow up on pricing discussion",
       "company_id": "550e8400-e29b-41d4-a716-446655440000"
     }' \
     "$BASE_URL/api/v1/followup/"
```

---

### **🎤 Voice & Audio Endpoints**

#### **Upload Audio File**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -F "audio_file=@call_recording.wav" \
     -F "call_id=call_12345" \
     -F "company_id=550e8400-e29b-41d4-a716-446655440000" \
     "$BASE_URL/api/v1/voice/upload"
```

#### **Get Audio Analysis**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/voice/call_12345/analysis"
```

---

### **🧠 Personal AI Endpoints**

#### **Generate Email Draft**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_REP" \
     -H "Content-Type: application/json" \
     -d '{
       "content_type": "email",
       "prompt": "Follow up email for call_12345",
       "company_id": "550e8400-e29b-41d4-a716-446655440000"
     }' \
     "$BASE_URL/api/v1/personal-ai/generate"
```

#### **Get AI Drafts**
```bash
curl -H "Authorization: Bearer $TOKEN_REP" \
     "$BASE_URL/api/v1/personal-ai/drafts?company_id=550e8400-e29b-41d4-a716-446655440000"
```

---

### **📈 CRM Integration Endpoints**

#### **Sync CRM Data**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -H "Content-Type: application/json" \
     -d '{
       "crm_system": "salesforce",
       "company_id": "550e8400-e29b-41d4-a716-446655440000"
     }' \
     "$BASE_URL/api/v1/crm/sync"
```

#### **Get CRM Contacts**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/crm/contacts?company_id=550e8400-e29b-41d4-a716-446655440000"
```

---

### **📊 Summary & Reports Endpoints**

#### **Get Daily Summary**
```bash
curl -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/summaries/daily?company_id=550e8400-e29b-41d4-a716-446655440000&date=2025-10-15"
```

#### **Get Weekly Report**
```bash
curl -H "Authorization: Bearer $TOKEN_EXEC" \
     "$BASE_URL/api/v1/reports/weekly?company_id=550e8400-e29b-41d4-a716-446655440000&week=2025-42"
```

---

### **🔗 Webhook Endpoints**

#### **Register Webhook**
```bash
curl -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -H "Content-Type: application/json" \
     -d '{
       "url": "https://your-app.com/webhook",
       "events": ["call_completed", "follow_up_created"],
       "company_id": "550e8400-e29b-41d4-a716-446655440000"
     }' \
     "$BASE_URL/api/v1/webhooks/"
```

#### **Get Webhooks**
```bash
curl -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/webhooks/?company_id=550e8400-e29b-41d4-a716-446655440000"
```

---

## 🚀 **Quick Test Script**

### **Set Environment Variables & Generate Tokens**
```bash
# Set base URL
export BASE_URL="http://localhost:8001"  # or "https://otto.shunyalabs.ai" for production
export COMPANY_ID="550e8400-e29b-41d4-a716-446655440000"

# Generate fresh tokens using Mock API
echo "🔑 Generating fresh tokens from Mock API..."
export TOKEN_ADMIN=$(curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token')
export TOKEN_MANAGER=$(curl -s "$BASE_URL/mock/token?role=sales_manager" | jq -r '.token')
export TOKEN_REP=$(curl -s "$BASE_URL/mock/token?role=sales_rep" | jq -r '.token')
export TOKEN_CSR=$(curl -s "$BASE_URL/mock/token?role=csr" | jq -r '.token')
export TOKEN_EXEC=$(curl -s "$BASE_URL/mock/token?role=executive" | jq -r '.token')

echo "✅ Tokens generated successfully!"
```

### **Test All Endpoints**
```bash
#!/bin/bash

echo "🧪 Testing Otto AI Mock API Endpoints"
echo "======================================"

# Health Check
echo "1. Health Check"
curl -s "$BASE_URL/api/v1/health" | jq .

# Auth - Get User Info
echo "2. Get User Info (Admin)"
curl -s -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/auth/me" | jq .

# SOP Stages
echo "3. Get SOP Stages"
curl -s -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/sop/stages?company_id=$COMPANY_ID" | jq .

# Calls
echo "4. Get Calls"
curl -s -H "Authorization: Bearer $TOKEN_ADMIN" \
     "$BASE_URL/api/v1/calls/?company_id=$COMPANY_ID" | jq .

# Analytics
echo "5. Get Analytics"
curl -s -H "Authorization: Bearer $TOKEN_MANAGER" \
     "$BASE_URL/api/v1/analytics/$COMPANY_ID" | jq .

# RAG Query
echo "6. RAG Query"
curl -s -X POST \
     -H "Authorization: Bearer $TOKEN_ADMIN" \
     -H "Content-Type: application/json" \
     -d "{\"query\": \"What are the top objections?\", \"company_id\": \"$COMPANY_ID\"}" \
     "$BASE_URL/api/v1/rag/query" | jq .

echo "✅ All tests completed!"
```

---

## 📚 **API Documentation**

### **Interactive API Testing (Recommended)**
- **Swagger UI (Local)**: `http://localhost:8001/docs` - **Use this to generate tokens and test endpoints!**
- **Swagger UI (Production)**: `https://otto.shunyalabs.ai/docs`

### **Alternative Documentation**
- **ReDoc (Local)**: `http://localhost:8001/redoc`
- **ReDoc (Production)**: `https://otto.shunyalabs.ai/redoc`
- **OpenAPI Spec (Local)**: `http://localhost:8001/openapi.json`
- **OpenAPI Spec (Production)**: `https://otto.shunyalabs.ai/openapi.json`

### **🎯 Quick Start with Swagger UI**
1. Open `http://localhost:8001/docs` in your browser
2. Go to **System APIs** → **Get Mock Token**
3. Generate a token for your desired role
4. Click **"Authorize"** and enter `Bearer <your_token>`
5. Test any endpoint directly in the UI!

---

## 🔧 **Troubleshooting**

### **Common Issues**

1. **401 Unauthorized**: Check if token is valid and not expired
2. **403 Forbidden**: Check if user role has required permissions
3. **404 Not Found**: Verify endpoint URL and company_id parameter
4. **422 Validation Error**: Check request body format and required fields

### **Token Expiration**
All tokens expire in 3600 minutes. Generate new tokens using the Mock API:
```bash
# Generate a fresh token for any role
curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token'

# Or generate all tokens at once
export TOKEN_ADMIN=$(curl -s "$BASE_URL/mock/token?role=admin" | jq -r '.token')
export TOKEN_MANAGER=$(curl -s "$BASE_URL/mock/token?role=sales_manager" | jq -r '.token')
export TOKEN_REP=$(curl -s "$BASE_URL/mock/token?role=sales_rep" | jq -r '.token')
export TOKEN_CSR=$(curl -s "$BASE_URL/mock/token?role=csr" | jq -r '.token')
export TOKEN_EXEC=$(curl -s "$BASE_URL/mock/token?role=executive" | jq -r '.token')
```

---

**🎉 Happy Testing! This guide covers all available mock API endpoints with proper authentication and role-based access control.**
