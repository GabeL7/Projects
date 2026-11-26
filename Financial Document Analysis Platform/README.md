# Financial Document Analysis & Reporting Platform

A full-stack web application for managing financial documents, analyzing financial data, visualizing company performance, and generating financial reports.

**Project Status:** In Development — Frontend and Backend Initialized

## Overview

The Financial Document Analysis & Reporting Platform is a full-stack application built with Angular, TypeScript, PrimeNG, C#, ASP.NET Core, and Microsoft SQL Server.

The platform is designed to streamline financial document management and analysis through structured data extraction, interactive dashboards, financial calculations, and automated reporting.

Development follows an incremental approach, beginning with frontend and backend infrastructure before implementing database integration, document processing, financial analytics, and reporting features.

## Features

### Implemented

- Angular 22 frontend application
- PrimeNG component library with Aura theme
- Initial responsive application layout
- Interactive frontend components
- ASP.NET Core Web API using .NET 10
- Controller-based REST API architecture
- HTTPS development configuration
- Functional API health-check endpoint
- JSON API responses
- Local frontend and backend development environments

### Planned

- Financial document upload and management
- CSV, Excel, JSON, and PDF document processing
- Financial data extraction and validation
- Revenue, expense, and profitability analysis
- Financial ratios and performance indicators
- Interactive financial dashboards and charts
- Company and reporting-period comparisons
- User authentication and role-based authorization
- SQL Server database integration
- PDF, Excel, and JSON report exports
- Automated testing and deployment

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular 22, TypeScript, HTML, CSS |
| UI Components | PrimeNG, PrimeIcons, Aura Theme |
| Reactive Programming | RxJS |
| Backend | C#, ASP.NET Core Web API, .NET 10 |
| API Communication | REST, HTTP, JSON |
| Database | Microsoft SQL Server (Planned) |
| Data Access | Entity Framework Core, LINQ, SQL (Planned) |
| Security | JWT Authentication, Role-Based Authorization (Planned) |
| Testing | Vitest, .NET Testing Frameworks |
| Development Tools | Visual Studio, VS Code, SSMS |
| Version Control | Git, GitHub |

## Application Architecture

The application follows a frontend-backend architecture with a separate database layer.

```text
Angular Frontend
    |
    | HTTP / REST API
    |
ASP.NET Core Web API
    |
    | Entity Framework Core
    |
Microsoft SQL Server
```

### Frontend

The Angular application provides the interface for financial document management, data visualization, reporting, and user interaction.

PrimeNG provides reusable UI components and consistent styling.

### Backend

The ASP.NET Core Web API handles incoming HTTP requests and will manage business logic, financial processing, document operations, and reporting.

The backend currently includes a functional health-check endpoint.

### Database

Microsoft SQL Server and Entity Framework Core will be integrated to store financial documents, extracted financial information, application users, and reporting data.

Database connectivity and persistence will be implemented in a future milestone.

## Project Structure

```text
Financial Document Analysis Platform/
├── frontend/
│   ├── public/
│   ├── src/
│   │   └── app/
│   ├── angular.json
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── backend/
│   ├── FinancialPlatform.Api/
│   │   ├── Controllers/
│   │   │   └── HealthController.cs
│   │   ├── Properties/
│   │   │   └── launchSettings.json
│   │   ├── Program.cs
│   │   ├── appsettings.json
│   │   └── FinancialPlatform.Api.csproj
│   └── README.md
│
├── docs/
│   └── Development Log.md
│
├── .gitignore
└── README.md
```

Additional directories and components will be introduced as development progresses.

## Getting Started

### Prerequisites

Frontend:

- Node.js compatible with Angular 22
- npm
- Angular CLI

Backend:

- .NET 10 SDK
- Visual Studio 2026
- ASP.NET and web development workload

### Running the Frontend

From the main project directory, navigate to the Angular application:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm start
```

Open:

```text
http://localhost:4200
```

### Building the Frontend

```powershell
npm run build
```

### Running the Backend

1. Open the `FinancialPlatform.Api` solution in Visual Studio.
2. Build the solution using `Ctrl + Shift + B`.
3. Press `F5` to launch the backend.
4. Open the health-check endpoint in a browser.

Example local endpoint:

```text
https://localhost:7174/api/health
```

Port numbers may vary depending on the local development configuration.

## API Endpoints

### Health Check

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Verifies that the backend API is running |

**Example Response:**

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

Additional REST API endpoints will be implemented for financial documents, data analysis, reporting, and user management.

## Development Roadmap

- **Milestone 1 — Development Environment:** Completed
- **Milestone 2 — Repository Setup:** Completed
- **Milestone 3 — Angular Frontend Initialization:** Completed
- **Milestone 4 — PrimeNG Integration:** Completed
- **Milestone 5 — ASP.NET Core Web API:** Completed Locally
- **Milestone 6 — Frontend and Backend Integration:** Next
- **Milestone 7 — SQL Server and Entity Framework Core:** Not Started
- **Milestone 8 — Document Management:** Not Started
- **Milestone 9 — Financial Data Processing:** Not Started
- **Milestone 10 — Financial Dashboards:** Not Started
- **Milestone 11 — Authentication and Authorization:** Not Started
- **Milestone 12 — Reporting and Exports:** Not Started
- **Milestone 13 — Advanced Document Extraction:** Not Started
- **Milestone 14 — Testing, Polish, and Deployment:** Not Started

## Current Development Progress

### Frontend

- Angular application created and configured
- Angular routing enabled
- PrimeNG installed and configured
- Aura theme integrated
- Initial dashboard interface created
- PrimeNG button interaction tested
- Development server and production build verified

### Backend

- ASP.NET Core Web API created using .NET 10
- Controller-based API architecture configured
- HTTPS development environment established
- OpenAPI support enabled
- Health-check controller implemented
- Backend successfully built and launched in Visual Studio
- API endpoint tested and verified in the browser

### Next Steps

Connect the Angular frontend to the ASP.NET Core backend using Angular's HTTP client, configure CORS, and display data retrieved from the API.

## Documentation

- [Frontend Documentation](frontend/README.md)
- [Backend Documentation](backend/README.md)
- [Development Log](docs/Development%20Log.md)

The Development Log contains milestone details, completed tasks, testing results, and upcoming work.

## Screenshots and Demo

Screenshots of the financial dashboard and a live application demonstration will be added as development progresses.

## Project Purpose

This project demonstrates full-stack software engineering through the design, development, testing, and deployment of a financial document analysis and reporting application.