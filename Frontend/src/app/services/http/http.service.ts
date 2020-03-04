import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  getLocationsByUserInput(posX: number, posY: number, mts: number, hr: string) {
    return this.http.get(`http://${environment.backend}/locais/user?pos_x=${posX}&pos_y=${posY}&mts=${mts}&hr=${hr}`);
  }
}
