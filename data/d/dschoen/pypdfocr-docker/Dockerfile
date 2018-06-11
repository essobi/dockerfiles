FROM ubuntu:latest  
MAINTAINER Dominik Schön <dominik@familie-schoen.com>  
  
ENV T_LANG deu  
  
RUN apt-get clean && apt-get update && apt-get install -y locales  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -y \  
tesseract-ocr \  
tesseract-ocr-${T_LANG} \  
ghostscript \  
imagemagick \  
python \  
python-pip \  
python-dev \  
gcc \  
libjpeg-dev \  
minizip \  
poppler-utils  
  
RUN pip install pypdfocr  
RUN cp /usr/share/tesseract-ocr/tessdata/${T_LANG}.traineddata
/usr/share/tesseract-ocr/tessdata/osd.traineddata  
  
VOLUME /media  
  
COPY config.yaml /media/.  
  
RUN find / | grep "pypdfocr"  
  
CMD ["/usr/local/bin/pypdfocr -w /media -f -c /media/config.yaml"]  

