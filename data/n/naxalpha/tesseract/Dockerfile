FROM gcc:5  
MAINTAINER Nauman Mustafa <horizone5050@gmail.com>  
RUN apt update && apt -y upgrade && apt -y install git g++ cmake subversion
autoconf automake \  
libtool autoconf-archive pkg-config libpng12-dev libjpeg62-turbo-dev
libtiff5-dev zlib1g-dev  
RUN wget https://github.com/DanBloomberg/leptonica/archive/1.74.1.tar.gz && \  
tar -xzf 1.74.1.tar.gz && \  
cd leptonica-1.74.1/ && \  
libtoolize --force && aclocal && autoheader && automake --force-missing --add-
missing && autoconf && \  
./configure && make && make install && make check  
RUN wget https://github.com/tesseract-
ocr/tesseract/archive/4.00.00alpha.tar.gz && \  
git clone https://github.com/tesseract-ocr/tesseract.git && \  
cd tesseract/ && \  
./autogen.sh && ./configure --enable-debug && make && make install && ldconfig  
CMD ["/bin/bash"]  

