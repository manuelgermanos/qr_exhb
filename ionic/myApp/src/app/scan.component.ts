import { Component } from '@angular/core';
import type { BarcodeScanner } from '@ionic-native/barcode-scanner';
import { Router } from '@angular/router';

@Component({
  selector: 'app-scan',
  templateUrl: './scan.component.html',
  styleUrls: ['./scan.component.scss'],
})
export class ScanComponent {
  constructor(private barcodeScanner: BarcodeScanner, private router: Router) {}

  scanQRCode() {
    this.barcodeScanner.scan().then((barcodeData) => {
      this.router.navigate(['/details', barcodeData.text]);
    });
  }
}
