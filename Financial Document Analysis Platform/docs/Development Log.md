# Development Log

This document tracks the development milestones, completed tasks, testing results, technical decisions, and future work for the Financial Document Analysis & Reporting Platform.

---

## Milestone 1 — Development Environment

**Status: Completed**

### Tasks

- Installed and configured development tools
- Installed Git and connected the local project to GitHub
- Configured Git username and GitHub-provided private email address
- Installed Node.js and npm
- Prepared Visual Studio and Visual Studio Code for development
- Established the project's technology stack and development roadmap

### Result

The development environment is configured for Angular frontend and ASP.NET Core backend development.

SQL Server connectivity will be verified during the database milestone.

---

## Milestone 2 — Repository Setup

**Status: Completed**

### Tasks

- Organized the Financial Document Analysis Platform inside the existing Projects repository
- Cloned the GitHub repository to the local computer
- Created the main project README
- Created the project-specific `.gitignore`
- Created the `docs` directory and Development Log
- Successfully committed and pushed the initial documentation

### Result

The project is maintained in GitHub with documentation and a development roadmap.

---

## Milestone 3 — Angular Frontend Initialization

**Status: Completed**

### Tasks

- Installed Angular CLI 22
- Generated the Angular application inside `frontend/`
- Enabled Angular routing
- Selected CSS styling
- Disabled server-side rendering for the initial setup
- Used the existing Git repository instead of creating a nested repository
- Configured the frontend for local development

### Angular Setup Command

```powershell
ng new financial-platform --directory frontend --routing --style=css --ssr=false --skip-git
```

### Testing Results

- Angular application generated successfully
- Application launched at `http://localhost:4200`
- Development server operated successfully
- Angular application built successfully

### Result

A functioning Angular 22 frontend application was created and committed to GitHub.

---

## Milestone 4 — PrimeNG Integration and Initial Interface

**Status: Completed**

### Tasks

- Installed PrimeNG and related dependencies
- Configured the Aura theme
- Registered PrimeNG in `app.config.ts`
- Preserved the existing Angular application providers
- Imported PrimeNG's ButtonModule
- Replaced the default Angular welcome page
- Created a custom financial platform interface
- Added basic layout styling
- Implemented an interactive PrimeNG button
- Tested the frontend application
- Successfully built the Angular project

### Installation Command

```powershell
npm install primeng@22 @primeuix/themes primeicons
```

### Testing Results

- PrimeNG components render in the Angular application
- Aura theme is configured
- Custom application page displays in the browser
- PrimeNG button renders successfully
- Button interaction updates the displayed status message
- Angular application builds without errors

### Result

The Angular frontend contains a functional initial interface with PrimeNG integration.

The implementation and documentation were committed to GitHub.

---

## Milestone 5 — ASP.NET Core Web API

**Status: Completed Locally**

### Objective

Create a C# ASP.NET Core backend, configure the development environment, implement an initial REST API endpoint, and verify that the application runs successfully.

### Tasks

- Created the ASP.NET Core Web API project in Visual Studio
- Selected .NET 10 (Long Term Support)
- Selected controller-based API architecture
- Configured HTTPS for local development
- Enabled OpenAPI support
- Disabled container support because Docker was not required for the initial implementation
- Used no authentication during initial setup
- Configured and trusted the local ASP.NET Core development certificate
- Built and launched the API successfully
- Created `HealthController.cs`
- Implemented an HTTP GET health-check endpoint
- Verified the API returns a successful JSON response

### Development Environment

- Language: C#
- Framework: ASP.NET Core Web API
- Target Framework: .NET 10
- IDE: Visual Studio
- Project: `FinancialPlatform.Api`

### Backend Location

```text
backend/FinancialPlatform.Api/
```

### API Endpoint

**Method:** GET

**Route:** `/api/health`

**Local HTTPS URL:**

```text
https://localhost:7174/api/health
```

### Expected Response

```json
{
  "status": "ok",
  "application": "Financial Document Analysis Platform",
  "message": "Backend API is running."
}
```

### Testing Results

- Visual Studio solution built successfully
- Application launched successfully using F5
- Backend started in the Development environment
- HTTPS server listened on `https://localhost:7174`
- HTTP server listened on `http://localhost:5255`
- Health-check controller responded successfully
- JSON response was verified in the browser

### Result

A working ASP.NET Core Web API backend has been established using .NET 10.

The application now has independently functioning frontend and backend projects.

### GitHub

Backend code and Milestone 5 documentation are ready to be committed and pushed.

---

## Milestone 6 — Frontend and Backend Integration

**Status: Not Started**

### Objective

Connect the Angular frontend to the ASP.NET Core backend through HTTP requests.

### Planned Tasks

- Configure backend CORS for the Angular development server
- Configure Angular HTTP client support
- Create an Angular service for backend communication
- Send an HTTP GET request to `/api/health`
- Display the backend response in the frontend
- Test the connection while both applications are running
- Handle connection errors
- Build both applications
- Update documentation and push changes to GitHub

---

## Milestone 7 — Database Integration

**Status: Not Started**

### Planned Tasks

- Configure Microsoft SQL Server
- Install Entity Framework Core packages
- Configure database connectivity
- Create initial data models
- Create and apply migrations
- Test database operations

---

## Upcoming Milestones

### Milestone 8 — Document Management

Implement document management, searching, filtering, and related CRUD functionality.

### Milestone 9 — Financial Data Processing

Implement financial data extraction, validation, and storage.

### Milestone 10 — Financial Dashboards

Create interactive charts, financial KPIs, and reporting tables.

### Milestone 11 — Authentication and Authorization

Implement user authentication and role-based permissions.

### Milestone 12 — Reporting and Exports

Implement SQL reporting and PDF, Excel, and JSON exports.

### Milestone 13 — Advanced Document Extraction

Support additional PDF extraction and validation workflows.

### Milestone 14 — Testing, Polish, and Deployment

Expand testing, improve usability, configure CI/CD, and deploy the application.

---

## Development Practices

- Develop and test features incrementally
- Verify functionality before completing milestones
- Use Git commits to track meaningful changes
- Update project README files after completed milestones
- Record progress and testing results in this Development Log
- Avoid committing credentials, secrets, or generated dependencies
- Use original source code and synthetic or publicly available financial data
- Maintain professional documentation suitable for a software engineering portfolio