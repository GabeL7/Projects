# Financial Document Analysis & Reporting Platform

A full-stack web application designed to manage financial documents, extract structured financial information, analyze company performance, and generate interactive dashboards and reports.

**Project Status:** In Development — Frontend Setup

## Overview

This independent portfolio project demonstrates full-stack software engineering using Angular, TypeScript, C#, ASP.NET Core, Entity Framework Core, and Microsoft SQL Server.

The application is being developed incrementally, beginning with the frontend, backend, and database architecture before introducing financial document processing, data analysis, authentication, and reporting.

The project is built independently using original source code and synthetic or publicly available financial data.

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
| Frontend | Angular, TypeScript, HTML, CSS |
| UI | PrimeNG, RxJS |
| Backend | C#, ASP.NET Core Web API |
| Database | Microsoft SQL Server |
| Data Access | Entity Framework Core, LINQ, SQL |
| API | REST / JSON |
| Security | JWT authentication, role-based authorization |
| Testing | .NET and Angular tests |
| Version Control | Git, GitHub |
| Development Tools | Visual Studio, VS Code, SSMS |
| Deployment | Planned for a later phase |

## Project Roadmap

- Set up development environment — Completed
- Create GitHub repository and project structure — Completed
- Initialize Angular frontend — In Progress
- Integrate PrimeNG components
- Create ASP.NET Core REST API
- Connect Angular to the backend
- Configure SQL Server and Entity Framework Core
- Implement document management
- Implement financial data extraction
- Build financial dashboards
- Add authentication and authorization
- Implement reporting and exports
- Add automated tests
- Deploy the application

## Architecture

**Frontend:** Angular + TypeScript + PrimeNG + RxJS

**Backend:** ASP.NET Core Web API + C#

**Data Access:** Entity Framework Core + LINQ + SQL

**Database:** Microsoft SQL Server

The Angular frontend will communicate with the ASP.NET Core backend through REST APIs. The backend will handle business logic, document processing, authentication, and database operations.

## Development Progress

### Completed

- Configured the development environment and Git version control
- Organized the application within the existing GitHub Projects repository
- Created the initial project README and development documentation
- Configured Git commits using a GitHub-provided private email address

### In Progress

- Initializing the Angular frontend
- Verifying the frontend development server and browser functionality
- Preparing the frontend for PrimeNG integration

Detailed development notes are maintained in [Development Log](docs/Development%20Log.md).

## Getting Started

### Prerequisites

- Node.js and npm
- Angular CLI
- Git
- Visual Studio Code

### Run the Frontend

From the project directory:

```powershell
cd frontend
npm install
npm start
```

Once the development server starts successfully, open:

`http://localhost:4200`

Backend and database setup instructions will be added during their respective development milestones.

## Screenshots and Demo

Application screenshots and a live demonstration will be added once functional features are implemented.

## Project Purpose

To demonstrate the design, development, testing, and eventual deployment of an enterprise-style full-stack application using modern software engineering practices.

This project is independently developed using original implementations and synthetic or publicly available financial data.