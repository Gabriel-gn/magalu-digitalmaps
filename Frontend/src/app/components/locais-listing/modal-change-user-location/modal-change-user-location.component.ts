import { Component, OnInit } from '@angular/core';
import { HttpService } from 'src/app/services/http/http.service';
import { UserLocationService } from 'src/app/services/user-location/user-location.service';

@Component({
  selector: 'app-modal-change-user-location',
  templateUrl: './modal-change-user-location.component.html',
  styleUrls: ['./modal-change-user-location.component.scss']
})
export class ModalChangeUserLocationComponent implements OnInit {

  public locaisPorUserInput: any = {};
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
    const hrStr = hr > 9 ? '' + hr : '0' + hr;
    const min = this.randomIntFromInterval(0, 60);
    const minStr = min > 9 ? '' + min : '0' + min;
    const seg = this.randomIntFromInterval(0, 60);
    const segStr = seg > 9 ? '' + seg : '0' + seg;
    return hrStr + ':' + minStr + ':' + segStr;
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
      this.userLocationService.setUserLocations(retorno);
    });
  }

  constructor(private httpService: HttpService,
              public userLocationService: UserLocationService
              ) {
                // Serviço para passar variáveis/objetos através de componentes
                this.userLocationService.getUserLocations.subscribe(retorno => {
                  this.locaisPorUserInput = retorno;
                });
               }

  ngOnInit(): void {
  }

}
