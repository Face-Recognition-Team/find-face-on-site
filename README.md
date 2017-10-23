# find-face-on-site
Find your face on a websites.

----------

__index__
usage:

```
python index.py sites_list.txt photo.jpg 

```

первый аргумент содержит в себе список сайтов, по которым необходимо производить поиск
второй аргумент - это фотография с изображением лица человека, которое будет искаться на картинках сайтов


__image_downloader__
usage:

```
import image_downloader

image_downloader.get_images('http://e1.ru')
```

второй аргумент, опционально, принимает output_directory. по дефолту 'photos'


__recognizer__
usage:

```
import recognizer

recognizer.recognize('photo.jpg', 'my_photos')
```

второй аргумент, опционально, принимает output_directory. по дефолту 'photos'
