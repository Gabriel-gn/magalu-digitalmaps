import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LocaisListingComponent } from './locais-listing.component';

describe('LocaisListingComponent', () => {
  let component: LocaisListingComponent;
  let fixture: ComponentFixture<LocaisListingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LocaisListingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LocaisListingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
