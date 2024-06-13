import pytest
from gra_liczbowa import GraLiczbowa

def test_wygrana_za_pierwszym_razem():
    gra = GraLiczbowa(liczba=5)
    assert gra.zgadnij(5) == "Gratulacje! Zgadłeś!"
    assert gra.wygrana
    assert gra.proby == 1

def test_przegrana_po_trzech_probach():
    gra = GraLiczbowa(liczba=5)
    assert gra.zgadnij(1) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(2) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(3) == "Nie zgadłeś! Prawidłowa liczba to 5."
    assert not gra.wygrana
    assert gra.proby == 3

def test_przekroczenie_maks_proby():
    gra = GraLiczbowa(liczba=5)
    gra.zgadnij(1)
    gra.zgadnij(2)
    gra.zgadnij(3)
    with pytest.raises(Exception, match="Przekroczono maksymalną liczbę prób"):
        gra.zgadnij(4)

def test_rozne_liczby():
    gra = GraLiczbowa(liczba=7)
    assert gra.zgadnij(5) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(6) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(7) == "Gratulacje! Zgadłeś!"
    assert gra.wygrana
    assert gra.proby == 3

def test_inicjalizacja_bez_liczby():
    gra = GraLiczbowa()
    assert 1 <= gra.liczba <= 10
    assert gra.maks_proby == 3
    assert gra.proby == 0
    assert not gra.wygrana

def test_zgadnij_po_przegranej():
    gra = GraLiczbowa(liczba=5)
    gra.zgadnij(1)
    gra.zgadnij(2)
    gra.zgadnij(3)
    with pytest.raises(Exception, match="Przekroczono maksymalną liczbę prób"):
        gra.zgadnij(4)

def test_zgadnij_przed_przegrana():
    gra = GraLiczbowa(liczba=5)
    assert gra.zgadnij(1) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(2) == "Spróbuj jeszcze raz!"
    assert gra.zgadnij(5) == "Gratulacje! Zgadłeś!"
    assert gra.wygrana
    assert gra.proby == 3
