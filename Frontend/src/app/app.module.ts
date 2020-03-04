import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LocaisListingComponent } from './components/locais-listing/locais-listing.component';
import { HttpService } from './services/http/http.service';

@NgModule({
  declarations: [
    AppComponent,
    LocaisListingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
