import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalChangeUserLocationComponent } from './modal-change-user-location.component';

describe('ModalChangeUserLocationComponent', () => {
  let component: ModalChangeUserLocationComponent;
  let fixture: ComponentFixture<ModalChangeUserLocationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModalChangeUserLocationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModalChangeUserLocationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
