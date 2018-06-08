FROM ubuntu:xenial  
MAINTAINER Daniel Floris <daniel.floris@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
# dependencies  
autoconf automake build-essential \  
# LIbs  
libass-dev \  
libfreetype6-dev \  
libtheora-dev \  
libtool \  
libvorbis-dev \  
# Packages  
pkg-config \  
texinfo \  
zlib1g-dev \  
libx264-dev \  
libx265-dev \  
libvpx-dev \  
yasm  
# Note: Server users can omit the ffplay and x11grab dependencies: libsdl2-dev
libva-dev libvdpau-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev.  
RUN mkdir /root/ffmpeg_sources  
WORKDIR /root/ffmpeg_sources  
COPY ThetaS_remap_files/ /  
COPY ffmpeg-snapshot.tar.bz2 /root/ffmpeg_sources  
  
RUN tar xjvf ffmpeg-snapshot.tar.bz2  
  
WORKDIR /root/ffmpeg_sources/ffmpeg  
  
RUN PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig"
./configure \  
\--prefix="$HOME/ffmpeg_build" \  
\--pkg-config-flags="--static" \  
\--extra-cflags="-I$HOME/ffmpeg_build/include" \  
\--extra-ldflags="-L$HOME/ffmpeg_build/lib" \  
\--bindir="$HOME/bin" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfreetype \  
# --enable-libfdk-aac \  
# --enable-libmp3lame \  
# --enable-libopus \  
# --enable-libtheora \  
# --enable-libvorbis \  
# --enable-libvpx \  
# --enable-libx264 \  
# --enable-remap \  
# --enable-libx265 \  
\--enable-nonfree && \  
PATH="$HOME/bin:$PATH" make && \  
make install && \  
hash -r  

