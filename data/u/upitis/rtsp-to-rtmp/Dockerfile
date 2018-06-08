FROM ubuntu:16.04  
MAINTAINER Konstantin Upitis <upitis.k@gmail.com>  
  
LABEL version="1.1" description="Retransmit rtsp to rtmp stream AS IS using
ffmpeg"  
#CMD ["--help"]  
#ENTRYPOINT ["ffmpeg"]  
WORKDIR /tmp/workdir  
  
  
ENV FFMPEG_VERSION=3.2.2 \  
FDKAAC_VERSION=0.1.4 \  
LAME_VERSION=3.99.5 \  
OGG_VERSION=1.3.2 \  
OPUS_VERSION=1.1.1 \  
THEORA_VERSION=1.1.1 \  
YASM_VERSION=1.3.0 \  
VORBIS_VERSION=1.3.5 \  
VPX_VERSION=1.6.0 \  
XVID_VERSION=1.3.4 \  
X265_VERSION=2.0 \  
X264_VERSION=20160826-2245-stable \  
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig \  
SRC=/usr/local  
  
RUN buildDeps="autoconf \  
automake \  
cmake \  
curl \  
bzip2 \  
g++ \  
gcc \  
git \  
libtool \  
make \  
nasm \  
perl \  
pkg-config \  
python \  
libssl-dev \  
yasm \  
zlib1g-dev" && \  
export MAKEFLAGS="-j$(($(nproc) \+ 1))" && \  
apt-get -yqq update && \  
apt-get install -yq --no-install-recommends ${buildDeps} ca-certificates && \  
  
DIR=$(mktemp -d) && cd ${DIR} && \  
## x264 http://www.videolan.org/developers/x264.html  
curl -sL
https://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-${X264_VERSION}.tar.bz2
| \  
tar -jx --strip-components=1 && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" \--enable-pic --enable-
shared --disable-cli && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## x265 http://x265.org/  
curl -sL
https://download.videolan.org/pub/videolan/x265/x265_${X265_VERSION}.tar.gz |
\  
tar -zx && \  
cd x265_${X265_VERSION}/build/linux && \  
./multilib.sh && \  
make -C 8bit install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libogg https://www.xiph.org/ogg/  
curl -sL http://downloads.xiph.org/releases/ogg/libogg-${OGG_VERSION}.tar.gz |
\  
tar -zx --strip-components=1 && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" \--disable-static
--datarootdir=${DIR} && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libopus https://www.opus-codec.org/  
curl -sL http://downloads.xiph.org/releases/opus/opus-${OPUS_VERSION}.tar.gz |
\  
tar -zx --strip-components=1 && \  
autoreconf -fiv && \  
./configure --prefix="${SRC}" \--disable-static --datadir="${DIR}" && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libvorbis https://xiph.org/vorbis/  
curl -sL
http://downloads.xiph.org/releases/vorbis/libvorbis-${VORBIS_VERSION}.tar.gz |
\  
tar -zx --strip-components=1 && \  
./configure --prefix="${SRC}" \--with-ogg="${SRC}" \--bindir="${SRC}/bin" \  
\--disable-static --datadir="${DIR}" && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libtheora http://www.theora.org/  
curl -sL
http://downloads.xiph.org/releases/theora/libtheora-${THEORA_VERSION}.tar.bz2
| \  
tar -jx --strip-components=1 && \  
./configure --prefix="${SRC}" \--with-ogg="${SRC}" \--bindir="${SRC}/bin" \  
\--disable-static --datadir="${DIR}" && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libvpx https://www.webmproject.org/code/  
curl -sL https://codeload.github.com/webmproject/libvpx/tar.gz/v${VPX_VERSION}
| \  
tar -zx --strip-components=1 && \  
./configure --prefix="${SRC}" \--enable-vp8 --enable-vp9 --enable-pic
--disable-debug --disable-examples --disable-docs --disable-install-bins
--enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## libmp3lame http://lame.sourceforge.net/  
curl -sL
https://downloads.sf.net/project/lame/lame/${LAME_VERSION%.*}/lame-${LAME_VERSION}.tar.gz
| \  
tar -zx --strip-components=1 && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" \--disable-static
--enable-nasm --datarootdir="${DIR}" && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## xvid https://www.xvid.com/  
curl -sL http://downloads.xvid.org/downloads/xvidcore-${XVID_VERSION}.tar.gz |
\  
tar -zx && \  
cd xvidcore/build/generic && \  
./configure --prefix="${SRC}" \--bindir="${SRC}/bin" \--datadir="${DIR}"
\--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## fdk-aac https://github.com/mstorsjo/fdk-aac  
curl -sL https://github.com/mstorsjo/fdk-aac/archive/v${FDKAAC_VERSION}.tar.gz
| \  
tar -zx --strip-components=1 && \  
autoreconf -fiv && \  
./configure --prefix="${SRC}" \--disable-static --datadir="${DIR}" && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR} && \  
DIR=$(mktemp -d) && cd ${DIR} && \  
## ffmpeg https://ffmpeg.org/  
curl -sL http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz | \  
tar -zx --strip-components=1 && \  
./configure --prefix="${SRC}" \  
\--extra-cflags="-I${SRC}/include" \  
\--extra-ldflags="-L${SRC}/lib" \  
\--bindir="${SRC}/bin" \  
\--disable-doc \  
\--disable-static \  
\--enable-shared \  
\--disable-ffplay \  
\--extra-libs=-ldl \  
\--enable-version3 \  
\--enable-libfdk_aac \  
\--enable-libmp3lame \  
\--enable-libopus \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libvpx \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-libxvid \  
\--enable-gpl \  
\--enable-avresample \  
\--enable-postproc \  
\--enable-nonfree \  
\--disable-debug \  
\--enable-small \  
\--enable-openssl && \  
make && \  
make install && \  
make distclean && \  
hash -r && \  
cd tools && \  
make qt-faststart && \  
cp qt-faststart ${SRC}/bin && \  
rm -rf ${DIR} && \  
## cleanup  
cd && \  
apt-get purge -y ${buildDeps} && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists && \  
ffmpeg -buildconf  
##  
##JAVA + TOMCAT  
##  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
# let "Tomcat Native" live somewhere isolated  
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libapr1 \  
openssl \  
wget \  
software-properties-common \  
openjdk-8-jdk \  
&& add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update && apt-get install -y --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS  
# see also "update.sh" (https://github.com/docker-
library/tomcat/blob/master/update.sh)  
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6
07E48665A34DCAFAE522E5E6266191C37C037D42
47309207D818FFD8DCD3F83F1931D684307A10A5
541FBE7D8F78B25E055DDEE13C370389288584E7
61B832AC2F1C5A90F0F9B00A1C506407564C17A3
713DA88BE50911535FE716F5208B0AB1D63011C7
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED
9BA44C2621385CB966EBA586F72C284D731FABEE
A27677289986DB50844682F8ACB77FC2E86E29AC
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
gpg --keyserver eu.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.9  
  
