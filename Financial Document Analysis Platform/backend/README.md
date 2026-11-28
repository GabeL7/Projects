
# Financial Document Analysis Platform — Backend

The C# ASP.NET Core Web API backend for the Financial Document Analysis & Reporting Platform.

**Status:** API and Database Integration Completed

## Overview

The backend is built using C#, ASP.NET Core Web API, .NET 10, Entity Framework Core, and Microsoft SQL Server.

It provides REST API endpoints for application status and financial document metadata management.

The backend uses Entity Framework Core to communicate with SQL Server, allowing document records to be created and retrieved through HTTP requests.

## Technology Stack

| Category | Technology |
|---|---|
| Language | C# |
| Framework | ASP.NET Core Web API |
| Target Framework | .NET 10 (LTS) |
| API Architecture | Controller-Based REST API |
| ORM | Entity Framework Core 10 |
| Database | Microsoft SQL Server Express |
| Data Access | LINQ, EF Core, SQL |
| Database Migrations | EF Core Code-First Migrations |
| API Format | JSON |
| API Description | OpenAPI Support |
| Development IDE | Visual Studio 2026 |
| Database Tools | SQL Server Management Studio 22 |
| Security (Planned) | JWT Authentication, Role-Based Authorization |

## Implemented Features

- ASP.NET Core Web API project setup
- HTTPS development configuration
- Controller-based API routing
- OpenAPI support
- CORS configuration for Angular
- Health-check endpoint
- SQL Server database integration
- Entity Framework Core dependency injection
- FinancialDocument entity model
- ApplicationDbContext
- Initial EF Core migration
- FinancialDocuments database table
- Asynchronous database queries
- Financial document metadata creation
- Financial document metadata retrieval
- Database persistence verified through SSMS

## Project Structure

```text
backend/
├── FinancialPlatform.Api/
│   ├── Controllers/
│   │   ├── HealthController.cs
│   │   └── FinancialDocumentsController.cs
│   ├── Data/
│   │   └── ApplicationDbContext.cs
│   ├── Models/
│   │   └── FinancialDocument.cs
│   ├── Migrations/
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
- Visual Studio 2026
- ASP.NET and web development workload
- Microsoft SQL Server Express
- SQL Server Management Studio

### Build and Run

Open:

```text
FinancialPlatform.Api/FinancialPlatform.Api.slnx
```

In Visual Studio 2026:

1. Build the solution using Ctrl + Shift + B.
2. Press F5 to start the application.
3. Verify the API responds successfully.

Example local HTTPS address:

```text
https://localhost:7174
```

The local port may differ depending on the launch configuration.

## Database Configuration

The API uses Microsoft SQL Server Express.

### Database Name

```text
FinancialPlatformDb
```

### Development Configuration

The SQL Server connection is configured in:

```text
FinancialPlatform.Api/appsettings.Development.json
```

The backend uses Windows Authentication for its local SQL Server connection.

### Entity Framework Core

Entity Framework Core is configured in Program.cs and registered through ASP.NET Core dependency injection.

The application uses:

- ApplicationDbContext
- DbSet<FinancialDocument>
- UseSqlServer
- LINQ queries
- Asynchronous EF Core operations
- Code-first migrations

## Database Model

### FinancialDocument

The FinancialDocument class represents metadata associated with a financial document.

| Property | Type | Description |
|---|---|---|
| Id | int | Primary key |
| FileName | string | Document filename |
| FileSizeBytes | long | Document size in bytes |
| UploadedAtUtc | DateTime | UTC record creation timestamp |

The initial model contains document metadata. File storage and content extraction will be added in later milestones.

## Database Migrations

The initial migration is named:

```text
InitialCreate
```

It was generated using Entity Framework Core 10.

### Create a Migration

In Visual Studio 2026, open:

Tools → NuGet Package Manager → Package Manager Console

Select FinancialPlatform.Api as the default project.

Run:

```powershell
Add-Migration MigrationName
```

Replace MigrationName with a descriptive migration name.

### Apply Migrations

```powershell
Update-Database
```

The initial migration creates:

- FinancialPlatformDb database
- FinancialDocuments table
- __EFMigrationsHistory table

Database migrations are included in version control to track schema changes.

## API Endpoints

### Health Check

| Method | Route | Description |
|---|---|---|
| GET | `/api/health` | Check backend availability |

Example response:

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

### Financial Documents

| Method | Route | Description |
|---|---|---|
| GET | `/api/financialdocuments` | Retrieve all document records |
| GET | `/api/financialdocuments/{id}` | Retrieve a document record by ID |
| POST | `/api/financialdocuments` | Create a document metadata record |

### Example Create Request

```http
POST /api/financialdocuments
Content-Type: application/json
```

```json
{
  "fileName": "sample-financial-report.csv",
  "fileSizeBytes": 2048
}
```

The backend creates a FinancialDocument entity and saves it using Entity Framework Core.

The response includes the generated database ID and creation timestamp.

### Example Retrieval

```http
GET /api/financialdocuments
```

The endpoint retrieves stored document records from SQL Server and returns them as JSON.

## Database Testing

Database integration was verified through REST API requests and SQL Server Management Studio.

### Tests Performed

- Successfully built the ASP.NET Core backend
- Generated the InitialCreate migration
- Applied the migration to SQL Server
- Verified the FinancialDocuments table exists
- Verified the migration was recorded in __EFMigrationsHistory
- Sent an HTTP GET request to retrieve document records
- Sent an HTTP POST request to create a document metadata record
- Confirmed the record was returned by the GET endpoint
- Queried SQL Server directly to verify the saved data

### SQL Verification

```sql
USE FinancialPlatformDb;

SELECT *
FROM dbo.FinancialDocuments;

SELECT *
FROM dbo.__EFMigrationsHistory;
```

The initial database insert and retrieval tests completed successfully.

## Angular Integration

The backend allows requests from the Angular development server through its configured CORS policy.

Current frontend origin:

```text
http://localhost:4200
```

The Angular frontend currently uses the health-check endpoint to verify backend communication.

Financial document management features will be integrated into Angular in Milestone 8.

## Planned Features

- Complete document CRUD operations
- Real document uploads and file storage
- Document validation and metadata management
- CSV, Excel, JSON, and PDF parsing
- Financial data extraction
- Financial calculation services
- Additional database entities and relationships
- Authentication and role-based authorization
- Reporting and export endpoints
- Automated unit and integration tests
- Deployment configuration

## Development Progress

- **Web API initialization:** Completed
- **Angular integration and CORS:** Completed
- **SQL Server and Entity Framework Core:** Completed Locally
- **Database migrations:** Completed
- **Database insert and retrieval testing:** Completed
- **Document management:** Next

## Documentation

- [Main Project README](../README.md)
- [Frontend README](../frontend/README.md)
- [Development Log](../docs/Development%20Log.md)
