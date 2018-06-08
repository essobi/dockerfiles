# Forked from  
# eljetico/ruby-imagemagick  
FROM ruby:2.3.1  
  
LABEL maintainer="Ken Greeff <ken@kengreeff.com>"  
# Create temp dir for installations  
WORKDIR /tmp/install  
  
# Install specific versions  
ENV GS_VER 9.16  
ENV MAGICK_VER 6.9.5-10  
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
libpng12-0 \  
libpng12-dev \  
libtiff5 \  
libtiff5-dev \  
libwmf0.2-7 \  
libwmf-dev \  
libxml2 \  
libxml2-dev \  
sudo \  
zip \  
zlib1g \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add docker user to sudo group  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN sudo apt-get update && sudo apt-get install yarn  
  
# Install Ghostscript  
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
  
WORKDIR /  
  
# Remove temp directory  
RUN rm -rf /tmp/install  
  
CMD ["gs", "-v"]

