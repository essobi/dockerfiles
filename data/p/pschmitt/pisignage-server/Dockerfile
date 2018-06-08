FROM node:latest  
  
# Install deps  
RUN apt-get update && \  
apt-get install -y autoconf automake build-essential libass-dev \  
libfreetype6-dev libsdl1.2-dev libtheora-dev libtool libva-dev \  
libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev \  
libxcb-xfixes0-dev pkg-config texi2html zlib1g-dev \  
yasm libx264-dev wget tar \  
imagemagick git  
  
# Install ffmpeg  
RUN mkdir "$HOME/ffmpeg_build" && cd "$HOME/ffmpeg_build" && \  
wget -O fdk-aac.tar.gz https://github.com/mstorsjo/fdk-aac/tarball/master && \  
tar xzvf fdk-aac.tar.gz && \  
cd mstorsjo-fdk-aac* && \  
autoreconf -fiv && \  
./configure --prefix="$HOME/ffmpeg_build" \--disable-shared && \  
make && \  
make install && \  
make distclean && \  
cd "$HOME/ffmpeg_build" && \  
wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \  
tar xjvf ffmpeg-snapshot.tar.bz2 && \  
cd ffmpeg && \  
export PATH="$HOME/bin:$PATH" && \  
export PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" && \  
./configure \  
\--prefix="$HOME/ffmpeg_build" \  
\--pkg-config-flags="--static" \  
\--extra-cflags="-I$HOME/ffmpeg_build/include" \  
\--extra-ldflags="-L$HOME/ffmpeg_build/lib" \  
\--bindir="$HOME/bin" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libx264 \  
\--enable-nonfree && \  
export PATH="$HOME/bin:$PATH" make && \  
make install && \  
make distclean && \  
hash -r && \  
ln -s "$HOME/bin/ffmpeg" /usr/local/bin/ffmpeg && \  
ln -s "$HOME/bin/ffprobe" /usr/local/bin/ffprobe  
  
# Install pisignage  
RUN git clone -b update-socketio https://github.com/pschmitt/pisignage-server
/usr/src/app && \  
cd /usr/src/app && \  
npm install  
  
# Clean up  
# RUN apt-get purge autoconf automake build-essential libass-dev \  
# libfreetype6-dev libsdl1.2-dev libtheora-dev libtool libva-dev \  
# libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev \  
# libxcb-xfixes0-dev pkg-config texi2html zlib1g-dev \  
# yasm libx264-dev wget tar git && \  
# rm -rf /var/lib/apt/lists/*  
# "$HOME/ffmpeg_build"  
EXPOSE 3000  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/media"]  
  
ENV MONGO_HOST=mongo MONGO_PORT=27017 MONGO_DB=pisignage-server  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
# VOLUME ["/usr/src/app/config/env/development.js"]  

