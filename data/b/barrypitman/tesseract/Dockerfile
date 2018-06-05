# Create an ubuntu image with tesseract installed.  
FROM ubuntu:14.04  
MAINTAINER Barry Pitman <barrypitman@gmail.com>  
RUN apt-get -qq update  
RUN apt-get -qqy install tesseract-ocr  
  
# perform OCR like this, e.g. :  
# docker run -i tesseract /usr/bin/tesseract stdin stdout -psm 3 -c
tessedit_char_whitelist=0123456789 < ocrimage.png  

