import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  /**
   *
   * @param posX: posição X do usuário
   * @param posY: posição Y do usuário
   * @param mts: distância máxima de locais relativos à posição do usuário
   * @param hr: horário para verificação se o local está aberto ou fechado
   */
  getLocationsByUserInput(posX: number, posY: number, mts: number, hr: string) {
    return this.http.get(`http://${environment.backend}/locais/user?pos_x=${posX}&pos_y=${posY}&mts=${mts}&hr=${hr}`);
  }

  /**
   * Retorna todas as localizações pois a distância em mts é muito alta
   * TODO fazer a distância em mts ser igual ao maior valor presente no banco de dados
   * @param hr Deve-se fornecer a hora em formato hh:mm:ss string.
   */
  getAllLocations(hr: string) {
    return this.http.get(`http://${environment.backend}/locais/user?pos_x=0&pos_y=0&mts=2000000000&hr=${hr}`);
  }
}
