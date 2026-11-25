# Financial Document Analysis Platform — Frontend

The Angular frontend for the Financial Document Analysis & Reporting Platform.

**Status:** Initial Frontend and PrimeNG Integration Completed

## Overview

This frontend application is built using Angular 22, TypeScript, CSS, RxJS, and PrimeNG.

It will provide the user interface for managing financial documents, viewing financial dashboards, analyzing company performance, and generating reports.

The initial application setup is complete, and the PrimeNG component library has been integrated successfully.

## Technology Stack

| Category | Technology |
|---|---|
| Frontend Framework | Angular 22 |
| Language | TypeScript |
| Markup and Styling | HTML, CSS |
| UI Components | PrimeNG |
| UI Theme | Aura |
| Icons | PrimeIcons |
| Reactive Programming | RxJS |
| Routing | Angular Router |
| Testing Framework | Vitest |
| Package Management | npm |
| Version Control | Git, GitHub |

## Implemented Features

- Angular application initialization
- Standalone Angular component architecture
- Angular routing configuration
- CSS styling
- PrimeNG integration
- Aura theme configuration
- Initial application layout
- Interactive PrimeNG button
- Working local development server
- Successful Angular production build

## Planned Features

- Reusable application navigation
- Financial dashboard with KPI cards
- Financial document management interface
- Data tables with searching, filtering, and sorting
- Financial charts and visualizations
- Company and reporting-period comparisons
- Document upload interface
- User login and authentication
- Role-based navigation and permissions
- REST API integration
- Loading indicators and error handling
- Responsive interface design

## Project Structure

```text
frontend/
├── public/
├── src/
│   ├── app/
│   │   ├── app.ts
│   │   ├── app.html
│   │   ├── app.css
│   │   ├── app.config.ts
│   │   └── app.routes.ts
│   ├── index.html
│   ├── main.ts
│   └── styles.css
├── angular.json
├── package.json
├── package-lock.json
└── README.md
```

Additional folders for components, pages, services, and models will be introduced as development progresses.

## Getting Started

### Prerequisites

- Node.js compatible with Angular 22
- npm
- Angular CLI

### Install Dependencies

From the `frontend` directory:

```powershell
npm install
```

### Run the Development Server

```powershell
npm start
```

Alternatively:

```powershell
ng serve
```

Open `http://localhost:4200/` in your browser.

The application automatically reloads when source files change.

### Build the Application

```powershell
npm run build
```

### Run Unit Tests

```powershell
npm test
```

The project uses Angular's generated Vitest testing setup. Additional tests will be developed as application functionality is implemented.

## PrimeNG Configuration

PrimeNG provides reusable UI components for the application.

The initial configuration includes:

- PrimeNG packages installed through npm
- Aura theme configured in `app.config.ts`
- Global PrimeNG configuration using `providePrimeNG()`
- Button component imported into the Angular application
- Functional button interaction verified in the browser

PrimeNG will also support future components such as tables, charts, dialogs, menus, forms, and notifications.

Any required PrimeNG licensing credentials must be kept outside the public GitHub repository.

## Backend Integration

The frontend will communicate with the ASP.NET Core Web API through HTTP requests using JSON.

Planned integrations include financial document management, data analysis, authentication, authorization, and reporting.

Backend API integration has not yet been implemented.

## Development Progress

### Completed

- Angular CLI project generation
- Frontend routing and styling setup
- PrimeNG installation and configuration
- Initial application interface
- Component interaction testing
- Successful application build

### Next Steps

- Create the ASP.NET Core backend
- Implement the first REST API endpoint
- Connect Angular to backend responses
- Expand the frontend with reusable components

## Development Practices

- Build and test features incrementally
- Use meaningful Git commits
- Keep dependencies tracked through `package.json` and `package-lock.json`
- Exclude `node_modules/` and generated build files from Git
- Avoid committing secrets or private credentials
- Document completed features and technical decisions

## Project Purpose

To demonstrate Angular development, reusable UI components, application architecture, frontend testing, and integration with a production-style backend.