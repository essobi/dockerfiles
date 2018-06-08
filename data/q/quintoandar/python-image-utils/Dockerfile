FROM python:3.5  
ENV PYTHONPATH /usr/local/bin/python  
ENV LOGPATH /var/log  
  
RUN apt-get update && apt-get install -y gcc musl git imagemagick wget libxml2
libxml2-dev libxslt-dev tesseract-ocr-dev tesseract-ocr xvfb gfortran zbar-
tools poppler-utils ghostscript  
  
RUN mkdir -p /usr/share/tessdata/  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
-O /tmp/eng.traineddata > /dev/null  
RUN mv -v /tmp/eng.traineddata /usr/share/tessdata/  

