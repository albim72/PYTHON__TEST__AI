from PIL import Image, ImageEnhance, ImageOps, ImageDraw, ImageFont

img = Image.open('input.jpg')

#zmiana rozzmiaru
img_resized = img.resize((600, 400))

#konwersja do skali szarości
img_gray = img_resized.convert('L')

#zwiększenie kontrastu
enhacer = ImageEnhance.Contrast(img_gray)
img_contrasted = enhacer.enhance(1.8)

#dodanie ramki o grubości 10px w kolorze czarnym
img_bordered = ImageOps.expand(img_contrasted, border=10, fill='black')

#narysuj prostokąt i tekst
draw = ImageDraw.Draw(img_bordered)
draw.rectangle([(20,20),(280,280)], outline='white', width=3)
try:
    font = ImageFont.truetype('arial.ttf', 25)
except:
    font = ImageFont.load_default()
draw.text((30, 200), 'Przetworzony rysunek!', fill='white', font=font)

#zapis wynik
img_bordered.save('output_complex.jpg')
print('Zapisano wynik do output_complex.jpg')


