FROM node:6.11.5-alpine  
  
ENV PKGNAME=graphicsmagick  
ENV PKGVER=1.3.25  
ENV
PKGSOURCE=http://downloads.sourceforge.net/$PKGNAME/$PKGNAME/$PKGVER/GraphicsMagick-$PKGVER.tar.lz  
  
RUN apk add --update g++ \  
gcc \  
make \  
lzip \  
wget \  
freetype-dev \  
tiff-dev \  
libxml2-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libtool \  
libgomp \  
\--repository http://nl.alpinelinux.org/alpine/v3.4/main/ && \  
wget $PKGSOURCE --no-check-certificate && \  
lzip -d -c GraphicsMagick-$PKGVER.tar.lz | tar -xvf - && \  
cd GraphicsMagick-$PKGVER && \  
./configure \  
\--build=$CBUILD \  
\--host=$CHOST \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--mandir=/usr/share/man \  
\--infodir=/usr/share/info \  
\--localstatedir=/var \  
\--enable-shared \  
\--disable-static \  
\--with-modules \  
\--with-threads \  
\--with-quantum-depth=16 && \  
make && \  
make install && \  
cd ../ && \  
rm -rf GraphicsMagick-$PKGVER && \  
rm GraphicsMagick-$PKGVER.tar.lz && \  
apk del g++ \  
gcc \  
make \  
lzip \  
wget  

