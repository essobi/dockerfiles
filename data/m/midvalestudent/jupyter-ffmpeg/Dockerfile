FROM midvalestudent/jupyter-opencv:latest  
  
USER root  
ENV HOME=/root/  
  
# Download/build/install ffmpeg  
ARG FFMPEG_VERSION  
ENV FFMPEG_VERSION ${FFMPEG_VERSION:-"3.2"}  
RUN DEBIAN_FRONTEND=noninteractive \  
&& REPO=http://www.deb-multimedia.org \  
&& echo "deb $REPO jessie main non-free\ndeb-src $REPO jessie main non-free"
>> /etc/apt/sources.list \  
&& apt-get update && apt-get install -y --force-yes deb-multimedia-keyring &&
apt-get update \  
&& apt-get remove ffmpeg \  
&& apt-get install -yq --no-install-recommends \  
build-essential \  
libmp3lame-dev \  
libvorbis-dev \  
libtheora-dev \  
libspeex-dev \  
yasm \  
pkg-config \  
libfaac-dev \  
libopenjpeg-dev \  
libx264-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/build && cd /usr/src/build \  
&& wget http://ffmpeg.org/releases/ffmpeg-$FFMPEG_VERSION.tar.gz \  
&& tar xzf ffmpeg-$FFMPEG_VERSION.tar.gz && cd ffmpeg-$FFMPEG_VERSION \  
&& ./configure \  
\--enable-gpl \  
\--enable-postproc \  
\--enable-swscale \  
\--enable-avfilter \  
\--enable-libmp3lame \  
\--enable-libvorbis \  
\--enable-libtheora \  
\--enable-libx264 \  
\--enable-libspeex \  
\--enable-shared \  
\--enable-pthreads \  
\--enable-libopenjpeg \  
\--enable-nonfree \  
&& make -j4 install && ldconfig \  
&& cd /usr/src/build && rm -rf ffmpeg-$FFMPEG_VERSION* \  
&& apt-get purge -y cmake && apt-get autoremove -y --purge  
  
# back to unprivilged user  
ENV HOME=/home/$NB_USER/  

