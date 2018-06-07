FROM alpine:3.7  
LABEL maintainer "mark@markhollow.com"  
  
RUN apk add \--no-cache jpeg libpng tiff zlib libstdc++ libgcc libgomp && \  
apk add \--no-cache build-base gcc abuild binutils autoconf pkgconfig \  
automake libtool git jpeg-dev libpng-dev tiff-dev zlib-dev \  
icu icu-dev && \  
git clone https://github.com/peti/autoconf-archive.git && \  
mkdir -p /usr/share/aclocal && \  
cp -a autoconf-archive/m4/* /usr/share/aclocal && \  
rm -rf autoconf-archive && \  
mkdir -p /build && \  
cd /build && \  
curl -o \- https://codeload.github.com/DanBloomberg/leptonica/tar.gz/1.74.2 |
tar xzf - && \  
cd leptonica-1.74.2 && \  
./autobuild && \  
./configure --prefix=/usr/local && \  
make install && \  
cd /build && \  
curl -o \- https://codeload.github.com/tesseract-ocr/tesseract/tar.gz/master |
tar xzf - && \  
cd tesseract-master && \  
./autogen.sh && \  
./configure --prefix=/usr/local && \  
make install && \  
ldconfig / && \  
cd /usr/local/share/tessdata && \  
curl -o osd.traineddata https://raw.githubusercontent.com/tesseract-
ocr/tessdata/3.04.00/osd.traineddata && \  
curl -o equ.traineddata https://raw.githubusercontent.com/tesseract-
ocr/tessdata/3.04.00/equ.traineddata && \  
curl -o eng.traineddata https://raw.githubusercontent.com/tesseract-
ocr/tessdata/4.00/eng.traineddata && \  
curl -o fra.traineddata https://raw.githubusercontent.com/tesseract-
ocr/tessdata/4.00/fra.traineddata && \  
curl -o tha.traineddata https://raw.githubusercontent.com/tesseract-
ocr/tessdata/4.00/tha.traineddata && \  
apk del build-base gcc abuild binutils autoconf pkgconfig \  
automake libtool git jpeg-dev libpng-dev tiff-dev zlib-dev && \  
apk add \--no-cache libstdc++ libgcc libgomp && \  
rm -rf /var/cache/apk/* /build  
  
ENTRYPOINT ["tesseract"]  
CMD ["-h"]  

