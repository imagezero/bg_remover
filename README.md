# bg_remover

Remove Background from Images

![demo](c.gif)


This also provides a remove bg command line tool that lets
you make a transparent images on a folder of images from the command line!

### Usage
```python
python bg_remover.py 1.png

```

or


```python
from bg_remover import run

run("1.png")

```


Common Issues
-------------

Issue: ``Illegal instruction (core dumped)`` when using
face\_recognition or running examples.

| Solution: ``dlib`` is compiled with SSE4 or AVX support, but your CPU
  is too old and doesn't support that.
| You'll need to recompile ``dlib`` after `making the code change
  outlined
  here <https://github.com/ageitgey/face_recognition/issues/11#issuecomment-287398611>`__.

Issue:
``RuntimeError: Unsupported image type, must be 8bit gray or RGB image.``
when running the webcam examples.

Solution: Your webcam probably isn't set up correctly with OpenCV. `Look
here for
more <https://github.com/ageitgey/face_recognition/issues/21#issuecomment-287779524>`__.

Issue: ``MemoryError`` when running ``pip2 install face_recognition``

| Solution: The face\_recognition\_models file is too big for your
  available pip cache memory. Instead,
| try ``pip2 --no-cache-dir install face_recognition`` to avoid the
  issue.

Issue:
``AttributeError: 'module' object has no attribute 'face_recognition_model_v1'``

Solution: The version of ``dlib`` you have installed is too old. You
need version 19.7 or newer. Upgrade ``dlib``.

Issue:
``Attribute Error: 'Module' object has no attribute 'cnn_face_detection_model_v1'``

Solution: The version of ``dlib`` you have installed is too old. You
need version 19.7 or newer. Upgrade ``dlib``.

Issue: ``TypeError: imread() got an unexpected keyword argument 'mode'``

Solution: The version of ``scipy`` you have installed is too old. You
need version 0.17 or newer. Upgrade ``scipy``.
