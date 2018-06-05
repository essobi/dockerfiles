FROM ubuntu  
MAINTAINER Konstantin Wilms <kon@geopacket.com>  
  
ENV LIBVPX_VER 1.3.0  
RUN sudo apt-get update  
  
RUN sudo apt-get -y install unzip git wget autoconf automake build-essential
libass-dev libfreetype6-dev libgpac-dev \  
libtheora-dev libtool libvorbis-dev libxfixes-dev pkg-config texi2html
zlib1g-dev  
  
# yasm  
RUN sudo apt-get install yasm  
  
# x264  
RUN wget http://download.videolan.org/pub/x264/snapshots/last_x264.tar.bz2  
RUN tar xjvf last_x264.tar.bz2  
RUN cd /x264-snapshot* && ./configure --prefix="/ffmpeg_build"
\--bindir="/bin" \--enable-static  
RUN cd /x264-snapshot* && make && make install && make distclean  
  
# libfdk-aac  
RUN wget -O fdk-aac.zip https://github.com/mstorsjo/fdk-aac/zipball/master &&
unzip fdk-aac.zip  
RUN cd mstorsjo-fdk-aac* && autoreconf -fiv && ./configure
--prefix="/ffmpeg_build" \--disable-shared  
RUN cd mstorsjo-fdk-aac* && make && make install && make distclean  
  
# libmp3lame  
RUN apt-get install -y libmp3lame-dev  
  
# libopus  
RUN apt-get install -y libopus-dev  
  
# libvpx  
RUN wget http://webm.googlecode.com/files/libvpx-v${LIBVPX_VER}.tar.bz2 && tar
xjvf libvpx-v${LIBVPX_VER}.tar.bz2  
RUN cd libvpx-v${LIBVPX_VER} && ./configure --prefix="/ffmpeg_build"
\--disable-examples  
RUN cd libvpx-v${LIBVPX_VER} && make && make install && make clean  
  
# ffmpeg  
RUN wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && tar xjvf
ffmpeg-snapshot.tar.bz2  
RUN PKG_CONFIG_PATH="/ffmpeg_build/lib/pkgconfig" && export PKG_CONFIG_PATH  
RUN cd ffmpeg && ./configure --prefix="/ffmpeg_build" \--extra-
cflags="-I/ffmpeg_build/include" \  
\--extra-ldflags="-L/ffmpeg_build/lib" \--bindir="/bin" \--extra-libs="-ldl"
\--enable-gpl \  
\--enable-libass --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame
--enable-libopus \  
\--enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264
--enable-nonfree  
RUN cd ffmpeg && make && make install && make distclean && hash -r  

