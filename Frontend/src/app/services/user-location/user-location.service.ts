import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserLocationService {

  // @ts-ignore
  private userLocations = new BehaviorSubject<any>();
  getUserLocations = this.userLocations.asObservable();
  setUserLocations(obj) { this.userLocations.next(obj); }

  constructor() { }
}
