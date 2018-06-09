FROM debian:stretch  
  
ARG TESS="4.00.00dev"  
ARG LEPTO="1.74.2"  
# Prepare dependencies  
RUN apt-get update  
RUN apt-get install -y \  
wget \  
make \  
autoconf \  
automake \  
libtool \  
autoconf-archive \  
pkg-config \  
libpng-dev \  
libjpeg-dev \  
libtiff-dev \  
zlib1g-dev \  
libicu-dev \  
libpango1.0-dev \  
libcairo2-dev  
  
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib  
  
# Compile Leptonica  
WORKDIR /  
RUN mkdir -p /tmp/leptonica \  
&& wget https://github.com/DanBloomberg/leptonica/archive/${LEPTO}.tar.gz \  
&& tar -xzvf ${LEPTO}.tar.gz -C /tmp/leptonica \  
&& mv /tmp/leptonica/* /leptonica  
WORKDIR /leptonica  
  
RUN autoreconf -i \  
&& ./autobuild \  
&& ./configure \  
&& make \  
&& make install  
  
# Compile Tesseract  
WORKDIR /  
RUN mkdir -p /tmp/tesseract \  
&& wget https://github.com/tesseract-ocr/tesseract/archive/${TESS}.tar.gz \  
&& tar -xzvf ${TESS}.tar.gz -C /tmp/tesseract \  
&& mv /tmp/tesseract/* /tesseract  
WORKDIR /tesseract  
  
RUN ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# Recover location  
WORKDIR /  
  
# Load languages  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
-P /usr/local/share/tessdata  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/deu.traineddata
-P /usr/local/share/tessdata  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/fra.traineddata
-P /usr/local/share/tessdata  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/spa.traineddata
-P /usr/local/share/tessdata  
RUN wget https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata
-P /usr/local/share/tessdata  

