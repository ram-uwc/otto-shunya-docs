# Otto AI RAG System Documentation

## 🎯 Overview

The Otto AI RAG (Retrieval-Augmented Generation) system is a comprehensive call analysis platform that processes audio calls, extracts insights, and provides AI-powered analysis including objection detection, lead qualification, compliance checking, and summarization.

## 🏗️ System Architecture

### Core Components

1. **API Service** (`services/api/`) - FastAPI-based REST API
2. **Worker Service** (`services/workers/`) - Celery-based background task processing
3. **Mock API** (`services/mock-api/`) - Development and testing API
4. **Database** - PostgreSQL with 14 optimized tables
5. **Message Queue** - Redis for Celery task management

### Database Schema (14 Tables)

#### Call Analysis Tables
- `sample call recording` -  https://otto-call-recording.s3.us-east-1.amazonaws.com/req_call_0001.mp3
- `call_transcripts` - Audio transcription results with speaker diarization
- `call_summaries` - AI-generated call summaries
- `call_objections` - Detected objections with categorization
- `call_lead_scores` - Lead qualification scoring (BANT analysis)
- `call_compliance_checks` - SOP compliance analysis
- `call_analysis_status` - Processing status tracking

#### Master Data Tables
- `objection_categories` - Predefined objection types (Pricing, Timing, Need, etc.)
- `sop_stages` - Standard Operating Procedure definitions

#### Document Processing Tables
- `documents` - Document metadata and file paths
- `document_chunks` - Text segments for RAG processing
- `document_processing_logs` - Processing pipeline tracking

#### System Tables
- `task_logs` - Celery task execution logs
- `celery_taskmeta` - Celery result backend
- `celery_tasksetmeta` - Celery task group management

## 🚀 Key Features

### 1. Call Transcription
- **Audio Processing**: Shunya ASR integration
- **Speaker Diarization**: Automatic speaker identification
- **Status Tracking**: Real-time processing status

### 2. Objection Detection
- **AI-Powered Analysis**: LLM-based objection identification
- **Categorized Detection**: 10 predefined objection categories
- **Overcome Tracking**: Monitors if objections were addressed

### 3. Lead Qualification
- **BANT Analysis**: Budget, Authority, Need, Timeline scoring
- **Decision Maker Identification**: Key stakeholder detection
- **Urgency Signals**: Timeline and priority assessment

### 4. Compliance Checking
- **SOP Validation**: Standard operating procedure compliance
- **Violation Detection**: Automated compliance monitoring
- **Recommendations**: AI-generated improvement suggestions

### 5. Call Summarization
- **Key Points Extraction**: Important conversation highlights
- **Action Items**: Follow-up tasks and commitments
- **Sentiment Analysis**: Call tone and outcome assessment

## 🔧 Technical Implementation

### Upsert Pattern
All analysis services implement PostgreSQL upsert (`INSERT ... ON CONFLICT DO UPDATE`) to prevent duplicate records and enable reprocessing.

### Service Architecture
- **Service Layer**: Core business logic encapsulation
- **API Layer**: RESTful endpoints with JWT authentication
- **Task Layer**: Asynchronous background processing
- **Database Layer**: Optimized queries with proper indexing

### Authentication
- **JWT-Based**: Token-based authentication system
- **Multi-Tenant**: Company-based data isolation
- **Role-Based**: Sales rep, manager, admin permissions

## 📊 API Endpoints

### Core Analysis APIs
- `POST /api/v1/transcription/transcribe` - Audio transcription
- `POST /api/v1/objection-detection/detect` - Objection analysis
- `POST /api/v1/lead-qualification/qualify` - Lead scoring
- `POST /api/v1/sop/compliance/check` - Compliance validation
- `POST /api/v1/summarization/summarize` - Call summarization

### Status & Results APIs
- `GET /api/v1/transcription/status/{call_id}` - Transcription status
- `GET /api/v1/analysis/objections/{call_id}` - Objection results
- `GET /api/v1/analysis/qualification/{call_id}` - Qualification results
- `GET /api/v1/analysis/compliance/{call_id}` - Compliance results
- `GET /api/v1/analysis/summary/{call_id}` - Summary results

### Document Management APIs
- `POST /api/v1/ingestion/upload` - Document upload
- `GET /api/v1/search/query` - RAG-based search
- `POST /api/v1/chunks/feedback` - Chunk quality feedback

## 🛠️ Development Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- PostgreSQL 13+
- Redis 6+

### Quick Start
```bash
# Clone repository
git clone <repository-url>
cd ottoai-rag

# Start services
docker-compose up -d

# Initialize database
docker-compose exec ottoai-rag-otto-api-1 python scripts/init_db.py

# Seed objection categories
docker-compose exec ottoai-rag-postgres-1 psql -U otto_user -d otto_dev -f /path/to/seed_objection_categories.sql
```

### Environment Configuration
- Copy `env.example` to `.env`
- Configure database, Redis, and API settings
- Set up JWT secrets and API keys

## 📈 Performance & Scalability

### Database Optimization
- **Unique Constraints**: Prevent duplicate processing
- **Indexes**: Optimized query performance
- **JSONB Fields**: Flexible data storage for complex objects

### Background Processing
- **Celery Workers**: Scalable task processing
- **Redis Queue**: Reliable message delivery
- **Task Monitoring**: Comprehensive logging and status tracking

### Caching Strategy
- **Redis Caching**: Session and temporary data
- **Database Indexing**: Query optimization
- **Connection Pooling**: Efficient database connections

## 🔒 Security & Compliance

### Data Protection
- **Multi-Tenant Isolation**: Company-based data separation
- **JWT Authentication**: Secure API access
- **Input Validation**: Pydantic model validation
- **SQL Injection Prevention**: SQLAlchemy ORM protection

### Audit Trail
- **Processing Logs**: Complete task execution history
- **Status Tracking**: Real-time processing visibility
- **Error Logging**: Comprehensive error handling

## 📚 Additional Documentation

- [API Reference](./api-reference.md) - Complete API documentation
- [Database Schema](./database-schema.md) - Detailed table structures
- [Deployment Guide](./deployment.md) - Production deployment instructions
- [Testing Guide](./testing.md) - Testing strategies and examples
- [Troubleshooting](./troubleshooting.md) - Common issues and solutions

## 🤝 Contributing

1. Follow the established service architecture patterns
2. Implement proper error handling and logging
3. Add comprehensive tests for new features
4. Update documentation for API changes
5. Follow the upsert pattern for data consistency

## 📞 Support

For technical support or questions about the Otto AI RAG system, please refer to the troubleshooting guide or contact the development team.
