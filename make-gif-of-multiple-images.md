# Make Gif of multiple images

Firstly install ffmpeg
```bash
sudo apt-get install ffmpeg
```

make your images ordered.
here i had 100 file named overlay_1.png, overlay_2.png, ... they should be 001.png, 002.png, ...
```bash
rename 's/(\d+)/sprintf("%03d",$1)/e' overlay*.png
```

finally convert to gif
```bash
ffmpeg -framerate 10 -pattern_type glob -i 'overlay*.png' out.gif
```

Reference: https://www.bannerbear.com/blog/how-to-make-gifs-from-images-using-ffmpeg/
