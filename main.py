from PIL import Image
import os

size_28 = (28, 28)
size_56 = (56, 56)
size_112 = (112, 112)

for f in os.listdir('.'):
    if f.endswith('png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_112)
        i.save('resized_emotes/{}_112x112.png'.format(fn))

        i.thumbnail(size_56)
        i.save('resized_emotes/{}_56x56.png'.format(fn))

        i.thumbnail(size_28)
        i.save('resized_emotes/{}_28x28.png'.format(fn))
