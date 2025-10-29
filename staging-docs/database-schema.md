# Otto AI RAG - Database Schema Documentation

**Last Updated**: October 28, 2025  
**Version**: 2.0  
**Database**: PostgreSQL 17.6

## Overview

This document describes the complete database schema for the Otto AI RAG system, including all tables, relationships, indexes, and constraints.

## Table of Contents

1. [Core Analysis Tables](#core-analysis-tables)
2. [SOP Management Tables](#sop-management-tables)
3. [Document Management Tables](#document-management-tables)
4. [Celery Task Tables](#celery-task-tables)
5. [Helper Functions](#helper-functions)
6. [Indexes](#indexes)
7. [Unique Constraints](#unique-constraints)

---

## Core Analysis Tables

### `call_transcripts`

Stores call transcriptions from the Shunya API.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL, UNIQUE | Unique call identifier (globally unique) |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier for multi-tenancy |
| `call_type` | VARCHAR(50) | NOT NULL | Type of call (e.g., 'sales', 'support') |
| `transcript` | TEXT | NOT NULL | Full call transcript |
| `speaker_segments` | JSONB | | Speaker-segmented transcript data |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT 'pending' | Processing status |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `processed_at` | TIMESTAMPTZ | | Processing completion timestamp |

**Indexes:**
- `idx_call_transcripts_call_id` on `call_id`
- `idx_call_transcripts_company_id` on `company_id`
- `idx_call_transcripts_status` on `status`

**Unique Constraint:** `call_transcripts_call_id_key` on `call_id`

---

### `call_summaries`

Stores AI-generated call summaries.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL | Reference to call |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `summary` | TEXT | NOT NULL | AI-generated summary |
| `key_points` | JSONB | | Array of key discussion points |
| `action_items` | JSONB | | Array of action items |
| `next_steps` | JSONB | | Array of next steps |
| `sentiment_score` | NUMERIC(3,2) | | Sentiment score (0.00-1.00) |
| `confidence_score` | NUMERIC(3,2) | | AI confidence score (0.00-1.00) |
| `processing_time` | INTEGER | | Processing time in milliseconds |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Unique Constraint:** `call_summaries_call_id_company_id_key` on `(call_id, company_id)`

---

### `objection_categories`

Master table for objection categories.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `category_text` | VARCHAR(100) | NOT NULL, UNIQUE | Category name |
| `description` | TEXT | NOT NULL | Category description |
| `is_active` | BOOLEAN | NOT NULL, DEFAULT TRUE | Active status |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Last update timestamp |

**Default Categories:**
- Pricing, Timing, Need, Authority, Trust, Competition, Product, Financing, Insurance, Other

---

### `call_objections`

Stores detected objections in calls.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL | Reference to call |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `objection_category_id` | INTEGER | NOT NULL, FK | Reference to objection category |
| `objection_text` | TEXT | NOT NULL | Full objection text |
| `speaker_id` | VARCHAR(50) | NOT NULL | Speaker identifier |
| `timestamp` | NUMERIC(10,2) | | Timestamp in call (seconds) |
| `overcome` | BOOLEAN | NOT NULL, DEFAULT FALSE | Whether objection was overcome |
| `confidence_score` | NUMERIC(3,2) | | AI confidence score |
| `severity` | VARCHAR(20) | | Objection severity level |
| `response_suggestions` | JSONB | | AI-generated response suggestions |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Indexes:**
- `idx_call_objections_call_id` on `call_id`
- `idx_call_objections_company_id` on `company_id`
- `idx_call_objections_category_id` on `objection_category_id`

**Foreign Key:** `objection_category_id` → `objection_categories(id)`

**Unique Constraint:** `call_objections_call_id_company_id_objection_category_id_sp_key` on `(call_id, company_id, objection_category_id, speaker_id, objection_text)`

---

### `call_lead_scores`

Stores BANT-based lead qualification scores.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL | Reference to call |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `overall_score` | NUMERIC(3,2) | NOT NULL | Overall BANT score (0.00-1.00) |
| `qualification_status` | VARCHAR(20) | | Status: hot/warm/cold |
| `bant_scores` | JSONB | NOT NULL | Individual BANT scores |
| `decision_makers` | JSONB | | Identified decision makers |
| `urgency_signals` | JSONB | | Detected urgency indicators |
| `budget_indicators` | JSONB | | Budget-related findings |
| `confidence_score` | NUMERIC(3,2) | | AI confidence score |
| `processing_time` | INTEGER | | Processing time in milliseconds |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Unique Constraint:** `call_lead_scores_call_id_company_id_key` on `(call_id, company_id)`

---

### `call_compliance_checks`

Stores SOP compliance analysis results.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL | Reference to call |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `compliance_score` | NUMERIC(3,2) | NOT NULL | Compliance score (0.00-1.00) |
| `violations` | JSONB | | Array of compliance violations |
| `recommendations` | JSONB | | Array of improvement recommendations |
| `sop_references` | JSONB | | Referenced SOP stages |
| `confidence_score` | NUMERIC(3,2) | | AI confidence score |
| `processing_time` | NUMERIC(8,2) | | Processing time in milliseconds |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Unique Constraint:** `call_compliance_checks_call_id_company_id_key` on `(call_id, company_id)`

---

### `call_analysis_status`

Tracks the orchestration status of call analysis pipeline.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `call_id` | INTEGER | NOT NULL | Reference to call |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `analysis_id` | VARCHAR(255) | | Analysis job identifier |
| `status` | VARCHAR(50) | NOT NULL | Overall status |
| `analysis_type` | VARCHAR(50) | | Type of analysis |
| `summarization_status` | VARCHAR(50) | | Summarization task status |
| `compliance_status` | VARCHAR(50) | | Compliance task status |
| `objections_status` | VARCHAR(50) | | Objection detection status |
| `qualification_status` | VARCHAR(50) | | Lead qualification status |
| `analysis_results` | JSONB | | Aggregated results |
| `error_message` | TEXT | | Error message if failed |
| `retry_count` | INTEGER | DEFAULT 0 | Number of retries |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Last update timestamp |
| `completed_at` | TIMESTAMPTZ | | Completion timestamp |

**Unique Constraint:** `call_analysis_status_call_id_company_id_key` on `(call_id, company_id)`

---

## SOP Management Tables

### `sop_stages`

Stores company-specific SOP stages.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `stage_name` | VARCHAR(100) | NOT NULL | Stage name |
| `stage_description` | TEXT | NOT NULL | Detailed stage description |
| `stage_order` | INTEGER | | Display order |
| `target_roles` | JSONB | | Array of applicable roles |
| `is_role_specific` | BOOLEAN | DEFAULT FALSE | Role-specific flag |
| `status` | VARCHAR(50) | DEFAULT 'active' | Stage status |
| `approval_status` | VARCHAR(50) | DEFAULT 'pending' | Approval status |
| `approved_by` | VARCHAR(255) | | Approver user ID |
| `created_by` | VARCHAR(255) | | Creator user ID |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Last update timestamp |
| `approved_at` | TIMESTAMPTZ | | Approval timestamp |

**Indexes:**
- `idx_sop_stages_company_id` on `company_id`
- `idx_sop_stages_status` on `status`

---

## Document Management Tables

### `documents`

Stores uploaded document metadata.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PRIMARY KEY | UUID primary key |
| `document_id` | VARCHAR(255) | NOT NULL, UNIQUE | Human-readable document ID |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `user_id` | VARCHAR(255) | NOT NULL | Uploader user ID |
| `document_name` | VARCHAR(255) | NOT NULL | Document name |
| `document_type` | VARCHAR(50) | NOT NULL | Document type (e.g., 'sop', 'manual') |
| `namespace` | VARCHAR(100) | NOT NULL | Milvus collection namespace |
| `original_file_path` | VARCHAR(500) | | S3 path to original file |
| `extracted_text_path` | VARCHAR(500) | | S3 path to extracted text |
| `original_file_name` | VARCHAR(255) | | Original filename |
| `file_size` | INTEGER | | File size in bytes |
| `mime_type` | VARCHAR(100) | | MIME type |
| `file_hash` | VARCHAR(64) | | SHA-256 hash |
| `status` | VARCHAR(50) | NOT NULL, DEFAULT 'uploaded' | Processing status |
| `processing_stage` | VARCHAR(50) | | Current processing stage |
| `progress` | INTEGER | DEFAULT 0 | Progress percentage |
| `chunks_created` | INTEGER | DEFAULT 0 | Number of chunks created |
| `vectors_stored` | BOOLEAN | DEFAULT FALSE | Vectors stored flag |
| `is_active` | BOOLEAN | DEFAULT TRUE | Active status |
| `deleted_at` | TIMESTAMPTZ | | Soft delete timestamp |
| `document_metadata` | JSONB | DEFAULT '{}' | Additional metadata |
| `processing_config` | JSONB | DEFAULT '{}' | Processing configuration |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Last update timestamp |
| `processed_at` | TIMESTAMPTZ | | Processing completion timestamp |

**Indexes:** Multiple indexes on `document_id`, `company_id`, `status`, `namespace`, etc.

---

### `document_chunks`

Stores text chunks for RAG retrieval.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `document_id` | VARCHAR(255) | NOT NULL, FK | Reference to document |
| `company_id` | VARCHAR(255) | NOT NULL | Company identifier |
| `chunk_text` | TEXT | NOT NULL | Chunk text content |
| `chunk_index` | INTEGER | NOT NULL | Chunk sequence number |
| `page_number` | INTEGER | | Source page number |
| `milvus_id` | VARCHAR(100) | | Milvus vector ID |
| `metadata` | JSONB | | Chunk metadata |
| `feedback_score` | INTEGER | CHECK (1-5) | User feedback score |
| `feedback_text` | TEXT | | User feedback text |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Foreign Key:** `document_id` → `documents(document_id)`

**Indexes:**
- `idx_document_chunks_document_id` on `document_id`
- `idx_document_chunks_company_id` on `company_id`

---

### `document_processing_logs`

Stores detailed processing logs for documents.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PRIMARY KEY | UUID primary key |
| `document_id` | VARCHAR(255) | NOT NULL, FK | Reference to document |
| `stage_name` | VARCHAR(100) | NOT NULL | Processing stage name |
| `log_level` | VARCHAR(20) | NOT NULL, DEFAULT 'INFO' | Log level |
| `message` | TEXT | NOT NULL | Log message |
| `details` | JSONB | | Additional details |
| `task_id` | VARCHAR(255) | | Celery task ID |
| `worker_id` | VARCHAR(255) | | Worker identifier |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |

**Foreign Key:** `document_id` → `documents(document_id)` ON DELETE CASCADE

---

## Celery Task Tables

### `celery_taskmeta`

Stores Celery task metadata and results.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `task_id` | VARCHAR(255) | NOT NULL, UNIQUE | Celery task ID |
| `name` | VARCHAR(255) | | Task name |
| `status` | VARCHAR(50) | NOT NULL | Task status |
| `result` | TEXT | | Task result (JSON) |
| `date_done` | TIMESTAMPTZ | DEFAULT NOW() | Completion timestamp |
| `traceback` | TEXT | | Error traceback |
| `meta` | JSONB | | Additional metadata |
| `args` | TEXT | | Task arguments |
| `kwargs` | TEXT | | Task keyword arguments |
| `worker` | VARCHAR(255) | | Worker identifier |
| `retries` | INTEGER | DEFAULT 0 | Retry count |
| `queue` | VARCHAR(255) | | Queue name |

**Indexes:** Multiple indexes on `task_id`, `status`, `name`, `date_done`

---

### `celery_tasksetmeta`

Stores Celery task group metadata.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing ID |
| `taskset_id` | VARCHAR(255) | NOT NULL, UNIQUE | Task group ID |
| `result` | JSONB | | Group result |
| `date_done` | TIMESTAMPTZ | DEFAULT NOW() | Completion timestamp |

---

### `task_logs`

Enhanced task logging with detailed tracking.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PRIMARY KEY | UUID primary key |
| `task_id` | VARCHAR(255) | NOT NULL | Task identifier |
| `document_id` | VARCHAR(255) | NOT NULL | Related document ID |
| `event_type` | VARCHAR(255) | NOT NULL | Event type |
| `message` | TEXT | | Event message |
| `event_metadata` | JSONB | | Event metadata |
| `status` | VARCHAR(50) | DEFAULT 'pending' | Task status |
| `progress` | INTEGER | DEFAULT 0 | Progress percentage |
| `current_step` | VARCHAR(255) | | Current processing step |
| `worker_id` | VARCHAR(255) | | Worker identifier |
| `queue_name` | VARCHAR(100) | | Queue name |
| `priority` | INTEGER | DEFAULT 0 | Task priority |
| `error_message` | TEXT | | Error message |
| `retry_count` | INTEGER | DEFAULT 0 | Retry count |
| `max_retries` | INTEGER | DEFAULT 3 | Max retries |
| `execution_time_ms` | INTEGER | | Execution time |
| `memory_usage_mb` | INTEGER | | Memory usage |
| `system_metadata` | JSONB | | System metadata |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Creation timestamp |
| `started_at` | TIMESTAMPTZ | | Start timestamp |
| `completed_at` | TIMESTAMPTZ | | Completion timestamp |

---

## Helper Functions

### `update_updated_at_column()`

Trigger function to automatically update `updated_at` timestamp.

```sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### `health_check()`

Simple health check function.

```sql
CREATE OR REPLACE FUNCTION health_check()
RETURNS TEXT AS $$
BEGIN
    RETURN 'Otto database is ready';
END;
$$ LANGUAGE plpgsql;
```

---

## Unique Constraints Summary

| Table | Constraint Name | Columns |
|-------|----------------|---------|
| `call_transcripts` | `call_transcripts_call_id_key` | `call_id` |
| `call_summaries` | `call_summaries_call_id_company_id_key` | `call_id, company_id` |
| `call_objections` | `call_objections_call_id_company_id_objection_category_id_sp_key` | `call_id, company_id, objection_category_id, speaker_id, objection_text` |
| `call_lead_scores` | `call_lead_scores_call_id_company_id_key` | `call_id, company_id` |
| `call_compliance_checks` | `call_compliance_checks_call_id_company_id_key` | `call_id, company_id` |
| `call_analysis_status` | `call_analysis_status_call_id_company_id_key` | `call_id, company_id` |
| `objection_categories` | `objection_categories_category_name_key` | `category_text` |
| `documents` | `documents_document_id_key` | `document_id` |

---

## Database Diagram

```
┌─────────────────────┐
│  call_transcripts   │
│  (Source)           │
└──────────┬──────────┘
           │
           ├─────────────────────┐
           │                     │
           ▼                     ▼
┌──────────────────┐   ┌──────────────────┐
│  call_summaries  │   │ call_objections  │◄─── objection_categories
└──────────────────┘   └──────────────────┘
           │
           ▼
┌──────────────────────┐
│  call_lead_scores    │
└──────────────────────┘
           │
           ▼
┌─────────────────────────┐
│ call_compliance_checks  │◄─── sop_stages
└─────────────────────────┘
           │
           ▼
┌─────────────────────────┐
│  call_analysis_status   │ (Orchestration)
└─────────────────────────┘
```

---

## Notes

- All tables use `TIMESTAMPTZ` for timezone-aware timestamps
- JSONB is used extensively for flexible, structured data storage
- Unique constraints prevent duplicate analysis results
- Foreign keys enforce referential integrity
- Indexes optimize query performance for common access patterns
- The schema supports multi-tenancy via `company_id`

---

**End of Schema Documentation**
