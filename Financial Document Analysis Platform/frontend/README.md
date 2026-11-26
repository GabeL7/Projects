
# Financial Document Analysis Platform — Frontend

The Angular frontend for the Financial Document Analysis & Reporting Platform.

**Status:** Initial Interface and Backend Integration Completed

## Overview

This application uses Angular 22, TypeScript, RxJS, and PrimeNG to provide the user interface for the platform. Its initial dashboard includes a PrimeNG component test and a live connection test for the ASP.NET Core backend.

The backend connection is implemented with Angular's `HttpClient` and a dedicated service rather than direct HTTP logic in the template.

## Technology Stack

| Category | Technology |
|---|---|
| Framework | Angular 22 |
| Language | TypeScript |
| Markup and Styling | HTML, CSS |
| Components | PrimeNG 22 |
| Theme | Aura |
| Icons | PrimeIcons |
| Routing | Angular Router |
| HTTP Communication | Angular `HttpClient` |
| Reactive Programming | RxJS, Angular signals |
| Testing | Vitest-based Angular setup; feature tests planned |
| Package Management | npm |

## Implemented Features

- Angular application initialization and standalone component configuration
- Angular routing and CSS styling
- PrimeNG provider and Aura theme registration
- Initial dashboard layout with PrimeNG buttons
- Button interaction that updates frontend status
- Angular `HttpClient` provider configuration
- Typed `HealthResponse` interface
- Reusable `HealthService` for API requests
- Backend connection button that calls `GET /api/health`
- Display of the backend's response or a connection-error message
- Successful local development-server and production-build verification

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

This is a summary of the key application files, not a complete listing.

## Getting Started

### Prerequisites

- Node.js compatible with Angular 22
- npm
- Angular CLI 22

### Install Dependencies

From the `frontend` directory:

```powershell
npm install
```

### Start the Development Server

```powershell
npm start
```

Open `http://localhost:4200`.

### Build

```powershell
npm run build
```

### Unit Tests

```powershell
npm test
```

Additional automated tests will be implemented as application features are added.

## Backend Connection

The frontend currently calls the ASP.NET Core health-check endpoint:

```text
GET https://localhost:7174/api/health
```

The URL is configured in `src/app/services/health.service.ts`. If the backend uses a different local port, update the service accordingly. Environment-specific API configuration will be introduced in a later milestone.

### How It Works

1. Angular registers `provideHttpClient()` in `app.config.ts`.
2. `HealthService` uses `HttpClient` to request `/api/health`.
3. The root component triggers the request when **Test Backend Connection** is clicked.
4. The response updates an Angular signal displayed in the template.
5. If the API cannot be reached, the interface displays a connection-error message.

### Run the Full-Stack Test

1. Start `FinancialPlatform.Api` in Visual Studio using `F5`.
2. Start the Angular development server with `npm start`.
3. Open `http://localhost:4200`.
4. Click **Test Backend Connection**.

Expected message:

```text
Connected: Backend API is running.
```

The backend must be running, its HTTPS development certificate must be trusted, and its CORS policy must allow `http://localhost:4200`.

## Planned Features

- Reusable navigation and layout components
- Document upload and management interface
- Financial KPI cards and interactive charts
- Searchable, filterable financial data tables
- Form validation and notifications
- Login and role-based navigation
- Additional API services for documents, analysis, and reporting
- Automated component and service tests
- Environment-specific API configuration

## Development Progress

- **Angular initialization:** Completed
- **PrimeNG integration:** Completed
- **Backend connection using `HttpClient`:** Completed Locally
- **Database-backed features:** Next phase

See the [main project README](../README.md) and [Development Log](../docs/Development%20Log.md) for the full roadmap.
