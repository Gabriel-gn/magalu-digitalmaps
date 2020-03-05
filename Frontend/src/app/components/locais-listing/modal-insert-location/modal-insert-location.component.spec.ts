import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalInsertLocationComponent } from './modal-insert-location.component';

describe('ModalInsertLocationComponent', () => {
  let component: ModalInsertLocationComponent;
  let fixture: ComponentFixture<ModalInsertLocationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModalInsertLocationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModalInsertLocationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