#
https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
# not all the mirrors actually carry the .asc files :'(  
ENV TOMCAT_ASC_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN set -x \  
\  
&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \  
&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
\  
&& nativeBuildDir="$(mktemp -d)" \  
&& tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" \--strip-
components=1 \  
&& nativeBuildDeps=" \  
gcc \  
libapr1-dev \  
libssl-dev \  
make \  
" \  
&& apt-get update && apt-get install -y --no-install-recommends
$nativeBuildDeps && rm -rf /var/lib/apt/lists/* \  
&& ( \  
export CATALINA_HOME="$PWD" \  
&& cd "$nativeBuildDir/native" \  
&& ./configure \  
\--libdir="$TOMCAT_NATIVE_LIBDIR" \  
\--prefix="$CATALINA_HOME" \  
\--with-apr="$(which apr-1-config)" \  
\--with-java-home="$(docker-java-home)" \  
\--with-ssl=yes \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& apt-get purge -y --auto-remove $nativeBuildDeps \  
&& rm -rf "$nativeBuildDir" \  
&& rm bin/tomcat-native.tar.gz  
  
# verify Tomcat Native is working properly  
RUN set -e \  
&& nativeLines="$(catalina.sh configtest 2>&1)" \  
&& nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \  
&& nativeLines="$(echo "$nativeLines" | sort -u)" \  
&& if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat
Native library' >&2; then \  
echo >&2 "$nativeLines"; \  
exit 1; \  
fi  
  
COPY ./target/rtsp2rtmp-1.0 $CATALINA_HOME/webapps/rtsp2rtmp-1.0  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

