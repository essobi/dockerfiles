FROM alpine:3.4  
RUN apk --update add git  
  
#install mozjpeg  
RUN git clone git://github.com/mozilla/mozjpeg.git && \  
cd mozjpeg && \  
git checkout v3.1 && \  
apk --update add autoconf automake build-base libtool nasm && \  
cd /mozjpeg && autoreconf -fiv && ./configure --prefix=/usr && make install  
  
#install pngcrush  
RUN apk add pngcrush  
RUN apk add bc  
  
ADD compress /compress  
  
CMD ["/compress"]  

