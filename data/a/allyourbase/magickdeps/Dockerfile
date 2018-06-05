# Start with Debian Jessie  
FROM debian:jessie-slim  
  
MAINTAINER Jamin Kortegard <jamink919@gmail.com>  
  
# Get basic utils  
RUN apt-get -y update && apt-get -y install --no-install-recommends \  
apt-utils \  
&& apt-get -y install --no-install-recommends \  
bzip2 \  
ca-certificates \  
curl \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dependencies for ImageMagick/GraphicsMagick.  
RUN apt-get -y update && apt-get -y install --no-install-recommends \  
dcraw \  
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
  
# Compilers for Ghostscript and GraphicsMagick/ImageMagick.  
# This will be wasted layer space afterwards. How to optimize?  
RUN apt-get -y update && apt-get -y install --no-install-recommends \  
autoconf \  
automake \  
build-essential \  
libx11-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install specific Ghostscript 9.19  
ENV GS_VER 9.19  
  
RUN cd /tmp \  
&& curl -L -O https://github.com/ArtifexSoftware/ghostpdl-
downloads/releases/download/gs919/ghostscript-${GS_VER}.tar.gz \  
&& tar -xzf ghostscript-${GS_VER}.tar.gz \  
&& cd ghostscript-${GS_VER} \  
&& ./configure \  
&& make && make install && make clean \  
&& ldconfig \  
&& cd /tmp \  
&& rm -rf ghostscript-${GS_VER}*  
  
# add Git SHA label to image build  
ARG GIT_COMMIT=unknown  
LABEL org.label-schema.vcs-ref=$GIT_COMMIT  

