# LPS API Documentation

## Overview

The LPS (Layered Publishing System) API provides a comprehensive REST interface for managing content through multiple layers of processing, approval, and distribution.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-token>
```

### Getting a Token

```bash
curl -X POST "http://localhost:8000/api/v1/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=demo&password=demo"
```

## Core Concepts

### Layers

LPS organizes content processing through distinct layers:

1. **Content Layer** - Raw content creation and management
2. **Processing Layer** - Content transformation and enrichment  
3. **Approval Layer** - Review workflows and quality control
4. **Distribution Layer** - Multi-channel publishing and delivery
5. **Analytics Layer** - Performance monitoring and insights

### Workflows

Workflows define the path content takes through the layers:

- `draft_review_publish` - Standard three-stage workflow
- `simple_publish` - Direct publishing without review
- `multi_approval` - Multiple approval stages

### Publications

Published content distributed through various channels:

- Website
- Social Media
- Email Newsletter
- RSS Feed

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/token` | Login and get token |
| POST | `/auth/refresh` | Refresh access token |
| POST | `/auth/logout` | Logout user |
| GET | `/auth/me` | Get current user |

### Content Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/content/` | List content items |
| POST | `/content/` | Create new content |
| GET | `/content/{id}` | Get content by ID |
| PUT | `/content/{id}` | Update content |
| DELETE | `/content/{id}` | Delete content |
| GET | `/content/{id}/versions` | Get content versions |
| POST | `/content/{id}/versions` | Create content version |
| POST | `/content/{id}/publish` | Publish content |

### Layer Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/layers/` | List all layers |
| POST | `/layers/` | Create new layer |
| GET | `/layers/{id}` | Get layer details |
| PUT | `/layers/{id}` | Update layer |
| DELETE | `/layers/{id}` | Delete layer |
| GET | `/layers/{id}/content` | Get layer content |
| POST | `/layers/{id}/process` | Process layer content |

### Workflow Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workflows/` | List workflows |
| POST | `/workflows/` | Create workflow |
| GET | `/workflows/{id}` | Get workflow |
| PUT | `/workflows/{id}` | Update workflow |
| DELETE | `/workflows/{id}` | Delete workflow |
| GET | `/workflows/{id}/instances` | Get workflow instances |
| POST | `/workflows/{id}/instances` | Create workflow instance |
| GET | `/workflows/instances/{id}` | Get instance details |
| PUT | `/workflows/instances/{id}/advance` | Advance workflow |

### Publications

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/publications/` | List publications |
| GET | `/publications/{id}` | Get publication |
| PUT | `/publications/{id}` | Update publication |
| DELETE | `/publications/{id}` | Unpublish content |
| GET | `/publications/{id}/analytics` | Get publication analytics |
| GET | `/publications/channels` | List distribution channels |
| POST | `/publications/channels` | Create distribution channel |
| GET | `/publications/channels/{id}` | Get channel details |
| GET | `/publications/analytics/overview` | Get analytics overview |

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/` | List users |
| GET | `/users/{id}` | Get user |
| PUT | `/users/{id}` | Update user |
| DELETE | `/users/{id}` | Delete user |
| GET | `/users/{id}/permissions` | Get user permissions |
| PUT | `/users/{id}/permissions` | Update permissions |
| GET | `/users/{id}/content` | Get user content |

## Response Format

All API responses follow a consistent format:

```json
{
  "status": "success|error|not_implemented",
  "message": "Description of the response",
  "data": {
    // Response data
  },
  "meta": {
    // Metadata (pagination, etc.)
  }
}
```

## Error Handling

Standard HTTP status codes are used:

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

## Rate Limiting

API requests are rate limited to 100 requests per minute per IP address.

## Pagination

List endpoints support pagination:

```
GET /api/v1/content/?skip=0&limit=20
```

## Interactive Documentation

Visit `/docs` for interactive Swagger documentation or `/redoc` for ReDoc documentation.

## SDKs and Examples

Coming soon:
- Python SDK
- JavaScript SDK
- Example applications