# Financial Document Analysis Platform — Backend

The ASP.NET Core Web API backend for the Financial Document Analysis & Reporting Platform.

**Status:** Initial API Setup Completed

## Overview

This backend is built using C# and ASP.NET Core Web API on .NET 10.

It will eventually manage financial documents, business logic, financial data processing, authentication, database operations, and reporting.

The initial backend setup is complete, with a working REST API endpoint that has been built and tested locally.

## Technology Stack

| Category | Technology |
|---|---|
| Language | C# |
| Framework | ASP.NET Core Web API |
| .NET Version | .NET 10 (LTS) |
| API Architecture | Controller-Based REST API |
| Data Format | JSON |
| API Documentation | OpenAPI Support |
| Development IDE | Visual Studio |
| Database | Microsoft SQL Server (Planned) |
| ORM | Entity Framework Core (Planned) |
| Authentication | JWT (Planned) |
| Authorization | Role-Based Authorization (Planned) |

## Implemented Features

- ASP.NET Core Web API project initialization
- Controller-based API architecture
- HTTPS development configuration
- OpenAPI support
- Health-check API endpoint
- JSON API responses
- Successful local build and execution

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
│   └── FinancialPlatform.Api.csproj
└── README.md
```

Visual Studio also generates supporting project and solution files.

## Getting Started

### Prerequisites

- .NET 10 SDK
- Visual Studio 2026
- ASP.NET and web development workload

### Build the Application

Open the API project or solution in Visual Studio.

Select:

**Build → Build Solution**

Or press:

`Ctrl + Shift + B`

### Run the Application

Press `F5` in Visual Studio.

The application starts using the locally configured HTTP and HTTPS addresses.

### Test the API

Open the following URL while the backend is running:

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

Port numbers may vary by development environment.

## API Endpoints

### Health Check

**Method:** GET

**Route:** `/api/health`

**Purpose:** Verifies that the backend application is operational.

**Response:** HTTP 200 with a JSON status message.

## Planned Features

- Financial document management endpoints
- CSV, Excel, JSON, and PDF processing
- Financial analysis services
- SQL Server database integration
- Entity Framework Core models and migrations
- Authentication and role-based authorization
- Report generation and exports
- Input validation and exception handling
- Automated unit and integration tests
- Application logging and deployment configuration

## Frontend Integration

The Angular frontend will communicate with the backend through HTTP requests.

Cross-origin resource sharing (CORS) and Angular HTTP services will be configured during the next development milestone.

## Development Practices

- Use controllers for HTTP request handling
- Separate business logic into services as functionality expands
- Use dependency injection for application services
- Validate incoming data
- Avoid committing credentials or connection-string secrets
- Add tests as application features are implemented
- Maintain clear documentation for API endpoints

## Project Purpose

To demonstrate backend development using C#, ASP.NET Core, REST APIs, and eventually Entity Framework Core and SQL Server in a full-stack financial analysis application.