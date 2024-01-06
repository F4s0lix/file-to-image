Can we save files as an PNG image?
==================
**YES YOU CAN!**
## How it works?
1. How files are saved?<br>
  Each file is set of bytes - values from 0 to 255. In python we can read raw bytes from file:
  ```python
  with open('filename.file', 'rb') as file: ...
  ```
3. How PNG format works?<br>
   For more acurate info how it work check [wikipedia](https://en.wikipedia.org/wiki/PNG) but for us most important data is that we can use PNG in grayscale where every pixel is one byte (value from 0-255)
4. 1 + 1<br>
  With both informations we can see that we can save each byte of file as next pixels in PNG.<br>
  But we have one issue:

If file is 9999B we can't have image this size. Nearest size is 100x100px. Solution to this issue is adding *\x00* to the end of byte stream and length of original file to EXIF of image. 

---
But how it affect files?
---
If PNG was not compressed, converted to another mode (for example RGBA) or EXIF truncated only affected thing is size.
| file | size |
|:-----|------:|
| model.pkl | 1.7MB |
| model.png | 272KB |
| extracted.pkl | 1.7MB |
