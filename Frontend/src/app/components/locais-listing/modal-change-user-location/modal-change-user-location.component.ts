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
  public userData = {
    usrPosX: 0,
    usrPosY: 0,
    usrMts: 50,
    usrHr: '00:00:01' // necessário o segundo senão o horário não vem no formato hh:mm:ss, só hh:mm
  }

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
    const hr = this.randomIntFromInterval(0, 23);
    const hrStr = hr > 9 ? '' + hr : '0' + hr;
    const min = this.randomIntFromInterval(0, 59);
    const minStr = min > 9 ? '' + min : '0' + min;
    const seg = this.randomIntFromInterval(0, 59);
    const segStr = seg > 9 ? '' + seg : '0' + seg;
    return hrStr + ':' + minStr + ':' + segStr;
  }

  /**
   * Altera os dados de input do usuário aleatoriamente e requisita novamente à API os dados de locais
   */
  changeLocaisPorUserInput() {
    this.userData.usrPosX = this.randomIntFromInterval(0, 100);
    this.userData.usrPosY = this.randomIntFromInterval(0, 100);
    this.userData.usrMts = this.randomIntFromInterval(10, 100);
    this.userData.usrHr = this.randomTimeStr();
    this.updateInformacoesServices();
  }

  /**
   * Atualiza as informações do serviço de localizações, fazendo atualização em tempo real dos valores
   */
  updateInformacoesServices(): void {
    this.httpService.getLocationsByUserInput(
      this.userData.usrPosX,
      this.userData.usrPosY,
      this.userData.usrMts,
      this.userData.usrHr
      ).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
      this.userLocationService.setUserLocations(retorno);
      this.userLocationService.setUserData(this.userData);
    });
  }

  constructor(private httpService: HttpService,
              public userLocationService: UserLocationService
              ) {
                // Serviço para passar variáveis/objetos através de componentes
                this.userLocationService.getUserLocations.subscribe(retorno => {
                  this.locaisPorUserInput = retorno;
                });
                this.userLocationService.getUserData.subscribe(retorno => {
                  this.userData = retorno;
                });
               }

  ngOnInit(): void {
  }

}
