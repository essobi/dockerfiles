# Dockerfile for minimal ffmpeg based on alpine  
FROM gliderlabs/alpine:3.4  
MAINTAINER Fred Park <https://github.com/alfpark/docker-ffmpeg>  
  
# install base  
RUN apk add \--update \--no-cache \  
musl coreutils build-base nasm ca-certificates curl tar \  
openssl-dev zlib-dev yasm-dev lame-dev freetype-dev opus-dev \  
rtmpdump-dev x264-dev x265-dev xvidcore-dev libass-dev libwebp-dev \  
libvorbis-dev libogg-dev libtheora-dev libvpx-dev \  
# build and install ffmpeg  
&& FFMPEG_VER=3.2.1 \  
&& curl -s http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VER}.tar.gz | tar zxvf -
-C . \  
&& cd ffmpeg-${FFMPEG_VER} \  
&& ./configure \  
\--disable-debug \--enable-version3 \--enable-small \--enable-gpl \  
\--enable-nonfree \--enable-postproc \--enable-openssl \  
\--enable-avresample \--enable-libfreetype \--enable-libmp3lame \  
\--enable-libx264 \--enable-libx265 \--enable-libopus \--enable-libass \  
\--enable-libwebp \--enable-librtmp \--enable-libtheora \  
\--enable-libvorbis \--enable-libvpx \--enable-libxvid \  
&& make -j"$(nproc)" install \  
&& cd .. \  
&& rm -rf ffmpeg-${FFMPEG_VER} \  
# cleanup  
&& apk del \--purge \  
coreutils build-base nasm curl tar openssl-dev zlib-dev yasm-dev \  
lame-dev freetype-dev opus-dev xvidcore-dev libass-dev libwebp-dev \  
libvorbis-dev libogg-dev libtheora-dev libvpx-dev \  
&& apk add \--no-cache \  
zlib lame freetype faac opus xvidcore libass libwebp libvorbis libogg \  
libtheora libvpx \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["ffmpeg"]  

