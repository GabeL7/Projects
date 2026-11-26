
# Financial Document Analysis & Reporting Platform

A full-stack web application for managing financial documents, analyzing financial data, visualizing company performance, and generating financial reports.

**Project Status:** In Development — Frontend and Backend Connected

## Overview

The Financial Document Analysis & Reporting Platform is being built with Angular, TypeScript, PrimeNG, C#, and ASP.NET Core. The application is designed to support financial document management, structured data extraction, financial analysis, interactive dashboards, and reporting.

The Angular frontend and ASP.NET Core Web API are operational and communicate through HTTP requests. Database integration, document processing, financial analytics, and reporting are planned for upcoming milestones.

## Implemented Features

- Angular 22 application with routing, CSS styling, and PrimeNG components
- Aura theme and an initial dashboard interface
- Interactive PrimeNG button and application status messages
- ASP.NET Core Web API using C# and .NET 10
- Controller-based REST endpoint: `GET /api/health`
- HTTPS-enabled local backend development
- Backend CORS policy allowing requests from the Angular development server
- Angular `HttpClient` integration through a dedicated `HealthService`
- Frontend button that requests backend status and displays the JSON response
- Frontend error message when the backend connection fails
- Successful local builds and end-to-end browser verification of the health-check request

## Planned Features

- Financial document upload and management
- CSV, Excel, JSON, and PDF document processing
- Financial data extraction and validation
- Revenue, expense, profitability, and financial ratio calculations
- Interactive financial dashboards, charts, and data tables
- Company and reporting-period comparisons
- Microsoft SQL Server and Entity Framework Core integration
- User authentication and role-based authorization
- PDF, Excel, and JSON report exports
- Automated testing, CI/CD, and deployment

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular 22, TypeScript, HTML, CSS, RxJS |
| UI | PrimeNG 22, PrimeIcons, Aura Theme |
| Backend | C#, ASP.NET Core Web API, .NET 10 |
| API Communication | REST, HTTP/HTTPS, JSON, Angular `HttpClient` |
| Database (Planned) | Microsoft SQL Server |
| Data Access (Planned) | Entity Framework Core, LINQ, SQL |
| Security (Planned) | JWT authentication, role-based authorization |
| Testing | Manual browser and build verification; automated tests planned |
| Development Tools | Visual Studio, VS Code, Git, GitHub |

## Application Architecture

```text
Angular Frontend (http://localhost:4200)
        |
        | HTTP GET /api/health
        v
ASP.NET Core Web API (https://localhost:7174)
        |
        | JSON response
        v
Angular HealthService -> Dashboard status message

Planned data layer:
ASP.NET Core Web API -> Entity Framework Core -> SQL Server
```

The frontend and backend run as separate applications. Angular uses a dedicated service to request data from the API, and the backend permits the local Angular origin through its development CORS policy.

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
│   └── README.md
├── backend/
│   ├── FinancialPlatform.Api/
│   │   ├── Controllers/
│   │   │   └── HealthController.cs
│   │   ├── Program.cs
│   │   ├── FinancialPlatform.Api.csproj
│   │   └── FinancialPlatform.Api.slnx
│   └── README.md
├── docs/
│   └── Development Log.md
├── .gitignore
└── README.md
```

Additional files and folders are omitted from this overview for readability.

## Getting Started

### Prerequisites

- Node.js and npm compatible with Angular 22
- Angular CLI 22
- .NET 10 SDK
- Visual Studio 2026 with the ASP.NET and web development workload
- VS Code for frontend development

### Run the Backend

Open `backend/FinancialPlatform.Api/FinancialPlatform.Api.slnx` in Visual Studio.

1. Build the solution (`Ctrl + Shift + B`).
2. Press `F5` to start the API.
3. Verify the health-check endpoint in your browser:

```text
https://localhost:7174/api/health
```

The local port may differ depending on your Visual Studio launch settings.

### Run the Frontend

From the `frontend` directory:

```powershell
npm install
npm start
```

Open `http://localhost:4200`, then click **Test Backend Connection**. Keep the backend running while testing.

The frontend should display:

```text
Connected: Backend API is running.
```

### Build the Frontend

```powershell
npm run build
```

### API Endpoint

| Method | Route | Purpose |
|---|---|---|
| GET | `/api/health` | Returns the backend's operational status |

Example response:

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

## Development Roadmap

- **Milestone 1 — Development Environment:** Completed
- **Milestone 2 — Repository Setup:** Completed
- **Milestone 3 — Angular Frontend Initialization:** Completed
- **Milestone 4 — PrimeNG Integration:** Completed
- **Milestone 5 — ASP.NET Core Web API:** Completed
- **Milestone 6 — Frontend and Backend Integration:** Completed Locally
- **Milestone 7 — SQL Server and Entity Framework Core:** Next
- **Milestone 8 — Document Management:** Not Started
- **Milestone 9 — Financial Data Processing:** Not Started
- **Milestone 10 — Financial Dashboards:** Not Started
- **Milestone 11 — Authentication and Authorization:** Not Started
- **Milestone 12 — Reporting and Exports:** Not Started
- **Milestone 13 — Advanced Document Extraction:** Not Started
- **Milestone 14 — Testing, Polish, and Deployment:** Not Started

## Documentation

- [Frontend README](frontend/README.md)
- [Backend README](backend/README.md)
- [Development Log](docs/Development%20Log.md)

## Screenshots and Demo

Screenshots of financial analysis features and a deployed demonstration will be added as those features are implemented.

## Project Purpose

This project demonstrates full-stack software engineering through the design, implementation, integration, and testing of a financial document analysis and reporting application.
