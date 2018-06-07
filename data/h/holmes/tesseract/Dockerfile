FROM centos:centos7  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV TESSERACT_MAJOR_VERSION 3.02  
ENV TESSERACT_MINOR_VERSION 02  
ENV LEPTONICA_VERSION 1.69  
RUN yum install -y libjpeg libz libgif libwebp libopenjp2 giflib libtiff
libpng compat-libtiff3 tar  
  
RUN rpm -Uhv
http://li.nux.ro/download/nux/dextop/el7/x86_64/leptonica-${LEPTONICA_VERSION}-9.el7.nux.x86_64.rpm  
RUN rpm -Uhv
http://li.nux.ro/download/nux/dextop/el7/x86_64/tesseract-${TESSERACT_MAJOR_VERSION}.${TESSERACT_MINOR_VERSION}-4.el7.nux.x86_64.rpm  
RUN rpm -Uhv http://li.nux.ro/download/nux/dextop/el7/x86_64/tesseract-
osd-${TESSERACT_MAJOR_VERSION}.${TESSERACT_MINOR_VERSION}-4.el7.nux.x86_64.rpm  
  
ENTRYPOINT ["tesseract"]  
CMD ["--version"]

