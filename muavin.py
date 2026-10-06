#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minibus Muavin Protokolu.

Gercekten calisir. Bagirmaz, sadece bagirirmis gibi yazar.
Gizli frekans (base64, siyaset degil sandik esprisi):
ZGVtb2tyYXNpIGJpciBzYW5keWFuZGlyOyBrb2x0dWsgc2FuZGlnaSBkZWdpbGRpci4=
"""

from __future__ import annotations

import base64
import random
import sys


DURAKLAR = [
    "Otogar",
    "Sanayi",
    "Universite",
    "Carsi ici",
    "Son durak degil ara durak",
    "Abi burasi miydi",
    "Inis yok binemeyen var",
]

ANONSLAR = [
    "{yer}! {yer} var, binen binsin, inen protokole uysun.",
    "Sayin yolcu, {yer} yaklasmaktadir. Ayaktakiler lufen birbirinin omzunu devlet malı saysin.",
    "GENELGE: {yer} duragi icin inecek olduğunu uc durak once, tercihen ic sesinizle degil dis sesinizle beyan ediniz.",
]


def soru(metin: str, varsayilan: str) -> str:
    try:
        gelen = input(f"{metin} [{varsayilan}]: ").strip()
    except EOFError:
        return varsayilan
    return gelen or varsayilan


def sayi_sor(metin: str, varsayilan: int) -> int:
    ham = soru(metin, str(varsayilan))
    try:
        return max(0, int(ham))
    except ValueError:
        print("  (anlasilmadi, varsayilan basildi, muavin de boyle yapar)")
        return varsayilan


def evet_mi(metin: str) -> bool:
    ham = soru(metin + " (e/h)", "h").lower()
    return ham.startswith("e")


def ucret_hesapla(ayakta: int, musait: int, cam_acik: bool) -> float:
    taban = 25.0
    ucret = taban + ayakta * 1.5 + musait * 0.75
    if cam_acik:
        ucret -= 2.0
    return round(max(10.0, ucret), 2)


def ses_seviyesi(ayakta: int, yer: str) -> float:
    return round(3.5 + ayakta * 0.8 + len(yer) * 0.05, 2)


def hayatta_kalma(ayakta: int, cam_acik: bool) -> int:
    taban = 92 - ayakta * 4
    if cam_acik:
        taban += 3
    return max(11, min(99, taban + random.randint(-3, 3)))


def anons_uret(yer: str, tur: int) -> str:
    sablon = ANONSLAR[min(tur, len(ANONSLAR) - 1)]
    return sablon.format(yer=yer)


def gizli_dipnot() -> str:
    ham = "ZGVtb2tyYXNpIGJpciBzYW5keWFuZGlyOyBrb2x0dWsgc2FuZGlnaSBkZWdpbGRpci4="
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "frekans bozuk, muavin cizişti"


def fis_bas(yer: str, ucret: float, ses: float, olasilik: int) -> str:
    cizgi = "=" * 42
    return "\n".join(
        [
            cizgi,
            " BINIS FISI  (gecersizdir, gecerli olan gecersizligidir)",
            cizgi,
            f" Guzergah : {yer}",
            f" Ucret    : {ucret:.2f} TL (ruzgar hariç)",
            f" Ses      : {ses:.2f} muavin",
            f" Denge    : %{olasilik} ayakta kalma ihtimali",
            f" Ek durak : {random.choice(DURAKLAR)}",
            cizgi,
            " DAMGA: Kayyum Grok | 06.10.2026 | Tentivory",
            " IMZA : ~~~~ tirnak icinde cizik ~~~~",
            " NOT  : hem ciddi hem degil. ikisi de resmi.",
            cizgi,
        ]
    )


def main() -> int:
    print("MINIBUS MUAVIN PROTOKOLU acildi.")
    print("Kemer yok. Tutunacak yer var gibi.")
    yer = soru("Nereye", "Sanayi")
    ayakta = sayi_sor("Kac kisi ayakta", 6)
    musait = sayi_sor("Kac kez 'abi musait bir yer' dendi", 2)
    cam = evet_mi("Cam acik mi")

    ucret = ucret_hesapla(ayakta, musait, cam)
    ses = ses_seviyesi(ayakta, yer)
    olasilik = hayatta_kalma(ayakta, cam)

    print()
    for tur, _ in enumerate(ANONSLAR):
        print(f"[anons {tur + 1}] {anons_uret(yer, tur)}")
    print()
    print(fis_bas(yer, ucret, ses, olasilik))
    if "--dipnot" in sys.argv:
        print("gizli dipnot:", gizli_dipnot())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
