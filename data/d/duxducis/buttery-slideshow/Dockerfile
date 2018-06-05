FROM debian:jessie  
  
VOLUME /work  
VOLUME /src  
  
# Add non-free for libfaac  
RUN sed -i "s/jessie main/jessie main non-free/" /etc/apt/sources.list  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
python3 \  
python3-pip \  
sox \  
imagemagick \  
gawk \  
autoconf \  
automake \  
build-essential \  
libass-dev \  
libfreetype6-dev \  
libtheora-dev \  
libtool \  
libvorbis-dev \  
pkg-config \  
texi2html \  
zlib1g-dev \  
wget \  
yasm \  
libx264-dev \  
libfaac-dev  
  
RUN mkdir ~/ffmpeg_sources  
  
RUN cd ~/ffmpeg_sources && \  
wget http://download.videolan.org/pub/x264/snapshots/last_x264.tar.bz2 && \  
tar xjvf last_x264.tar.bz2 && \  
cd x264-snapshot* && \  
PATH="$HOME/bin:$PATH" ./configure --prefix="$HOME/ffmpeg_build"
\--bindir="$HOME/bin" \--enable-static && \  
PATH="$HOME/bin:$PATH" make && \  
make install && \  
make distclean  
  
RUN cd ~/ffmpeg_sources && \  
wget -O fdk-aac.tar.gz https://github.com/mstorsjo/fdk-aac/tarball/master && \  
tar xzvf fdk-aac.tar.gz && \  
cd mstorsjo-fdk-aac* && \  
autoreconf -fiv && \  
./configure --prefix="$HOME/ffmpeg_build" \--disable-shared && \  
make && \  
make install && \  
make distclean  
  
RUN cd ~/ffmpeg_sources && \  
wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \  
tar xjvf ffmpeg-snapshot.tar.bz2 && \  
cd ffmpeg && \  
PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig"
./configure \  
\--prefix="$HOME/ffmpeg_build" \  
\--pkg-config-flags="--static" \  
\--extra-cflags="-I$HOME/ffmpeg_build/include" \  
\--extra-ldflags="-L$HOME/ffmpeg_build/lib" \  
\--bindir="$HOME/bin" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfaac \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libx264 \  
\--enable-nonfree && \  
PATH="$HOME/bin:$PATH" make && \  
make install && \  
make distclean && \  
hash -r  
  
RUN pip3 install \  
pyyaml \  
Pillow  
  
# Add /root/bin to path for ffmpeg  
ENV PATH /root/bin:$PATH  
  
ADD src/buttery_slideshow.py /src/  
RUN ln -s /src/buttery_slideshow.py /usr/local/bin/buttery_slideshow && chmod
+x /src/buttery_slideshow.py  
  
COPY fonts /fonts  
  
COPY diascope-0.2.1d/ /tmp/diascope  
RUN cd /tmp/diascope && /bin/bash install.sh && rm -rf /tmp/diascope  
  

