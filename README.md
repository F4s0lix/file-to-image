Can we save AI model as an PNG image?
==================
**YES YOU CAN!**
## How it works?
1. How model is saved?<br>
  In python with [pickle](https://docs.python.org/3/library/pickle.html) library object is converted into byte stream and we know that each byte is value from 0-255
2. How PNG format works?<br>
   For more acurate info how it work check [wikipedia](https://en.wikipedia.org/wiki/PNG) but for us most important data is that we can use PNG in grayscale where
   every pixel is one byte
3. 2 + 2<br>
  With both informations we can see that we can save each byte of model as next pixels in PNG.<br>
  But we have one issue:

If model is 9999B we can't have image this size. Nearest size is 100x100px. Solution to this issue is adding *\x00* to the end of model and length of original model
to EXIF of image. 

---
But how it affect model?
If PNG was not compressed, converted to another mode (for example RGBA) or EXIF truncated only affected thing is size.
| file | size |
|:-----|------:|
| model.pkl | 1.7MB |
| model.png | 272KB |
| extracted.pkl | 1.7MB |
