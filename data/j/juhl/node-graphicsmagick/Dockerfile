FROM node:10-alpine  
MAINTAINER danieljuhl  
  
# Build tools for native dependencies  
RUN apk add \--update make gcc g++ python git  
  
ENV PKGVER=1.3.29  
ENV PKGNAME=GraphicsMagick  
ENV PKGSLUG=graphicsmagick  
ENV
PKGSOURCE=http://downloads.sourceforge.net/$PKGSLUG/$PKGSLUG/$PKGVER/$PKGNAME-$PKGVER.tar.lz  
  
# Install dependencies and install graphicsmagick from source  
RUN apk add \--update lzip \  
wget \  
ffmpeg \  
libjpeg-turbo-dev \  
libpng-dev \  
libtool \  
libgomp \  
pdftk \  
ghostscript \  
ghostscript-fonts && \  
wget $PKGSOURCE && \  
lzip -d -c $PKGNAME-$PKGVER.tar.lz | tar -xvf - && \  
cd $PKGNAME-$PKGVER && \  
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
\--with-gs-font-dir=/usr/share/fonts/Type1 \  
\--with-quantum-depth=16 && \  
make && \  
make install && \  
cd / && \  
rm -rf $PKGNAME-$PKGVER && \  
rm $PKGNAME-$PKGVER.tar.lz  

