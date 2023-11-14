from PIL import Image, ImageDraw, ImageFont
img=Image.open('p.jpg')
d=ImageDraw.Draw((img))
fnt=ImageFont.truetype('comicbd.ttf', 25)
d.text((60, 60),"happy deepavali", font=fnt, fill=(255,255,255))
img.save('bb.jpg')

