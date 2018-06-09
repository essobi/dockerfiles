FROM debian:jessie  
MAINTAINER Robin Speekenbrink <docker@kingsquare.nl>  
  
ENV PATH="$PATH:/usr/src/tools/bin" CCPREFIX="/usr/src/tools/bin/arm-linux-
gnueabihf-" BUILD_ARCH=arm-linux-gnueabihf BUILD_PREFIX=/opt/ffmpeg  
  
ENV BUILD_DEPS \  
git-core \  
autoconf \  
automake \  
binutils \  
bison \  
build-essential \  
curl \  
flex \  
gawk \  
gperf \  
libncurses5-dev \  
libtool \  
libtool-bin \  
texinfo \  
tmux \  
unzip \  
yasm \  
help2man  
  
RUN apt-get update \  
&& apt-get install -y $BUILD_DEPS \  
&& rm -rf /var/lib/apt/lists/* \  
# GET THE COMPILER  
&& mkdir -p /usr/src \  
&& git clone \--depth=1 https://github.com/raspberrypi/tools /usr/src/raspain
\  
&& mv /usr/src/raspain/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64
/usr/src/tools \  
# build FDK AAC  
&& git clone \--depth=1 https://github.com/mstorsjo/fdk-aac.git /usr/src/fdk-
aac \  
&& cd /usr/src/fdk-aac \  
&& ./autogen.sh \  
&& ./configure \--host=${BUILD_ARCH} \--prefix=${BUILD_PREFIX} \--enable-
shared \--enable-static \  
&& make -j6 \  
&& make install \  
# build ALSA  
&& curl -s ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.1.0.tar.bz2 | tar -jx
-C /usr/src \  
&& cd /usr/src/alsa-lib-1.1.0 \  
&& ./configure \--host=${BUILD_ARCH} \--prefix=${BUILD_PREFIX} \  
&& make -j6 \  
&& make install \  
# build x264  
&& git clone \--depth=1 http://git.videolan.org/git/x264.git /usr/src/x264 \  
&& cd /usr/src/x264 \  
&& ./configure \--host=${BUILD_ARCH} \--enable-static \--cross-
prefix=${CCPREFIX} \--prefix=${BUILD_PREFIX} \--extra-cflags='-march=armv7-a
-mfpu=neon-vfpv4' \--extra-ldflags='-march=armv7-a' \  
&& make -j6 \  
&& make install \  
# build LAME mp3  
&& curl -Ls
"http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz" |
tar -zx -C /usr/src \  
&& cd /usr/src/lame-3.99.5 \  
&& CC=${CCPREFIX}gcc CFLAGS="-march=armv7-a -mfpu=neon-vfpv4" ./configure
\--host=${BUILD_ARCH} \--enable-static \--prefix=${BUILD_PREFIX} \  
&& make -j6 \  
&& make install \  
# build ffmpeg  
&& curl -Ls "https://github.com/FFmpeg/FFmpeg/archive/n3.2.tar.gz" | tar -zx
-C /usr/src \  
&& cd /usr/src/FFmpeg-n3.2 \  
&& PKG_CONFIG_PATH=${BUILD_PREFIX}/lib/pkgconfig ./configure \--enable-cross-
compile \--cross-prefix=${CCPREFIX} \--arch=armhf \--target-os=linux
\--prefix=${BUILD_PREFIX} \--enable-gpl \--enable-nonfree \--enable-libx264
\--enable-nonfree \--enable-libfdk-aac \--enable-libmp3lame \--extra-
cflags="-I${BUILD_PREFIX}/include" \--extra-ldflags="-L${BUILD_PREFIX}/lib"
\--enable-static \--pkg-config-flags="--static" \--extra-libs=-ldl \  
&& make -j6 \  
&& make install \  
&& rm -rfR /usr/src/* /tmp/* /opt/ffmpeg/ffprobe /opt/ffmpeg/ffserver \  
&& apt-get purge -y \--auto-remove $BUILD_DEPS gcc-4.8-base  
  
WORKDIR /opt/ffmpeg  
VOLUME /opt/ffmpeg

