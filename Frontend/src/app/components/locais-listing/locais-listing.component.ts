import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpService } from 'src/app/services/http/http.service';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { ModalInsertLocationComponent } from './modal-insert-location/modal-insert-location.component';
import { ModalChangeUserLocationComponent } from './modal-change-user-location/modal-change-user-location.component';
import { UserLocationService } from 'src/app/services/user-location/user-location.service';

@Component({
  selector: 'app-locais-listing',
  templateUrl: './locais-listing.component.html',
  styleUrls: ['./locais-listing.component.scss']
})
export class LocaisListingComponent implements OnInit {

  public locaisPorUserInput: any = {};
  public locaisTodos: any = {};
  public userData = {
    usrPosX: 0,
    usrPosY: 0,
    usrMts: 50,
    usrHr: '00:00:01'  // necessário o segundo senão o horário não vem no formato hh:mm:ss, só hh:mm
  }

  public insertLocationModal: ModalInsertLocationComponent;

  /**
   * Abre o modal de cadastro de nova localização. Exibe uma mensagem ao confirmar
   * primeiro define as configurações do modal e exibe ele renderizando dentro o ModalInsertLocationComponent
   */
  abrirModalNovaLocalizacao(): void {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;
    dialogConfig.width = '80vw';

    this.modal.open(ModalInsertLocationComponent, dialogConfig);
  }

  /**
   * Abre o modal de cadastro de nova localização. Exibe uma mensagem ao confirmar
   * primeiro define as configurações do modal e exibe ele renderizando dentro o ModalChangeUserLocationComponent
   */
  abrirModalMudarLocalizacaoUsuario(): void {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;
    dialogConfig.width = '80vw';

    this.modal.open(ModalChangeUserLocationComponent, dialogConfig);
  }

  /**
   * Atualiza as informações do serviço de localizações, fazendo atualização em tempo real dos valores
   */
  updateInformacoesServices(): void {
    console.log(this.userData);
    this.httpService.getLocationsByUserInput(
      this.userData.usrPosX,
      this.userData.usrPosY,
      this.userData.usrMts,
      this.userData.usrHr
      ).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });
    this.userLocationService.setUserData(this.userData);
  }


  /**
   * O construtor inicia na inicialização do componente
   * @param httpService Serviço de subscrição para consumo de APIs
   */
  constructor(private httpService: HttpService,
              public modal: MatDialog,
              public userLocationService: UserLocationService
  ) {
    // Serviço para requerimento geral GET
    this.httpService.getLocationsByUserInput(
      this.userData.usrPosX,
      this.userData.usrPosY,
      this.userData.usrMts,
      this.userData.usrHr
      ).subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });

    this.httpService.getAllLocations().subscribe(retorno => {
      this.locaisTodos = retorno;
    });

    // Serviço para passar variáveis/objetos através de componentes
    this.userLocationService.getUserLocations.subscribe(retorno => {
      this.locaisPorUserInput = retorno;
    });
    this.userLocationService.setUserData(this.userData);
    this.userLocationService.getUserData.subscribe(retorno => {
      this.userData = retorno;
    });

  }

  ngOnInit(): void {
  }

}
