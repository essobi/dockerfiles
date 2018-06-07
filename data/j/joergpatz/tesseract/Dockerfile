FROM buildpack-deps:jessie  
MAINTAINER Joerg Patzer <joerg.patzer@me.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
leptonica-progs \  
ghostscript \  
tesseract-ocr \  
tesseract-ocr-deu \  
tesseract-ocr-eng \  
tesseract-ocr-spa \  
tesseract-ocr-fra \  
tesseract-ocr-ita \  
&& apt-get purge --auto-remove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/bin/tesseract"]

