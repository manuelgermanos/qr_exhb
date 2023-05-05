import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss'],
})
export class DetailsComponent implements OnInit {
  constID: string | null = null;
  constructorData: any;
  driversData: any[] | null = null;

  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  ngOnInit() {
    this.constID = this.route.snapshot.paramMap.get('constID');
    this.http
      .get<any>(`http://localhost:5000/constructor/${this.constID}`)
      .subscribe((data) => {
        this.constructorData = data.constructor;
        this.driversData = data.drivers;
      });
  }
}
