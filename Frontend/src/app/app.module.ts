import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LocaisListingComponent } from './components/locais-listing/locais-listing.component';
import { HttpClientModule } from '@angular/common/http';
import { HttpService } from './services/http/http.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ModalInsertLocationComponent } from './components/locais-listing/modal-insert-location/modal-insert-location.component';
import { MatDialogModule } from '@angular/material/dialog';
import { ModalChangeUserLocationComponent } from './components/locais-listing/modal-change-user-location/modal-change-user-location.component';


@NgModule({
  declarations: [
    AppComponent,
    LocaisListingComponent,
    ModalInsertLocationComponent,
    ModalChangeUserLocationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatDialogModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
