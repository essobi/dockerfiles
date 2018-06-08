FROM ruby:2.0.0-slim  
  
MAINTAINER Tim Davies <tim@eljetico.co.uk>  
  
# Create temp dir for installations  
WORKDIR /tmp/install  
  
# Install specific versions  
ENV GS_VER 9.15  
ENV MAGICK_VER 6.8.9-10  
# Get basic utils  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
bzip2 \  
ca-certificates \  
curl \  
wget \  
dcraw \  
autoconf \  
automake \  
build-essential \  
libx11-dev \  
libfreetype6 \  
libfreetype6-dev \  
libgif4 \  
libgif-dev \  
libjasper1 \  
libjasper-dev \  
libturbojpeg1 \  
libturbojpeg1-dev \  
liblcms2-2 \  
liblcms2-dev \  
# libperl-dev \  
libpng12-0 \  
libpng12-dev \  
libtiff5 \  
libtiff5-dev \  
libwmf0.2-7 \  
libwmf-dev \  
libxml2 \  
libxml2-dev \  
zlib1g \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L -O http://downloads.ghostscript.com/public/old-gs-
releases/ghostscript-${GS_VER}.tar.gz \  
&& tar -xzf ghostscript-${GS_VER}.tar.gz\  
&& cd ghostscript-${GS_VER} \  
&& ./configure \  
&& make \  
&& make install \  
&& make clean \  
&& ldconfig \  
&& cd /tmp/install \  
&& rm -rf ghostscript-${GS_VER}* \  
&& curl -L -O
http://www.imagemagick.org/download/releases/ImageMagick-${MAGICK_VER}.tar.xz
\  
&& tar -xf ImageMagick-${MAGICK_VER}.tar.xz \  
&& cd ImageMagick-${MAGICK_VER} \  
&& ./configure --enable-shared --with-gslib --with-wmf --without-x --with-xml
\  
\--with-freetype --with-fontconfig --with-quantum-depth=8 \--with-perl=no \  
&& make \  
&& make install \  
&& make clean \  
&& ldconfig \  
&& cd /tmp/install \  
&& rm -rf ImageMagick-${MAGICK_VER}* \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY policy.xml /usr/local/etc/ImageMagick-6/policy.xml  
  
WORKDIR /  
  
RUN rm -rf /tmp/install  
  
CMD ["convert", "--version"]  

