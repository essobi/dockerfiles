FROM alpine:3.7 as ffmpeg  
  
ENV VERSION n4.1-dev  
  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
curl \  
gnutls-dev lame-dev libvorbis-dev xvidcore-dev zlib-dev libvdpau-dev \  
imlib2-dev x264-dev libtheora-dev coreutils bzip2-dev perl-dev \  
libvpx-dev sdl2-dev libxfixes-dev libva-dev alsa-lib-dev \  
rtmpdump-dev v4l-utils-dev yasm opus-dev x265-dev libass-dev \  
libwebp-dev libxml2-dev  
  
RUN curl -sfL https://github.com/FFmpeg/FFmpeg/archive/$VERSION.tar.gz | tar
xz  
  
RUN cd FFmpeg-$VERSION && \  
./configure \  
--prefix=/usr/local \  
# --extra-cflags=-march=native \  
--enable-avisynth \  
--enable-avresample \  
--enable-avfilter \  
--enable-fontconfig \  
--enable-gnutls \  
--enable-gpl \  
--enable-libass \  
--enable-libmp3lame \  
--enable-librtmp \  
--enable-libvorbis \  
--enable-libvpx \  
--enable-libwebp \  
--enable-libxvid \  
--enable-libx264 \  
--enable-libx265 \  
--enable-libtheora \  
--enable-libv4l2 \  
--enable-postproc \  
--enable-pic \  
--enable-pthreads \  
--enable-shared \  
--enable-libxcb \  
--enable-libxml2 \  
--disable-debug \  
--disable-stripping \  
--disable-static \  
--enable-vaapi \  
--enable-vdpau \  
--enable-libopus && \  
make -j$(nproc) && \  
# make doc/ffmpeg.1 doc/ffplay.1 doc/ffserver.1 && \  
make install install-man  
  
###  
  
FROM alpine:3.7  
  
RUN apk add --no-cache --virtual .run-deps \  
gnutls lame libvorbis xvidcore zlib libvdpau \  
imlib2 x264-libs x265 libtheora perl \  
libvpx sdl2 libxfixes libva alsa-lib \  
rtmpdump v4l-utils opus libass libwebp libxml2  
  
ENTRYPOINT ["ffmpeg"]  
  
COPY --from=ffmpeg /usr/local /usr/local  

