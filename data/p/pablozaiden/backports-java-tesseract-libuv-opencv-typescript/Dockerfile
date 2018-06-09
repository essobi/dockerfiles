FROM pablozaiden/typescript  
  
RUN sed -i
's/http:\/\/httpredir\\.debian\\.org\/debian/http:\/\/ftp.us.debian.org\/debian/g'
/etc/apt/sources.list  
  
RUN echo "deb http://ftp.us.debian.org/debian/ jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y default-jre  
RUN apt-get install -y libtesseract-dev  
RUN apt-get install -y tesseract-ocr-eng  
RUN apt-get install -y tesseract-ocr-spa  
RUN apt-get install -y libuv1-dev  
RUN apt-get install -y libopencv-dev  
RUN apt-get install -y opencv-data  
RUN apt-get install -y build-essential  

