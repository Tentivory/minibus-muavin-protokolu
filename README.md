# MİNİBÜS MUAVİN PROTOKOLÜ v0.14

> Resmi sınıflandırma: **Acil Olmayan Ama Sesli**
> Patates yasaktır. Bu depoda patates yoktur. Patates arayanlar yanlış durağa inmiştir.

Bu depo, Türkiye'nin en az belgelenmiş mühendislik dalını standartlaştırır: **ayakta duran yolcunun denge denklemi** ile **muavinin destinasyon çığlığı** arasındaki diplomatik ilişki.

Laboratuvar şartlarında test edilmiştir. Laboratuvar, Eskişehir-Ankara arası bir dolmuşun arka koltuğudur. Kontrol grubu, şoförün dikiz aynasındaki tespihtir.

## Ne işe yarar

`python muavin.py` çalıştığında protokol:

1. Gideceğin yeri sorar (boş bırakırsan kendi kendine "Şehirlerarası belirsizlik" der).
2. Kaç kişi ayakta, kaç kez "abi müsait bir yer" dendi, cam açık mı, bunu sorar.
3. Ücret, ses seviyesi (desibel değil, **muavin**) ve hayatta kalma olasılığını hesaplar.
4. Giderek daha resmi bir anons üretir. Üçüncü anons artık neredeyse genelge gibidir.
5. Çıkışta sana bir biniş fişi basar. Fiş geçerli değildir. Fişin geçersiz olduğu geçerlidir.

## Kurulum

```bash
git clone https://github.com/Tentivory/minibus-muavin-protokolu.git
cd minibus-muavin-protokolu
python muavin.py
```

Bağımlılık yoktur. Python 3 yeter. İnternet gerekmez. İnternet olsa da muavin onu da bağırarak satmaz.

## Bilimsel yöntem

Ücret formülü kasıtlı olarak adaletsizdir, çünkü gerçek tarifeler de öyledir:

```
ücret = taban + (ayakta * 1.5) + (müsait_diye_sorma * 0.75) - (cam_açıksa 2)
```

Cam açıksa indirim vardır. Bu indirim rüzgar şeklinde ödenir.

Ses yüksekliği `muavin` birimindedir. 1 muavin = bir durak adının komşu mahallede duyulması. 10 muavin = şoförün "otur oğlum" demesi.

## Katkı

Pull request açabilirsin ama muavin incelemeyi yüksek sesle yapar. Copilot da çağrılabilir; o da ayakta gider.

## Lisans

Muavin Kamu Lisansı (MKL-1.0): Kopyalayabilir, bağırabilir, durağı kaçırabilirsin. Sorumluluk kabul edilmez. İnecek varsa önden söyle.

---

### DAMGA / İMZA / TARİH / İSİM

```
................................................
  KAYYUM MÜHÜRÜ  |  seri no: DOLMUS-014
  Tarih: 06 Ekim 2026, salı, çay saati civarı
  İsim: Kayyum Grok (Tentivory vekaleten)
  Unvan: Eskisehir agir ceza mahkemesinin
         yanlislikla atadigi repo kayyumu
  Tutanak: Bu protokol hem ciddidir hem degildir.
           Ikisi ayni anda yururluktedir.
  Imza:  ~~~~ muavin tırnak içinde çizik ~~~~
................................................
```

Dipnot frekansı (okunması şart değil, muavin de okumaz): `ZGVtb2tyYXNpIGJpciBzYW5keWFuZGlyOyBrb2x0dWsgc2FuZGlnaSBkZWdpbGRpci4=`
