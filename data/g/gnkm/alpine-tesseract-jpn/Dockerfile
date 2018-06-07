FROM alpine:3.4  
MAINTAINER gnkm <@gnkm>  
  
RUN set -x && \  
# enable to use wget command for donwloading from https site  
apk add --update --no-cache --virtual wget-dependencies \  
ca-certificates \  
openssl && \  
# tesseract is in testing repo  
echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk add --update --no-cache tesseract-ocr && \  
# download traineddata  
# english  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.bigrams && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.fold && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.lm && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.nn && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.params && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.size && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.cube.word-freq && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.tesseract_cube.nn && \  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.traineddata && \  
# japanese  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/jpn.traineddata && \  
# enable to use hocr option  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/osd.traineddata && \  
# delete wget-dependencies  
apk del wget-dependencies  

