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
   * Retorna todas as localizações pelo django rest framework.
   */
  getAllLocations() {
    return this.http.get(`http://${environment.backend}/locais/?nome__icontains=`);
  }

  /**
   * Adiciona nova localização ao backend
   * @param payload corpo em JSON a ser adicionado
   * ex:
   * {
   *   "nome": "Casa Mal Assombrada 2",
   *   "pos_x": 18,
   *   "pos_y": 88,
   *   "hor_abertura": "19:00:00",
   *   "hor_fechamento": "03:00:00"
   * }
   */
  postNewLocation(payload: any) {
    return this.http.post(`http://${environment.backend}/locais/`, payload);
  }

}
