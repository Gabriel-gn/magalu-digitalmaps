import { Component, OnInit } from '@angular/core';
import { HttpService } from 'src/app/services/http/http.service';

@Component({
  selector: 'app-locais-listing',
  templateUrl: './locais-listing.component.html',
  styleUrls: ['./locais-listing.component.scss']
})
export class LocaisListingComponent implements OnInit {

  public locaisPorUserInput: any = {};
  public locaisTodos: any = {};
  public usrPosX = 0;
  public usrPosY = 0;
  public usrMts = 50;
  public usrHr = '00:00:00';

  /**
   * Retorno um inteiro aleatório entre dois valores
   * @param min valor inteiro mínimo
   * @param max valor inteiro máximo
   */
  randomIntFromInterval(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  /**
   * Retorna um horário aleatório no formato hh:mm:ss
   */
  randomTimeStr() {
    const hr = this.randomIntFromInterval(0, 24);
    let hr_str = hr > 9 ? '' + hr : '0' + hr;
    const min = this.randomIntFromInterval(0, 60);
    let min_str = min > 9 ? '' + min : '0' + min;
    const seg = this.randomIntFromInterval(0, 60);
    let seg_str = seg > 9 ? '' + seg : '0' + seg;
    return hr_str + ':' + min_str + ':' + seg_str;
  }

  /**
   * Altera os dados de input do usuário aleatoriamente e requisita novamente à API os dados de locais
   */
  changeLocaisPorUserInput() {
    this.usrPosX = this.randomIntFromInterval(0, 100);
    this.usrPosY = this.randomIntFromInterval(0, 100);
    this.usrMts = this.randomIntFromInterval(10, 100);
    this.usrHr = this.randomTimeStr();
    this.httpService.getLocationsByUserInput(this.usrPosX, this.usrPosY, this.usrMts, this.usrHr).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });
  }


  /**
   * O construtor inicia na inicialização do componente
   * @param httpService Serviço de subscrição para consumo de APIs
   */
  constructor(private httpService: HttpService) {
    this.httpService.getLocationsByUserInput(this.usrPosX, this.usrPosY, this.usrMts, this.usrHr).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });
  }

  ngOnInit(): void {
  }

}
