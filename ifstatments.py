"""Saya bangun
jika saya lapar:
    saya makan nasi uduk
jika tidak, jika saya tidak membeli sarapan:
    saya berangkat kerja
jika tidak,
    saya mandi"""

laki_laki = True
tinggi = False
if laki_laki or tinggi: #and
    print("Kamu Adalah laki-laki atau kamu tinggi")
elif laki_laki and not(tinggi):
    print("Kamu adalah laki-laki yang pendek")
elif not(laki_laki) and tinggi:
    print("Kamu adalah laki-laki yang pendek")
else:
    print("Kamu bukan laki-laki atau tidak tinggi")






