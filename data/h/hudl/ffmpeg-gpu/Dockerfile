FROM nvidia/cuda:8.0-cudnn5-devel  
MAINTAINER Ryan Versaw <ryan.versaw@hudl.com>  
  
RUN apt-get update -y && \  
apt-get install -y git wget vim libgtk2.0-0 cmake subversion yasm unzip
mediainfo ntp \  
ruby autoconf automake build-essential curl pkg-config texi2html \  
zlib1g-dev libvpx-dev libmp3lame-dev libxvidcore-dev libxml2-utils \  
libass-dev libgpac-dev libtheora-dev libtool libvorbis-dev bzip2 \  
make gcc libtool nasm libx264-dev mercurial libopus-dev libfreetype6-dev  
  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
  
RUN export LD_LIBRARY_PATH=/usr/local/lib/ && \  
echo /usr/local/lib > /etc/ld.so.conf.d/custom-libs.conf && \  
ldconfig  
  
RUN hg clone https://bitbucket.org/multicoreware/x265 && \  
cd x265/build/linux && \  
PATH="$HOME/bin:$PATH" cmake -G "Unix Makefiles" \  
../../source && \  
make -j8 && make install && \  
ldconfig && \  
cd ../../../ && \  
rm -rf x265  
  
RUN curl -L http://downloads.sourceforge.net/project/opencore-amr/opencore-
amr/opencore-amr-0.1.4.tar.gz | tar zxf - && \  
cd opencore-amr-0.1.4 && \  
./configure && \  
make -j8 && make install && \  
ldconfig && \  
cd .. && \  
rm -rf opencore-amr-0.1.4  
  
RUN curl -L https://github.com/mstorsjo/fdk-aac/archive/v0.1.5.tar.gz | tar
zxf - && \  
cd fdk-aac-0.1.5 && \  
autoreconf -fiv && \  
./configure && \  
make -j8 && make install && \  
ldconfig && \  
cd .. && \  
rm -rf fdk-aac-0.1.5  
  
RUN curl -L http://ffmpeg.org/releases/ffmpeg-3.3.2.tar.bz2 | tar xjf - && \  
cd ffmpeg-3.3.2 && \  
./configure --enable-avfilter --enable-version3 --enable-libopencore-amrnb
--enable-libopencore-amrwb \  
\--enable-libvpx --enable-libfdk-aac --enable-libmp3lame --enable-libtheora
--enable-libvorbis \  
\--enable-libx264 --enable-libxvid --enable-gpl --enable-postproc --enable-
nonfree --enable-shared \  
\--enable-libx265 --enable-libopus --enable-libass --enable-libfreetype
--enable-nvenc \  
\--enable-cuda --enable-cuvid --extra-cflags=-I/usr/local/cuda/include \  
\--extra-cflags=-I/usr/local/include --extra-ldflags=-L/usr/local/cuda/lib64 \  
\--enable-libnpp && \  
make -j8 && make install && \  
ldconfig && \  
cd tools && \  
make qt-faststart && \  
cp qt-faststart /usr/local/bin && \  
ldconfig && \  
cd ../.. && \  
rm -rf ffmpeg-3.3.2  
  
RUN curl -L http://www.sno.phy.queensu.ca/~phil/exiftool/Image-
ExifTool-10.46.tar.gz | tar zxf - && \  
cd Image-ExifTool-10.46 && \  
perl Makefile.PL && \  
make -j8 && make install && \  
cd .. && \  
rm -rf Image-ExifTool-10.46  
  
ENTRYPOINT ["ffmpeg"]

