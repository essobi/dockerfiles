FROM debian:stretch  
MAINTAINER mrxra  
  
  
WORKDIR /tmp  
  
# https://github.com/tesseract-ocr/tesseract/wiki/Compiling#linux  
# https://github.com/tesseract-
ocr/tesseract/wiki/Compiling-%E2%80%93-GitInstallation  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
git \  
ca-certificates \  
autoconf-archive \  
automake \  
g++ \  
libtool \  
libleptonica-dev \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd ${WORKDIR} \  
&& git clone \--depth 1 https://github.com/tesseract-ocr/tesseract \  
&& cd tesseract \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig  
  
RUN cd ${WORKDIR} \  
&& git clone \--depth 1 https://github.com/tesseract-ocr/tessdata_fast \  
&& mv tessdata_fast/* /usr/local/share/tessdata/ && rm -rf tessdata_fast  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
inotify-tools \  
ghostscript \  
imagemagick \  
pdftk \  
&& rm /etc/ImageMagick-6/policy.xml \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD tesseract.sh /opt/tesseract.sh  
RUN chmod 750 /opt/tesseract.sh  
  
ENV OCR_DATA /opt/pdfocr  
  
VOLUME ${OCR_DATA}  
  
CMD ["/opt/tesseract.sh", $OCR_DATA ]  

