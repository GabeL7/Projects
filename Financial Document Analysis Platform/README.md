
# Financial Document Analysis & Reporting Platform

A full-stack web application for managing financial documents, analyzing financial data, visualizing company performance, and generating financial reports.

**Project Status:** In Development — Database Integration Completed

## Overview

The Financial Document Analysis & Reporting Platform is a full-stack application built with Angular, TypeScript, PrimeNG, C#, ASP.NET Core, Entity Framework Core, and Microsoft SQL Server.

The platform is designed to support financial document management, structured data extraction, financial analysis, interactive dashboards, and automated reporting.

The application currently includes a functioning Angular frontend, an ASP.NET Core REST API, and a SQL Server database integrated through Entity Framework Core. Frontend-to-backend communication and database read/write operations have been implemented and tested.

## Implemented Features

### Frontend

- Angular 22 application with TypeScript, HTML, and CSS
- PrimeNG component library with Aura theme
- Angular routing and standalone component architecture
- Initial dashboard interface
- Interactive PrimeNG components
- Angular HttpClient integration
- Reusable HealthService for backend communication
- Backend connection testing and status messages

### Backend

- C# ASP.NET Core Web API using .NET 10
- Controller-based REST API architecture
- HTTPS development configuration
- OpenAPI support
- CORS configuration for Angular integration
- API health-check endpoint
- Financial document metadata endpoints
- Asynchronous database operations using Entity Framework Core
- JSON request and response handling

### Database

- Microsoft SQL Server Express integration
- Entity Framework Core 10
- ApplicationDbContext configuration
- FinancialDocument data model
- Code-first database migrations
- FinancialPlatformDb database
- FinancialDocuments table
- Database insert and retrieval operations
- Verified persistence using SQL Server Management Studio

## Planned Features

- Financial document uploads and file storage
- Complete document CRUD operations
- CSV, Excel, JSON, and PDF processing
- Financial data extraction and validation
- Revenue, expense, and profitability calculations
- Financial ratios and performance indicators
- Interactive dashboards, charts, and data tables
- Company and reporting-period comparisons
- User authentication and role-based authorization
- PDF, Excel, and JSON report exports
- Automated testing and deployment

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular 22, TypeScript, HTML, CSS |
| UI | PrimeNG, PrimeIcons, Aura Theme |
| Reactive Programming | RxJS, Angular Signals |
| Backend | C#, ASP.NET Core Web API, .NET 10 |
| API Communication | REST, HTTP/HTTPS, JSON, Angular HttpClient |
| Database | Microsoft SQL Server Express |
| ORM | Entity Framework Core 10 |
| Data Access | LINQ, EF Core, SQL |
| Database Migrations | EF Core Code-First Migrations |
| Security (Planned) | JWT Authentication, Role-Based Authorization |
| Testing | Manual API, Database, and Build Testing; Automated Tests Planned |
| Development Tools | Visual Studio 2026, VS Code, SSMS 22 |
| Version Control | Git, GitHub |

## Application Architecture

The application separates frontend presentation, backend API operations, and database persistence.

```text
Angular Frontend
(TypeScript + PrimeNG)
        |
        | HTTP / REST / JSON
        |
ASP.NET Core Web API
(C# + .NET 10)
        |
        | Entity Framework Core
        |
Microsoft SQL Server
(FinancialPlatformDb)
```

### Frontend

The Angular frontend provides the application interface and communicates with the ASP.NET Core backend using HTTP requests.

The frontend currently includes an initial dashboard and a working API connection test.

### Backend

The ASP.NET Core Web API handles HTTP requests, controller routing, and database operations.

The backend provides health-check and financial document metadata endpoints.

### Database

Microsoft SQL Server stores application data using an Entity Framework Core data model and DbContext.

The initial database schema was created through EF Core migrations.

## Project Structure

```text
Financial Document Analysis Platform/
├── frontend/
│   ├── src/
│   │   └── app/
│   │       ├── services/
│   │       │   └── health.service.ts
│   │       ├── app.config.ts
│   │       ├── app.ts
│   │       ├── app.html
│   │       └── app.css
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── backend/
│   ├── FinancialPlatform.Api/
│   │   ├── Controllers/
│   │   │   ├── HealthController.cs
│   │   │   └── FinancialDocumentsController.cs
│   │   ├── Data/
│   │   │   └── ApplicationDbContext.cs
│   │   ├── Models/
│   │   │   └── FinancialDocument.cs
│   │   ├── Migrations/
│   │   ├── Properties/
│   │   ├── Program.cs
│   │   ├── appsettings.json
│   │   ├── appsettings.Development.json
│   │   ├── FinancialPlatform.Api.csproj
│   │   └── FinancialPlatform.Api.slnx
│   └── README.md
│
├── docs/
│   └── Development Log.md
│
├── .gitignore
└── README.md
```

