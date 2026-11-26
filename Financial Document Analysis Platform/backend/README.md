
# Financial Document Analysis Platform — Backend

The ASP.NET Core Web API backend for the Financial Document Analysis & Reporting Platform.

**Status:** Initial API and Angular Integration Completed

## Overview

The backend is built with C# and ASP.NET Core Web API on .NET 10. It currently exposes a health-check endpoint that the Angular frontend calls through an HTTP service.

Future development will add document management, financial processing, database access, authentication, and reporting endpoints.

## Technology Stack

| Category | Technology |
|---|---|
| Language | C# |
| Framework | ASP.NET Core Web API |
| Target Framework | .NET 10 (LTS) |
| API Architecture | Controller-based REST API |
| Response Format | JSON |
| Local Transport | HTTP and HTTPS |
| Development IDE | Visual Studio |
| API Description | OpenAPI support |
| Database (Planned) | Microsoft SQL Server |
| Data Access (Planned) | Entity Framework Core |
| Security (Planned) | JWT authentication, role-based authorization |

## Implemented Features

- ASP.NET Core Web API project setup
- Controller-based routing
- Local HTTPS development configuration
- OpenAPI support
- `HealthController` with a working HTTP GET endpoint
- JSON response with backend status and application information
- CORS policy allowing the Angular development origin
- Successful API build, startup, and browser verification
- Successful cross-origin request from the Angular frontend

## Project Structure

```text
backend/
├── FinancialPlatform.Api/
│   ├── Controllers/
│   │   └── HealthController.cs
│   ├── Properties/
│   │   └── launchSettings.json
│   ├── Program.cs
│   ├── appsettings.json
│   ├── appsettings.Development.json
│   ├── FinancialPlatform.Api.csproj
│   ├── FinancialPlatform.Api.slnx
│   └── FinancialPlatform.Api.http
└── README.md
```

## Getting Started

### Prerequisites

- .NET 10 SDK
- Visual Studio 2026 with the ASP.NET and web development workload

### Build and Run

1. Open `FinancialPlatform.Api/FinancialPlatform.Api.slnx` in Visual Studio.
2. Build the solution with `Ctrl + Shift + B`.
3. Press `F5` to run the API.
4. Use the configured local HTTPS address to test the endpoint.

Example local addresses from the current development setup:

```text
https://localhost:7174
http://localhost:5255
```

Ports may vary with the local launch configuration.

## Available Endpoint

### Health Check

| Property | Value |
|---|---|
| Method | GET |
| Route | `/api/health` |
| Success Response | HTTP 200 |
| Content Type | JSON |

Example request:

```text
https://localhost:7174/api/health
```

Example response:

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

## Angular Integration and CORS

The Angular development server runs at `http://localhost:4200`, while the backend uses its own local HTTPS address. These addresses are different browser origins, so the backend has a CORS policy configured in `Program.cs`.

The current development policy permits requests from:

```text
http://localhost:4200
```

It allows HTTP methods and headers needed for the initial frontend API calls. The policy is registered and applied to controller routes through the ASP.NET Core middleware pipeline.

The frontend uses `HealthService` to call `/api/health` and display the response. The end-to-end request has been tested successfully in the browser.

## Planned Features

- Financial document CRUD endpoints
- Financial data extraction and processing services
- SQL Server database configuration
- Entity Framework Core models, migrations, and queries
- Financial calculation and reporting services
- Authentication and role-based authorization
- Request validation and consistent error responses
- Automated unit and integration tests
- Deployment configuration

## Development Progress

- **Web API setup and health endpoint:** Completed
- **Angular integration and development CORS configuration:** Completed Locally
- **SQL Server and Entity Framework Core:** Next

See the [main project README](../README.md) and [Development Log](../docs/Development%20Log.md) for project-wide progress.
