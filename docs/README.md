# Otto AI Platform Documentation

## 📚 Comprehensive Documentation

This section provides access to all comprehensive documentation files for the Otto AI platform, including API specifications, authentication systems, and integration details.

### 🔧 Core API Documentation

#### [Comprehensive API Design](./comprehensive-api-design.md)
**Complete API specification with 42+ endpoints across 13 functional categories**

- **Call Data Ingestion**: 7 endpoints for call processing and metadata management
- **Document Data Ingestion**: 5 endpoints for SOP, training, reference documents, and UWC document processing
- **Voice Intelligence**: 8 endpoints for AI-powered voice analysis
- **RAG/Ask Otto**: 2 endpoints for WebSocket-based natural language queries
- **Personal AI**: 5 endpoints for AI clones and content generation
- **Follow-up**: 6 endpoints for task management and draft generation
- **SOP Management**: 6 endpoints for compliance tracking and analytics
- **Analytics**: 4 endpoints for performance metrics and business intelligence
- **Webhooks**: 3 endpoints for external system integration

**Key Features:**
- Complete request/response schemas with examples
- Error handling specifications
- Business value mapping for each endpoint
- Role-based access control documentation

#### [Comprehensive API OpenAPI Specification](./comprehensive-api-openapi.yaml)
**OpenAPI 3.0.3 specification for all endpoints**

- **Format**: YAML specification file
- **Version**: 3.0.3
- **Endpoints**: 42+ endpoints with complete schemas
- **Authentication**: JWT Bearer token + Company ID headers
- **Environments**: Production, staging, and local development URLs

**Usage:**
- Import into Postman for API testing
- Generate client SDKs automatically
- Validate API requests and responses
- Interactive API documentation

### 🔐 Authentication & Security

#### [Comprehensive Authentication Documentation](./comprehensive_authentication_doc.md)
**Complete authentication system with 4-role RBAC and Clerk integration**

- **4-Role System**: Admin, Manager, CSR, Sales Rep with distinct permissions
- **Clerk Integration**: Frontend authentication with JWT token verification
- **Role-Based Data Access**: Company-wide vs individual data access for RAG/Ask Otto
- **Permission Matrix**: Detailed access control for all API categories
- **Security Implementation**: JWT verification, HMAC signatures, multi-tenant isolation

**Key Components:**
- Authentication flow diagrams
- Permission matrix tables
- Role-based data access examples
- Security middleware implementation
- UWC integration authentication

### 📊 Requirements & Specifications

#### [Comprehensive Requirements Response](./comprehensive-requirements-response.md)
**Complete requirements documentation with performance SLAs and testing resources**

- **Performance SLAs**: Latency targets, rate limits, timeouts, and availability for each endpoint category
- **Rate Limiting**: for ASR details given for all APIS we can have autoscale to handle load
- **Storage and Retention**: Data retention policies and storage limits
- **Testing Resources**: Sample RAG queries with mock responses, webhook payloads

**Key Features:**
- Performance specifications table
- Sample RAG queries and responses
- UWC integration endpoints
- Testing resource specifications

### 🗄️ Database Schema

#### [Comprehensive Database Schema](./comprehensive-db-schema.md)
**Complete database schema with PostgreSQL + Milvus integration**

- **Multi-tenant Architecture**: Company-based isolation with role-based access control
- **PostgreSQL Tables**: Business entities, users, calls, documents, analytics, and audit trails
- **Milvus Integration**: Vector storage and content for RAG operations
- **UWC Integration**: Entity management and event sourcing
- **Performance Optimization**: Indexing strategy and query optimization

**Key Features:**
- 19 core business tables with complete schemas
- Milvus collection strategy for vector operations
- RAG namespace partitioning by company/type/role
- Data retention and archival policies
- Security implementation with RLS and encryption

### 📧 Communication

#### [Requirements Summary Email](./requirements-summary-email.md)
**Executive summary email for stakeholders and development teams**

- **Status**: 98% complete documentation
- **Key Achievements**: 42+ endpoints, authentication system, performance SLAs
- **Development Readiness**: All major components documented
- **Next Steps**: Timeline for development and testing phases
- **Business Impact**: Sales intelligence, analytics, AI-powered features

**Audience:**
- Development teams
- Stakeholders
- UWC integration partners
- Product management

### Mock API Features
- **50+ Endpoints**: Complete API coverage including calls, analytics, SOP, RAG, and more
- **Role-Based Access**: Test different user permissions and access levels
- **Realistic Data**: Generated mock data that mimics real business scenarios
- **Interactive Testing**: Swagger UI for easy endpoint testing
- **Token Management**: Dynamic token generation with 3600-minute expiration

## 📖 API Documentation

### Mock API


- **Swagger UI**: http://otto.shunyalabs.ai/docs

### Mock API (Testing)
- **Swagger UI**: https://otto.shunyalabs.ai/docs - **Interactive testing with token generation**

## 🚀 Quick Start Guide

### For Developers
1. **Start with**: [Comprehensive API Design](./comprehensive-api-design.md) for endpoint specifications
2. **Database**: Review [Comprehensive Database Schema](./comprehensive-db-schema.md) for data model and relationships
3. **Authentication**: Review [Comprehensive Authentication Documentation](./comprehensive_authentication_doc.md) for security implementation
4. **Testing**: Use [Comprehensive Requirements Response](./comprehensive-requirements-response.md) for performance targets and sample data
5. **Mock API Testing**: Use [Mock API Testing](./MOCK_API_TESTING_GUIDE.md)** - Complete guide with all endpoints, examples, and troubleshooting

### For Integration Partners
1. **API Reference**: [Comprehensive API OpenAPI Specification](./comprehensive-api-openapi.yaml) for complete API documentation
2. **Authentication**: [Comprehensive Authentication Documentation](./comprehensive_authentication_doc.md) for JWT token structure
3. **Performance**: [Comprehensive Requirements Response](./comprehensive-requirements-response.md) for SLA targets

### For Stakeholders
1. **Business Value**: [Comprehensive API Design](./comprehensive-api-design.md) for business outcomes mapping
2. **Status**: [Comprehensive Requirements Response](./comprehensive-requirements-response.md) for completion status

## 📋 Documentation Status

| **Document** | **Status** | **Completion** | **Last Updated** |
|--------------|------------|----------------|------------------|
| [API Design](./comprehensive-api-design.md) | ✅ Complete | 100% | Oct 15, 2025 |
| [OpenAPI Spec](./comprehensive-api-openapi.yaml) | ✅ Complete | 100% | Oct 15, 2025 |
| [Authentication](./comprehensive_authentication_doc.md) | ✅ Complete | 100% | Oct 15, 2025 |
| [Requirements Response](./comprehensive-requirements-response.md) | ✅ Complete | 98% | Oct 15, 2025 |
| [Database Schema](./comprehensive-db-schema.md) | ✅ Complete | 100% | Oct 15, 2025 |



---

**Documentation Status**: 99% Complete  
**Ready for Development**: ✅ Yes  
**Last Updated**: October 15, 2025
