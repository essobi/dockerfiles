FROM yellowblackandwhite/alpine-flask  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
# ENV FFMPEG_VERSION=3.0  
# RUN apk add --update build-base gmp-dev g++ curl nasm tar git bzip2 sqlite
openssl \  
# opus speex x264 x265 libvpx libvorbis faac freetype libass libwebp rtmpdump
\  
# libtheora zlib yasm lame libogg zlib-dev yasm-dev lame-dev libogg-dev
x264-dev \  
# x265-dev libvpx-dev libvorbis-dev faac-dev freetype-dev libass-dev libwebp-
dev \  
# rtmpdump-dev libtheora-dev speex-dev opus-dev python3-dev sqlite-libs
sqlite-dev openssl-dev && \  
# DIR=$(mktemp -d) && cd ${DIR} && \  
# curl -s http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz | tar
zxvf - -C . && \  
# cd ffmpeg-${FFMPEG_VERSION} && \  
# ./configure \  
# \--enable-version3 --enable-gpl --enable-nonfree --enable-small --enable-
libmp3lame --enable-libx264 \  
# \--enable-libx265 --enable-libvpx --enable-libtheora --enable-libvorbis
--enable-libopus \  
# \--enable-libass --enable-libwebp --enable-librtmp --enable-postproc
--enable-avresample \  
# \--enable-libfaac --enable-libfreetype --enable-openssl --disable-debug
--enable-libspeex && \  
# make && make install && make distclean && rm -rf ${DIR} && \  
# apk del sqlite-dev openssl-dev opus-dev speex-dev x264-dev x265-dev libvpx-
dev \  
# libvorbis-dev faac-dev freetype-dev libass-dev libwebp-dev rtmpdump-dev \  
# libtheora-dev zlib-dev yasm-dev lame-dev libogg-dev  
  
RUN apk add --update ffmpeg  
USER alpine  

