
import { Component, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-root',
  imports: [ButtonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly status = signal('Frontend initialized.');

  protected testPrimeNG() {
    this.status.set('PrimeNG Button Test');
  }
}
  