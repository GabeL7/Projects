
import { Component, inject, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { HealthService } from './services/health.service';

@Component({
  selector: 'app-root',
  imports: [ButtonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  private readonly healthService = inject(HealthService);

  protected readonly status = signal('Frontend initialized.');
  protected readonly apiStatus = signal('Backend not tested.');

  protected testPrimeNG() {
    this.status.set('PrimeNG is working correctly');
  }

  protected testBackend() {
    this.apiStatus.set('Connecting to backend...');

    this.healthService.getHealth().subscribe({
      next: (response) => {
        this.apiStatus.set(`Connected: ${response.message}`);
      },
      error: () => {
        this.apiStatus.set(
          'Unable to connect to the backend. Check that the API is running.'
        );
      }
    });
  }
}
