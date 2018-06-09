FROM ruby:2.4.1  
  
ENV TESSERACT_VERSION 3.02.02  
  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y libleptonica-dev unzip \  
&& cd /usr/src \  
&& wget -O tesseract-ocr.zip "https://github.com/tesseract-
ocr/tesseract/archive/$TESSERACT_VERSION.zip" \  
&& unzip tesseract-ocr.zip \  
&& cd tesseract-$TESSERACT_VERSION \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig  

