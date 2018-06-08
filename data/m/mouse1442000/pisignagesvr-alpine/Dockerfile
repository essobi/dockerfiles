FROM node:8-alpine  
  
# Install Dependencies  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories; \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories;  
  
RUN apk update  
  
RUN apk add --no-cache \  
autoconf \  
automake \  
build-base \  
libass-dev \  
freetype-dev \  
libtheora-dev \  
libtool \  
libva-dev \  
libvdpau-dev \  
libvorbis-dev \  
yasm \  
wget \  
tar \  
imagemagick \  
git \  
ffmpeg-libs \  
x264-dev \  
ca-certificates \  
curl \  
gnupg \  
libressl \  
pkgconfig \  
libc6-compat  
  
#NOT FOUND YET:  
#libsdl1.2-dev  
#libxcb1-dev  
#libxcb-shm0-dev  
#libxcb-xfixes0-dev  
#pkg-config - no '-'  
#texi2html - replaced with ffmpeg-libs  
#libx264-dev - drop the lib!  
RUN git clone -b update-socketio https://github.com/pschmitt/pisignage-server
/usr/src/app && \  
cd /usr/src/app  
  
RUN node -v  
  
RUN npm -v  
  
EXPOSE 3000  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/media"]  

