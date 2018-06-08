FROM ubuntu:16.04  
ARG webp_version="0.6.0"  
ARG ffmpeg_version="3.2.4"  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:mc3man/xerus-media  
RUN apt-get update && apt-get install -y \  
wget \  
gcc \  
make \  
cmake \  
libass-dev \  
libfdk-aac-dev \  
libfreetype6-dev \  
libgnutls-dev \  
libmp3lame-dev \  
libnuma-dev \  
libopus-dev \  
libtheora-dev \  
libtool \  
libvorbis-dev \  
libvpx-dev \  
libx264-dev \  
libx265-dev \  
texi2html \  
yasm \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# webp build  
RUN wget
https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${webp_version}.tar.gz
-O /tmp/libwebp-${webp_version}.tar.gz  
WORKDIR /tmp  
RUN tar -xzf /tmp/libwebp-${webp_version}.tar.gz  
WORKDIR /tmp/libwebp-${webp_version}  
RUN ./configure && make && make install && ldconfig  
  
# ffmpeg build  
RUN wget https://ffmpeg.org/releases/ffmpeg-${ffmpeg_version}.tar.gz -O
/tmp/ffmpeg-${ffmpeg_version}.tar.gz  
WORKDIR /tmp  
RUN tar -xzf /tmp/ffmpeg-${ffmpeg_version}.tar.gz  
WORKDIR /tmp/ffmpeg-${ffmpeg_version}  
RUN ./configure \  
\--pkg-config-flags="--static --libs-only-l gnutls" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libmp3lame \  
\--enable-libopus \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libvpx \  
\--enable-gnutls \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-libwebp \  
\--enable-nonfree \  
&& make -j 4 \  
&& make install \  
&& make distclean \  
&& ldconfig  
  
# clean up /tmp  
WORKDIR /tmp  
RUN rm -rf *  

