# The Alpine Linux with preinstalled Node.js  
FROM node:8-alpine  
  
ENV PKGNAME=graphicsmagick  
ENV PKGVER=1.3.28  
ENV
PKGSOURCE=http://downloads.sourceforge.net/$PKGNAME/$PKGNAME/$PKGVER/GraphicsMagick-$PKGVER.tar.lz  
ENV JBIG_REPO=https://github.com/nu774/jbigkit.git  
  
#  
# Installing graphicsmagick dependencies  
RUN apk add --no-cache --update g++ \  
gcc \  
make \  
automake \  
autoconf \  
git \  
lzip \  
wget \  
libjpeg-turbo-dev \  
lcms2-dev \  
libwmf-dev \  
jasper-dev \  
libx11-dev \  
libpng-dev \  
libtool \  
libwebp-dev \  
jasper-dev \  
bzip2-dev \  
libxml2-dev \  
tiff-dev \  
exiftool \  
freetype-dev \  
libgomp && \  
git clone $JBIG_REPO && \  
cd ./jbigkit && ls -la && \  
autoreconf -ivf && automake --add-missing && \  
./configure && \  
make install && \  
cd / && \  
rm -rf ./jbigkit && \  
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
\--with-webp=yes \  
\--with-bzip=yes \  
\--with-tiff=yes \  
\--with-freetype=yes \  
\--with-jpeg=yes \  
\--with-jp2=yes \  
\--with-cms2=yes \  
\--with-xml=yes \  
\--with-x11=yes \  
\--with-wmf=yes \  
\--with-gs-font-dir=/usr/share/fonts/Type1 \  
\--with-quantum-depth=16 && \  
make && \  
make install && \  
cd / && \  
rm -rf GraphicsMagick-$PKGVER && \  
rm GraphicsMagick-$PKGVER.tar.lz && \  
apk del g++ \  
gcc \  
make \  
automake \  
autoconf \  
git \  
lzip \  
wget  
  
CMD [ "/bin/sh" ]  
  

