FROM ruby:2.4.2-slim-stretch  
MAINTAINER Klaus Badelt <klaus@filmhub.com>  
# Kinonation base container  
# Contains all dependencies of Kinonation apps including os, packages, ffmpeg,
melt  
# might need at runtime also: libsqlite3-0 libxslt1.1 [libxslt1-dev]  
  
ENV FFMPEG_VERSION=3.4 \  
YASM_VERSION=1.3.0 \  
X264_VERSION=20171015-2245-stable \  
LAME_VERSION=3.100 \  
LAME_FOLDER_VERSION=3.100 \  
FDKAAC_VERSION=e2e35b82738dc9d5e5229477d49d557cadad4dc7 \  
MLT_VERSION=6.4.1 \  
MEDIAINFO_VERSION=0.7.99 \  
LIBZEN0_VERSION=0.4.37 \  
NODE_VERSION=8.x \  
PREFIX=/usr/local  
  
COPY 99-timeout.apt.conf /etc/apt/apt.conf.d/99-timeout  
COPY bashrc /root/.bashrc  
ENV TERM linux  
  
# @see http://redsymbol.net/articles/unofficial-bash-strict-mode/  
RUN set -eux \  
# setup build environment  
&& BUILD_DEPS="apt-utils g++ gcc libc-dev libtool pkg-config git make xz-utils
curl gnupg2" \  
&& APP_RUNTIME_DEPS="imagemagick libicu57 libpq5 bash-completion less" \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -qq upgrade -y \  
&& apt-get -qq autoremove -y \  
&& apt-get -qq install -y \--no-install-recommends $APP_RUNTIME_DEPS
$BUILD_DEPS \  
&& MAKEFLAGS="-j$[$(nproc) + 1]" \  
&& PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig" \  
&& TMP_DIR=$(mktemp -d) && cd $TMP_DIR \  
#  
# node  
#  
# install from package  
&& curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | bash - \  
&& apt-get install -y nodejs \  
#  
# FFmpeg  
#  
&& FFMPEG_RUNTIME_DEPS="libass5" \  
&& FFMPEG_BUILD_DEPS=" \  
autoconf \  
automake \  
cmake \  
libass-dev \  
nasm \  
python \  
texinfo \  
zlib1g-dev \  
" \  
&& apt-get -qq install -y \--no-install-recommends $FFMPEG_RUNTIME_DEPS
$FFMPEG_BUILD_DEPS \  
#  
# yasm  
#  
&& curl \--retry 5 -Ls
https://github.com/yasm/yasm/archive/v${YASM_VERSION}.tar.gz | tar zxf - -C
$TMP_DIR \  
&& cd $TMP_DIR/yasm* \  
&& ./autogen.sh \--prefix=$PREFIX \--bindir=$PREFIX/bin \--docdir=$TMP_DIR
\--mandir=$TMP_DIR \  
&& make \  
&& make install \  
#  
# x264  
#  
&& curl \--retry 5 -Ls
http://download.videolan.org/pub/x264/snapshots/x264-snapshot-${X264_VERSION}.tar.bz2
| tar -jxf - -C $TMP_DIR \  
&& cd $TMP_DIR/x264* \  
&& ./configure \--prefix=$PREFIX \--bindir=$PREFIX/bin \--disable-opencl
\--enable-shared \  
&& make \  
&& make install \  
#  
# libmp3lame  
#  
&& curl \--retry 5 -Ls
https://sourceforge.net/projects/lame/files/lame/${LAME_FOLDER_VERSION}/lame-${LAME_VERSION}.tar.gz/download
| tar zxf - -C $TMP_DIR \  
&& cd $TMP_DIR/lame* \  
&& ./configure \--prefix=$PREFIX \--bindir=$PREFIX/bin \--enable-nasm
\--datadir=$TMP_DIR \--enable-shared \--disable-static \  
&& make \  
&& make install \  
#  
# fdk-aac  
#  
&& curl \--retry 5 -Ls https://github.com/mstorsjo/fdk-
aac/archive/${FDKAAC_VERSION}.tar.gz | tar zxf - -C $TMP_DIR \  
&& cd $TMP_DIR/fdk-aac* \  
&& autoreconf -fiv \  
&& ./configure \--prefix=$PREFIX \--datadir=$TMP_DIR \--enable-shared
\--disable-static \  
&& make \  
&& make install \  
#  
# ffmpeg  
#  
# --pkg-config-flags="--static" \  
&& curl \--retry 5 -Ls
http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.bz2 | tar jxf - -C
$TMP_DIR \  
&& cd $TMP_DIR/ffmpeg* \  
&& ./configure \  
\--prefix=$PREFIX \  
\--bindir=$PREFIX/bin \  
\--extra-cflags="-I$PREFIX/include" \  
\--extra-ldflags="-L$PREFIX/lib" \  
\--extra-libs=-ldl \  
\--enable-shared \  
\--enable-pthreads \  
\--enable-hardcoded-tables \  
\--disable-static \  
\--disable-debug \  
\--disable-doc \  
\--enable-gpl \  
\--enable-version3 \  
\--enable-nonfree \  
\--enable-openssl \  
\--enable-postproc \  
\--enable-small \  
\--disable-ffplay \  
\--disable-ffserver \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libmp3lame \  
\--enable-libx264 \  
&& make \  
&& make install \  
&& hash -r \  
&& ldconfig \  
#  
# Melt  
#  
&& MELT_RUNTIME_DEPS="libxml2" \  
&& MELT_BUILD_DEPS="pkg-config libxml2-dev" \  
&& apt-get -qq install -y \--no-install-recommends $MELT_RUNTIME_DEPS
$MELT_BUILD_DEPS \  
&& curl \--retry 5 -Ls
https://github.com/mltframework/mlt/archive/v${MLT_VERSION}.tar.gz | tar zxf -
-C $TMP_DIR \  
&& cd $TMP_DIR/mlt* \  
&& ./configure \  
\--prefix=$PREFIX \  
\--docdir=$TMP_DIR \  
\--mandir=$TMP_DIR \  
\--enable-gpl \  
\--disable-frei0r \  
\--disable-gtk2 \  
\--disable-jackrack \  
\--disable-opengl \  
\--disable-rtaudio \  
\--disable-swfdec \  
\--disable-gtk \  
\--disable-qt \  
&& make \  
&& make install \  
&& ldconfig \  
#  
# Mediainfo  
# python-dev \  
&& MEDIAINFO_RUNTIME_DEPS="libmms0 libcurl3-gnutls" \  
&& MEDIAINFO_BUILD_DEPS="" \  
&& apt-get install -qq -y \--no-install-recommends $MEDIAINFO_RUNTIME_DEPS
$MEDIAINFO_BUILD_DEPS \  
&& curl \--retry 5 \  
-Ls https://mediaarea.net/download/binary/libzen0/${LIBZEN0_VERSION}/libzen0_${LIBZEN0_VERSION}-1_amd64.Debian_8.0.deb \  
\--output libzen0.deb \  
-Ls https://mediaarea.net/download/binary/libmediainfo0/${MEDIAINFO_VERSION}/libmediainfo0_${MEDIAINFO_VERSION}-1_amd64.Debian_8.0.deb \  
\--output libmediainfo0.deb \  
-Ls https://mediaarea.net/download/binary/mediainfo/${MEDIAINFO_VERSION}/mediainfo_${MEDIAINFO_VERSION}-1_amd64.Debian_8.0.deb \  
\--output mediainfo.deb \  
&& dpkg -i libzen0.deb libmediainfo0.deb mediainfo.deb \  
#  
# clean-up  
#  
&& cd / \  
&& apt-get purge \--auto-remove -y $BUILD_DEPS $FFMPEG_BUILD_DEPS
$MELT_BUILD_DEPS $MEDIAINFO_BUILD_DEPS \  
&& apt-get clean \  
&& rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
#  
# test that builds work  
#  
&& ffmpeg -buildconf \  
&& melt \--version \  
&& mediainfo \--version || [ $? -eq 255 ] \  
&& node \--version  
CMD ["/bin/bash"]  

