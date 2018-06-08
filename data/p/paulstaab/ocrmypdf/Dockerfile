# OCRmyPDF  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Paul Staab <develop@paulstaab.de>  
  
# Add unprivileged user  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bc \  
curl \  
parallel \  
poppler-utils \  
imagemagick \  
unpaper \  
tesseract-ocr tesseract-ocr-deu tesseract-ocr-spa tesseract-ocr-eng tesseract-
ocr-fra \  
python2.7 python-lxml python-reportlab python-pil \  
ghostscript \  
openjdk-7-jdk \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install OCRmyPDF  
RUN cd /usr/local && \  
curl -L https://github.com/fritz-hh/OCRmyPDF/archive/v2.2-stable.tar.gz | tar
xz  
RUN ln -s /usr/local/OCRmyPDF-2.2-stable/OCRmyPDF.sh /usr/local/bin/OCRmyPDF
&& \  
ln -s /usr/bin/python2.7 /usr/local/bin/python2  
  
USER docker  
WORKDIR /home/docker  
ENV SHELL /bin/sh  
  

