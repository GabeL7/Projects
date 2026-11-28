
# Financial Document Analysis Platform — Frontend

The Angular frontend for the Financial Document Analysis & Reporting Platform.

**Status:** Frontend Initialization and Backend Integration Completed

## Overview

The frontend is built with Angular 22, TypeScript, RxJS, and PrimeNG.

It provides the foundation for financial document management, interactive dashboards, data visualization, and reporting.

The initial frontend interface is operational and communicates with the ASP.NET Core backend through Angular's HttpClient.

Database integration has been completed on the backend. The frontend will use database-backed financial document endpoints in upcoming milestones.

## Technology Stack

| Category | Technology |
|---|---|
| Framework | Angular 22 |
| Language | TypeScript |
| Markup and Styling | HTML, CSS |
| UI Components | PrimeNG |
| Theme | Aura |
| Icons | PrimeIcons |
| Routing | Angular Router |
| HTTP Communication | Angular HttpClient |
| Reactive Programming | RxJS, Angular Signals |
| Testing | Angular/Vitest Setup |
| Package Management | npm |
| Version Control | Git, GitHub |

## Implemented Features

- Angular standalone application
- Angular routing configuration
- CSS styling
- PrimeNG component integration
- Aura theme configuration
- Initial dashboard layout
- Interactive PrimeNG button
- Angular HttpClient configuration
- Reusable HealthService
- Typed HealthResponse interface
- Backend connection test
- HTTP GET request to the ASP.NET Core API
- Backend response displayed using Angular signals
- Connection-error status message
- Successful frontend build and browser testing

## Project Structure

```text
frontend/
├── src/
│   └── app/
│       ├── services/
│       │   └── health.service.ts
│       ├── app.config.ts
│       ├── app.ts
│       ├── app.html
│       ├── app.css
│       └── app.routes.ts
├── angular.json
├── package.json
├── package-lock.json
└── README.md
```

Additional folders for components, pages, models, and services will be added as frontend functionality expands.

## Getting Started

### Prerequisites

- Node.js compatible with Angular 22
- npm
- Angular CLI 22
- Visual Studio Code

### Install Dependencies

From the frontend directory:

```powershell
npm install
```

### Start the Development Server

```powershell
npm start
```

Open:

```text
http://localhost:4200
```

### Build the Application

```powershell
npm run build
```

### Run Unit Tests

```powershell
npm test
```

Automated tests will be expanded as additional application features are implemented.

## PrimeNG Configuration

PrimeNG provides reusable components and styling.

The initial configuration includes:

- PrimeNG provider registration in app.config.ts
- Aura theme
- ButtonModule
- Interactive application controls

Planned PrimeNG components include data tables, cards, charts, dialogs, forms, and navigation menus.

## Backend Integration

Angular uses HttpClient to communicate with the ASP.NET Core Web API.

### Configuration

HttpClient is registered using:

```typescript
provideHttpClient()
```

The API communication service is located at:

```text
src/app/services/health.service.ts
```

The current health-check endpoint is:

```text
GET https://localhost:7174/api/health
```

The backend URL may vary depending on the local development configuration.

### Connection Flow

1. The user clicks Test Backend Connection.
2. The Angular component calls HealthService.
3. HealthService sends an HTTP GET request.
4. ASP.NET Core processes the request.
5. The backend returns JSON.
6. Angular displays the response.

Expected message:

```text
Connected: Backend API is running.
```

## Database Integration

The ASP.NET Core backend now uses SQL Server and Entity Framework Core.

The backend includes database-backed endpoints for retrieving and creating financial document metadata.

The Angular frontend has not yet implemented the financial document management interface. That integration is planned for Milestone 8.

## Planned Features

- Reusable navigation and layout components
- Financial document upload interface
- Document list and management page
- Financial data tables
- Search, sorting, and filtering
- Financial dashboard KPI cards
- Charts and interactive visualizations
- Reporting-period and company comparisons
- Form validation and notifications
- User authentication
- Role-based navigation
- Additional HTTP services for financial documents and reports
- Automated component and service tests

## Development Progress

- **Angular initialization:** Completed
- **PrimeNG integration:** Completed
- **Backend HTTP integration:** Completed
- **Backend database integration:** Completed
- **Frontend document management:** Next
- **Financial dashboards and reporting:** Planned

## Documentation

- [Main Project README](../README.md)
- [Backend README](../backend/README.md)
- [Development Log](../docs/Development%20Log.md)
