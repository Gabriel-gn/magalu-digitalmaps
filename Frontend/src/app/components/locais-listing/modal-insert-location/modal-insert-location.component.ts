import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpService } from 'src/app/services/http/http.service';

@Component({
  selector: 'app-modal-insert-location',
  templateUrl: './modal-insert-location.component.html',
  styleUrls: ['./modal-insert-location.component.scss']
})
export class ModalInsertLocationComponent implements OnInit {

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
   * Adiciona um novo local via POST request baseado nos valores de input dos campos do form.
   * Não faz uso da função 'submit' nativa do form.
   */
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

  constructor(private httpService: HttpService) { }

  ngOnInit(): void {
  }

}
