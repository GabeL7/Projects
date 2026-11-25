# Financial Document Analysis & Reporting Platform

A full-stack web application designed to manage financial documents, extract structured financial information, analyze company performance, and generate interactive dashboards and reports.

**Project Status:** In Development — Frontend Initialized

## Overview

This independent portfolio project demonstrates full-stack software engineering using Angular, TypeScript, PrimeNG, C#, ASP.NET Core, Entity Framework Core, and Microsoft SQL Server.

The application is being developed incrementally, beginning with the frontend, backend, and database architecture before introducing financial document processing, data analysis, authentication, and reporting.

The Angular frontend has been initialized, PrimeNG has been integrated with the Aura theme, and an initial interactive interface has been implemented and tested locally.

## Planned Features

- Financial document upload and management
- Financial data extraction from CSV, Excel, JSON, and PDF files
- Revenue, expense, profit, and financial ratio analysis
- Interactive financial dashboards
- Company and reporting-period comparisons
- User authentication and role-based authorization
- SQL-based financial reporting
- PDF, Excel, and JSON exports
- Validation and manual review of unrecognized financial data

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular 22, TypeScript, HTML, CSS |
| UI | PrimeNG, PrimeIcons, Aura Theme |
| Reactive Programming | RxJS |
| Backend | C#, ASP.NET Core Web API |
| Database | Microsoft SQL Server |
| Data Access | Entity Framework Core, LINQ, SQL |
| API | REST / JSON |
| Security | JWT authentication, role-based authorization |
| Testing | Angular/Vitest, .NET tests |
| Version Control | Git, GitHub |
| Development Tools | Visual Studio, VS Code, SSMS |
| Deployment | Planned for a later phase |

Backend, database, security, and reporting technologies are planned for future milestones.

## Project Roadmap

- Set up development environment — Completed
- Create GitHub repository and project structure — Completed
- Initialize Angular frontend — Completed
- Integrate PrimeNG components — Completed
- Create ASP.NET Core REST API — Not Started
- Connect Angular to the backend — Not Started
- Configure SQL Server and Entity Framework Core — Not Started
- Implement document management
- Implement financial data extraction
- Build financial dashboards
- Add authentication and authorization
- Implement reporting and exports
- Add automated tests
- Deploy the application

## Architecture

**Frontend:** Angular + TypeScript + PrimeNG + RxJS

**Backend (Planned):** ASP.NET Core Web API + C#

**Data Access (Planned):** Entity Framework Core + LINQ + SQL

**Database (Planned):** Microsoft SQL Server

The Angular frontend will communicate with the ASP.NET Core backend through REST APIs. The backend will manage business logic, financial document processing, authentication, and database operations.

## Development Progress

### Completed

- Configured Git and the initial development environment
- Established the project structure inside the existing GitHub Projects repository
- Created project documentation and Git ignore rules
- Generated the Angular 22 frontend application
- Configured Angular routing and CSS styling
- Integrated PrimeNG with the Aura theme
- Created an initial frontend interface
- Added an interactive PrimeNG button
- Verified the frontend runs locally
- Successfully built the Angular application

### Next Milestone

Create the ASP.NET Core Web API backend and implement an initial endpoint.

Detailed progress is recorded in [Development Log](docs/Development%20Log.md).

## Getting Started

### Prerequisites

- Node.js compatible with Angular 22
- npm
- Angular CLI
- Git

### Run the Frontend

Navigate to the `frontend` directory:

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

Open `http://localhost:4200/` in your browser.

### Build the Frontend

```powershell
npm run build
```

Backend and database instructions will be added when those components are implemented.

## Screenshots and Demo

The initial frontend interface is operational locally.

Screenshots of the financial dashboard and a live demonstration will be added as the application develops.

## Project Purpose

To demonstrate the design, development, testing, and eventual deployment of an enterprise-style full-stack application using modern software engineering practices.

This project is independently developed using original source code and synthetic or publicly available financial data.