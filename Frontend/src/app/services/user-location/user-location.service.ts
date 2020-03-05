import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserLocationService {

  constructor() { }

  // @ts-ignore
  private userLocations = new BehaviorSubject<any>();
  getUserLocations = this.userLocations.asObservable();

  // @ts-ignore
  private userData = new BehaviorSubject<any>();
  getUserData = this.userData.asObservable();

  setUserLocations(obj) { this.userLocations.next(obj); }
  setUserData(obj) { this.userData.next(obj); }
}
