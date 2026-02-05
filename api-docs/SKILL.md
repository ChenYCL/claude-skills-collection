---
name: api-docs
description: >
  Generate comprehensive API documentation from code, OpenAPI specs, or descriptions.
  Use when: (1) documenting REST APIs, GraphQL schemas, or RPC endpoints,
  (2) generating OpenAPI/Swagger specs, (3) creating SDK documentation,
  (4) writing API reference guides for developers.
  Triggers: "document this API", "generate OpenAPI", "API docs", "swagger spec",
  "document endpoints", "write API reference", "SDK documentation".
---

# API Documentation Generator

Generate professional API documentation following industry standards like OpenAPI, with clear examples and consistent formatting.

## Documentation Components

### 1. Endpoint Documentation

```markdown
## Create User

Creates a new user account.

**Endpoint:** `POST /api/v1/users`

**Authentication:** Bearer token required

### Request

**Headers:**
| Header | Type | Required | Description |
|--------|------|----------|-------------|
| Authorization | string | Yes | Bearer {token} |
| Content-Type | string | Yes | application/json |

**Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "role": "member"
}
```

**Parameters:**
| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| email | string | Yes | User email | Valid email format |
| name | string | Yes | Display name | 1-100 chars |
| role | string | No | User role | `admin`, `member`, `guest` |

### Response

**Success (201 Created):**
```json
{
  "id": "usr_abc123",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "member",
  "createdAt": "2024-01-15T10:30:00Z"
}
```

**Errors:**
| Code | Description |
|------|-------------|
| 400 | Invalid request body |
| 401 | Unauthorized |
| 409 | Email already exists |
| 422 | Validation failed |
```

### 2. OpenAPI 3.0 Specification

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0
  description: User management API

paths:
  /users:
    post:
      summary: Create user
      operationId: createUser
      tags: [Users]
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          example: usr_abc123
        email:
          type: string
          format: email
        name:
          type: string
        role:
          type: string
          enum: [admin, member, guest]
        createdAt:
          type: string
          format: date-time
```

## Documentation Workflow

### From Code Analysis

1. **Identify endpoints** - Routes, handlers, controllers
2. **Extract parameters** - Path, query, body, headers
3. **Determine types** - Request/response schemas
4. **Find constraints** - Validation rules, enums
5. **Check authentication** - Auth requirements per endpoint
6. **Document errors** - Error codes and messages

### From Existing API

1. **Make sample requests** - Capture real responses
2. **Test edge cases** - Error scenarios
3. **Document rate limits** - If applicable
4. **Note pagination** - Cursor vs offset patterns
5. **Version information** - API versioning strategy

## Best Practices

### Clarity
- Use consistent terminology
- Provide realistic examples (not `"string"` or `"test"`)
- Explain non-obvious fields
- Document default values

### Completeness
- All endpoints documented
- All parameters described
- All error codes listed
- Authentication explained

### Maintainability
- Keep docs close to code
- Use references to avoid duplication
- Version documentation with API
- Include changelog

## Common Patterns

### Pagination
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "perPage": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

### Error Response
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {"field": "email", "message": "Must be valid email"}
    ]
  }
}
```

### Rate Limiting Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640995200
```

## Output Formats

- **Markdown** - For GitHub/GitLab wikis
- **OpenAPI YAML/JSON** - For Swagger UI, Redoc
- **Postman Collection** - For API testing
- **SDK Code Comments** - JSDoc, docstrings

## References

See [references/openapi_guide.md](references/openapi_guide.md) for complete OpenAPI specification guide.