Additional generated and configuration files are omitted for readability.

## Getting Started

### Prerequisites

- Node.js and npm compatible with Angular 22
- Angular CLI 22
- .NET 10 SDK
- Visual Studio 2026 with ASP.NET and web development support
- Visual Studio Code
- Microsoft SQL Server Express
- SQL Server Management Studio

### Run the Backend

Open the following solution in Visual Studio 2026:

```text
backend/FinancialPlatform.Api/FinancialPlatform.Api.slnx
```

Build the solution using `Ctrl + Shift + B`.

Press `F5` to run the ASP.NET Core Web API.

Example local backend address:

```text
https://localhost:7174
```

Local ports may differ depending on the development configuration.

### Run the Frontend

Open the `frontend` directory in Visual Studio Code.

Install dependencies:

```powershell
npm install
```

Start the Angular development server:

```powershell
npm start
```

Open:

```text
http://localhost:4200
```

Click **Test Backend Connection** to verify the Angular application can communicate with the running API.

### Build the Frontend

```powershell
npm run build
```

### Database Configuration

The backend uses Microsoft SQL Server Express and Entity Framework Core.

The development connection is configured in:

```text
backend/FinancialPlatform.Api/appsettings.Development.json
```

The database name is:

```text
FinancialPlatformDb
```

The schema is maintained through EF Core migrations.

### Apply Database Migrations

In Visual Studio 2026, open:

**Tools → NuGet Package Manager → Package Manager Console**

Select `FinancialPlatform.Api` as the default project.

Run:

```powershell
Update-Database
```

This applies pending migrations to the configured SQL Server database.

## API Endpoints

### Health Check

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Checks backend availability |

Example response:

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

### Financial Documents

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/financialdocuments` | Retrieve all financial document records |
| GET | `/api/financialdocuments/{id}` | Retrieve a financial document by ID |
| POST | `/api/financialdocuments` | Create a financial document metadata record |

### Example POST Request

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

The API saves the document metadata to SQL Server and returns the created record.

Actual file uploads and file-content processing will be implemented in a later milestone.

## Database Design

### FinancialDocuments Table

| Column | Data Type | Description |
|---|---|---|
| Id | int | Primary key |
| FileName | nvarchar(255) | Document filename |
| FileSizeBytes | bigint | Document size in bytes |
| UploadedAtUtc | datetime2 | UTC creation timestamp |

The table is managed through Entity Framework Core.

### Entity Framework Core

The backend uses:

- ApplicationDbContext for database access
- FinancialDocument as the initial entity model
- DbSet for querying and persisting document records
- LINQ queries for data retrieval
- SaveChangesAsync for persistence
- Code-first migrations for schema management

## Development Roadmap

- **Milestone 1 — Development Environment:** Completed
- **Milestone 2 — Repository Setup:** Completed
- **Milestone 3 — Angular Frontend Initialization:** Completed
- **Milestone 4 — PrimeNG Integration:** Completed
- **Milestone 5 — ASP.NET Core Web API:** Completed
- **Milestone 6 — Frontend and Backend Integration:** Completed
- **Milestone 7 — SQL Server and Entity Framework Core:** Completed Locally
- **Milestone 8 — Document Management:** Next
- **Milestone 9 — Financial Data Processing:** Not Started
- **Milestone 10 — Financial Dashboards:** Not Started
- **Milestone 11 — Authentication and Authorization:** Not Started
- **Milestone 12 — Reporting and Exports:** Not Started
- **Milestone 13 — Advanced Document Extraction:** Not Started
- **Milestone 14 — Testing, Polish, and Deployment:** Not Started

## Development Progress

### Completed

- Angular frontend initialization and PrimeNG integration
- ASP.NET Core Web API initialization
- HTTP communication between Angular and ASP.NET Core
- SQL Server Express connection
- Entity Framework Core package installation and configuration
- FinancialDocument model and ApplicationDbContext
- Initial EF Core migration
- Database and table creation
- REST API endpoints for financial document metadata
- Successful database insert using HTTP POST
- Successful retrieval using HTTP GET
- Database persistence verification using SSMS

### Next Steps

Expand financial document management with additional CRUD operations, file uploads, validation, and backend storage functionality.

## Documentation

- [Frontend README](frontend/README.md)
- [Backend README](backend/README.md)
- [Development Log](docs/Development%20Log.md)

## Screenshots and Demo

Screenshots, example financial dashboards, and a deployed demonstration will be added as development progresses.

## Project Purpose

This project demonstrates full-stack software engineering through the design, implementation, integration, and testing of a financial document analysis and reporting application.
