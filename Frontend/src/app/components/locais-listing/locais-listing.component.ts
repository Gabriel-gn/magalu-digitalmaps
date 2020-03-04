import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
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
  public newLocationNome = '';
  public newLocationPosX = 0;
  public newLocationPosY = 0;
  public newLocationHorAbertura = '';
  public newLocationHorFechamento = '';
  @ViewChild('inputLocalizacaoNome', {static: true}) inputLocalizacaoNome: ElementRef;
  @ViewChild('inputLocalizacaoPosX', {static: true}) inputLocalizacaoPosX: ElementRef;
  @ViewChild('inputLocalizacaoPosY', {static: true}) inputLocalizacaoPosY: ElementRef;
  @ViewChild('inputLocalizacaoHorAbertura', {static: true}) inputLocalizacaoHorAbertura: ElementRef;
  @ViewChild('inputLocalizacaoHorFechamento', {static: true}) inputLocalizacaoHorFechamento: ElementRef;


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
    });
  }

  submitNewLocation() {
    let payload = {
      'nome': this.inputLocalizacaoNome.nativeElement.value,
      'pos_x': this.inputLocalizacaoPosX.nativeElement.value,
      'pos_y': this.inputLocalizacaoPosY.nativeElement.value,
      'hor_abertura': this.inputLocalizacaoHorAbertura.nativeElement.value,
      'hor_fechamento': this.inputLocalizacaoHorFechamento.nativeElement.value,
    }
    this.httpService.postNewLocation(payload).subscribe(retorno => {
      console.log(retorno);
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
