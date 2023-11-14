from PIL import Image, ImageFilter


img= Image.open('colorproject12.jpg')
filtered= img.filter(ImageFilter.BLUR)
filtered.save('blurred.png','png')

filtered= img.convert('L')
filtered.save('grey.png','png')


filtered= img.rotate(180)
filtered.save('rotate.png', 'png')

filtered= img.resize((400,400))
filtered.save('resize.png', 'png')

box=(100, 100, 400, 400)
region= img.crop(box)
region.save('crop.png','png')

img.thumbnail((400, 400))
img.save('tumb.png','png')



