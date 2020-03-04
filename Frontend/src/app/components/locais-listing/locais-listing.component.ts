import { Component, OnInit } from '@angular/core';
import { HttpService } from 'src/app/services/http/http.service';

@Component({
  selector: 'app-locais-listing',
  templateUrl: './locais-listing.component.html',
  styleUrls: ['./locais-listing.component.scss']
})
export class LocaisListingComponent implements OnInit {

  private locaisPorUserInput: any = {};
  private locaisTodos: any = {};
  private usrPosX = 0;
  private usrPosY = 0;
  private usrMts = 50;
  private usrHr = '00:00:00';


  constructor(private httpService: HttpService) {
    this.httpService.getLocationsByUserInput(this.usrPosX, this.usrPosY, this.usrMts, this.usrHr).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });
  }

  ngOnInit(): void {
  }

}
