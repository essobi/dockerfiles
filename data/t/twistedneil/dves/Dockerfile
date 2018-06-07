From debian:jessie-slim  
  
MAINTAINER TwistTheNeil  
  
ENV FFMPEG_REPO https://github.com/FFmpeg/FFmpeg.git  
ENV FFMPEG_HASH 148c4fb8d203fdef8589ccef56a995724938918b  
ENV FFMS2_REPO https://github.com/FFMS/ffms2.git  
ENV FFMS2_HASH 2cf2c4b8961c7b1bb2466e5f3305ed2d6bdbe8ef  
ENV ZIMG_REPO https://github.com/sekrit-twc/zimg.git  
ENV ZIMG_HASH a93132a03ded2d3e37ba3a9d64780c2d491c1d5e  
ENV NASM_REPO git://repo.or.cz/nasm.git  
ENV NASM_HASH 7bde33431fe09a4246fb65fef47825a74d7cb3ce  
ENV x264_REPO git://git.videolan.org/x264.git  
  
RUN apt-get update && apt-get -y install autoconf automake build-essential \  
libfreetype6-dev libtool \  
libvdpau-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev \  
pkg-config texinfo zlib1g-dev git  
  
RUN git clone ${NASM_REPO} && cd nasm && \  
git checkout ${NASM_HASH} && \  
./autogen.sh && ./configure --prefix=/usr && make && \  
make install || stat /usr/bin/nasm  
  
RUN git clone ${x264_REPO} && cd x264 && \  
./configure --enable-shared --disable-opencl && \  
make && make install && ldconfig  
  
RUN git clone ${FFMPEG_REPO} && cd FFmpeg && \  
git checkout ${FFMPEG_HASH} && \  
./configure \  
\--prefix=/usr \  
\--extra-version=1 \  
\--toolchain=hardened \  
\--libdir=/usr/lib/x86_64-linux-gnu \  
\--incdir=/usr/include/x86_64-linux-gnu \  
\--enable-gpl \  
\--disable-stripping \  
\--enable-avresample \  
\--enable-avisynth \  
\--enable-libx264 \  
\--enable-libfreetype \  
\--enable-shared && \  
make && make install && hash -r  
  
RUN git clone ${FFMS2_REPO} && cd ffms2 && \  
git checkout ${FFMS2_HASH} && \  
./configure && make && make install && ldconfig  
  
RUN git clone ${ZIMG_REPO} && cd zimg && \  
git checkout ${ZIMG_HASH} && \  
./autogen.sh && ./configure && make && make install  

