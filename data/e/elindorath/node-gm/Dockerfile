FROM elindorath/node  
MAINTAINER Joachim Westphal <joachim@sparted.com>  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache libgomp \  
&& apk add --no-cache -t build-dependencies \  
git \  
curl \  
make \  
gcc \  
g++ \  
linux-headers \  
# ----- 1  
&& mkdir -p /usr/local/src \  
  
# http://www.ijg.org/  
&& cd /usr/local/src \  
&& curl -L
https://github.com/Sparted/dependencies/blob/master/jpegsrc.v9b.tar.gz?raw=true
-o jpegsrc.v9b.tar.gz \  
&& tar -xzvf jpegsrc.v9b.tar.gz \  
&& cd jpeg-9b \  
&& ./configure --prefix=/usr/local/libjpeg-9b \  
&& make \  
&& make install \  
&& ln -s libjpeg-9b /usr/local/libjpeg \  
&& rm -rf \  
/usr/local/src/jpegsrc.v9b.tar.gz \  
/usr/local/src/jpeg-9b \  
  
# http://www.remotesensing.org/libtiff/  
&& cd /usr/local/src \  
&& curl -L
https://github.com/Sparted/dependencies/blob/master/tiff_4.0.6.orig.tar.gz?raw=true
-o tiff_4.0.6.orig.tar.gz \  
&& tar -xzvf tiff_4.0.6.orig.tar.gz \  
&& cd tiff-4.0.6 \  
&& ./configure --prefix=/usr/local/libtiff-4.0.6 \  
&& make \  
&& make install \  
&& ln -s libtiff-4.0.6 /usr/local/libtiff \  
&& rm -rf \  
/usr/local/src/tiff_4.0.6.orig.tar.gz \  
/usr/local/src/tiff-4.0.6 \  
  
# http://zlib.net/  
&& cd /usr/local/src \  
&& curl -L
https://github.com/Sparted/dependencies/blob/master/zlib-1.2.8.tar.gz?raw=true
-o zlib-1.2.8.tar.gz \  
&& tar -xzvf zlib-1.2.8.tar.gz \  
&& cd zlib-1.2.8 \  
&& ./configure --prefix=/usr/local/libz-1.2.8 \  
&& make \  
&& make install \  
&& ln -s libz-1.2.8 /usr/local/libz \  
&& rm -rf \  
/usr/local/src/zlib-1.2.8.tar.gz \  
/usr/local/src/zlib-1.2.8 \  
  
# http://www.libpng.org/pub/png/libpng.html  
&& cd /usr/local/src \  
&& curl -L
https://github.com/Sparted/dependencies/blob/master/libpng-1.6.23.tar.gz?raw=true
-o libpng-1.6.23.tar.gz \  
&& tar -xzvf libpng-1.6.23.tar.gz \  
&& cd libpng-1.6.23 \  
&& ./configure \  
\--prefix=/usr/local/libpng-1.6.23 \  
LDFLAGS="-L/usr/local/libz/lib" \  
CPPFLAGS="-I/usr/local/libz/include" \  
&& make \  
&& make install \  
&& ln -s libpng-1.6.23 /usr/local/libpng \  
&& rm -rf \  
/usr/local/src/libpng-1.6.23.tar.gz \  
/usr/local/src/libpng-1.6.23 \  
  
# GraphicsMagick  
&& cd /usr/local/src \  
&& curl -L
https://github.com/Sparted/dependencies/blob/master/GraphicsMagick-1.3.24.tar.gz?raw=true
-o GraphicsMagick-1.3.24.tar.gz \  
&& tar -xzvf GraphicsMagick-1.3.24.tar.gz \  
&& cd GraphicsMagick-1.3.24 \  
&& ./configure \  
LDFLAGS="-L/usr/local/libjpeg/lib -L/usr/local/libpng/lib
-L/usr/local/libz/lib -L/usr/local/libtiff/lib -L/usr/local/libwebp/lib" \  
CPPFLAGS="-I/usr/local/libjpeg/include -I/usr/local/libpng/include
-I/usr/local/libz/include -I/usr/local/libtiff/include
-I/usr/local/libwebp/include" \  
&& make \  
&& make install \  
&& make check \  
&& ln -s graphicsmagick-1.3.24 /usr/local/graphicsmagick \  
&& rm -rf \  
/usr/local/src/GraphicsMagick-1.3.24.tar.gz \  
/usr/local/src/GraphicsMagick-1.3.24 \  
  
# delete unnecessary packages  
&& apk del \  
build-dependencies  

