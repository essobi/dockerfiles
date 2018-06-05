FROM alpine:latest  
  
# Install build deps  
ARG PKG_CONFIG_PATH=/usr/lib/pkgconfig  
ARG LD_LIBRARY_PATH=/usr/lib  
ARG PREFIX=/usr  
ARG MAKEFLAGS="-j4"  
ENV PATH $PATH:/automator  
ENV WATCHFOLDER='/downloads/watchfolder'  
ENV SERVER_PORT='7080'  
ENV PUID='911'  
ENV PGID='1000'  
ENV GITSERVER='https://github.com/phtagn/sickbeard_mp4_automator.git/'  
ENV AUTOUPDATE='true'  
ENV GITBRANCH='server'  
ENV MP4PORT='7080'  
RUN apk add --no-cache --update \  
libgcc \  
libstdc++ \  
ca-certificates \  
libcrypto1.0 \  
libssl1.0 \  
libgomp \  
expat \  
autoconf \  
automake \  
binutils \  
bzip2 \  
cmake \  
coreutils \  
file \  
g++ \  
gcc \  
gperf \  
git \  
libtool \  
make \  
python \  
openssl-dev \  
tar \  
yasm \  
zlib-dev \  
expat-dev \  
py2-pip \  
texinfo \  
diffutils \  
curl \  
mercurial \  
inotify-tools \  
py-twisted  
  
WORKDIR /tmp  
  
# NASM  
RUN \  
wget -O nasm.tar.bz2
http://www.nasm.us/pub/nasm/releasebuilds/2.13.01/nasm-2.13.01.tar.bz2 && \  
mkdir -p nasm && \  
tar xf nasm.tar.bz2 -C nasm --strip-components 1 && \  
cd nasm && \  
./autogen.sh && \  
./configure --prefix=${PREFIX} && \  
make ${MAKEFLAGS} && \  
make install  
  
# LAME  
RUN \  
DIR=/tmp/lame && \  
LAME_VERSION=3.99.5 && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sL
https://downloads.sf.net/project/lame/lame/${LAME_VERSION%.*}/lame-${LAME_VERSION}.tar.gz
| \  
tar -zx --strip-components=1 && \  
./configure --prefix="${PREFIX}" \--bindir="${PREFIX}/bin" \--enable-shared
--enable-nasm --enable-pic --disable-frontend && \  
make ${MAKEFLAGS} && \  
make install && \  
rm -rf ${DIR}  
  
## freetype https://www.freetype.org/  
RUN \  
FREETYPE_VERSION=2.5.5 && \  
DIR=/tmp/freetype && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sLO
http://download.savannah.gnu.org/releases/freetype/freetype-${FREETYPE_VERSION}.tar.gz
&& \  
tar -zx --strip-components=1 -f freetype-${FREETYPE_VERSION}.tar.gz && \  
./configure --prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
## libvstab https://github.com/georgmartius/vid.stab  
RUN \  
LIBVIDSTAB_VERSION=1.1.0 && \  
DIR=/tmp/vid.stab && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sLO
https://github.com/georgmartius/vid.stab/archive/v${LIBVIDSTAB_VERSION}.tar.gz
&&\  
tar -zx --strip-components=1 -f v${LIBVIDSTAB_VERSION}.tar.gz && \  
cmake -DCMAKE_INSTALL_PREFIX="${PREFIX}" . && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
## fridibi https://www.fribidi.org/  
RUN \  
MAKEFLAGS="-j1" && \  
rm -rf /tmp/fribidi && \  
git clone https://github.com/fribidi/fribidi.git fribidi && \  
cd /tmp/fribidi && \  
./autogen.sh --disable-docs && \  
./configure --disable-static --enable-shared --disable-docs --prefix=${PREFIX}
&& \  
make install  
  
## fontconfig https://www.freedesktop.org/wiki/Software/fontconfig/  
RUN \  
FONTCONFIG_VERSION=2.12.4 && \  
DIR=/tmp/fontconfig && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sLO
https://www.freedesktop.org/software/fontconfig/release/fontconfig-${FONTCONFIG_VERSION}.tar.bz2
&&\  
tar -jx --strip-components=1 -f fontconfig-${FONTCONFIG_VERSION}.tar.bz2 && \  
./configure -prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
## libass https://github.com/libass/libass  
RUN \  
git clone https://github.com/libass/libass.git libass && \  
cd libass && \  
./autogen.sh && \  
./configure -prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install  
  
  
## openjpeg https://github.com/uclouvain/openjpeg  
RUN \  
git clone https://github.com/uclouvain/openjpeg.git openjpeg && \  
cd openjpeg && \  
cmake -DBUILD_THIRDPARTY:BOOL=ON -DCMAKE_INSTALL_PREFIX="${PREFIX}" . && \  
make && \  
make install  
  
### libogg https://www.xiph.org/ogg/  
RUN \  
git clone https://github.com/xiph/ogg.git ogg && \  
cd ogg && \  
./autogen.sh && ./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install  
  
### libvorbis https://xiph.org/vorbis/  
RUN \  
git clone https://github.com/xiph/vorbis.git vorbis && \  
cd vorbis && \  
./autogen.sh && ./configure --prefix="${PREFIX}" \--with-ogg="${PREFIX}"
\--enable-shared && \  
make && \  
make install  
  
### libtheora http://www.theora.org/  
RUN \  
git clone https://github.com/xiph/theora.git theora && \  
cd theora && \  
./autogen.sh && ./configure --prefix="${PREFIX}" \--with-ogg="${PREFIX}"
\--enable-shared && \  
make && \  
make install  
  
# Opus  
RUN \  
git clone https://github.com/xiph/opus && \  
cd opus && \  
autoreconf -fiv && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install  
  
# xvid  
RUN \  
XVID_VERSION=1.3.4 && \  
DIR=/tmp/xvid && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sLO http://downloads.xvid.org/downloads/xvidcore-${XVID_VERSION}.tar.gz
&& \  
tar -zx -f xvidcore-${XVID_VERSION}.tar.gz && \  
cd xvidcore/build/generic && \  
./configure --prefix="${PREFIX}" \--bindir="${PREFIX}/bin" \--datadir="${DIR}"
\--enable-shared --enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
# fdk-aac  
RUN \  
git clone https://github.com/mstorsjo/fdk-aac.git fdk-aac && \  
cd fdk-aac && \  
autoreconf -fiv && \  
./configure --prefix="${PREFIX}" \--enable-shared --datadir=/tmp/fdk-aac && \  
make ${MAKEFLAGS} && \  
make install  
  
# VPX  
RUN \  
git clone \--depth 1 https://chromium.googlesource.com/webm/libvpx.git && \  
cd libvpx && \  
./configure --prefix=${PREFIX} \--disable-examples --disable-unit-tests
--enable-vp9-highbitdepth --disable-install-bins --disable-debug --enable-
shared && \  
make ${MAKEFLAGS} && \  
make install  
  
# x265  
RUN \  
hg clone https://bitbucket.org/multicoreware/x265 && \  
cd x265/build/linux && \  
sed -i "/-DEXTRA_LIB/ s/$/ -DCMAKE_INSTALL_PREFIX=\${PREFIX}/" multilib.sh &&
\  
sed -i "/^cmake/ s/$/ -DENABLE_CLI=OFF/" multilib.sh && \  
./multilib.sh && \  
make -C 8bit install  
  
RUN \  
OPENCOREAMR_VERSION=0.1.4 && \  
DIR=/tmp/opencore-amr && \  
mkdir -p ${DIR} && \  
cd ${DIR} && \  
curl -sL https://downloads.sf.net/project/opencore-amr/opencore-amr/opencore-
amr-${OPENCOREAMR_VERSION}.tar.gz | \  
tar -zx --strip-components=1 && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ${DIR}  
  
# X264 -  
RUN \  
git clone https://git.videolan.org/git/x264.git && \  
cd x264 && \  
./configure --prefix="${PREFIX}" \--enable-shared --enable-pic --disable-cli
&& \  
make ${MAKEFLAGS} && \  
make install  
  
RUN \  
git clone https://github.com/ffmpeg/ffmpeg && \  
cd ffmpeg && \  
./configure \  
\--prefix=${PREFIX} \  
\--extra-cflags="-I${PREFIX}/include" \  
\--extra-ldflags="-L${PREFIX}/lib" \  
\--extra-libs=-ldl \  
\--enable-shared \  
\--disable-doc \  
\--disable-debug \  
\--disable-ffplay \  
\--enable-gpl \  
\--enable-libopencore-amrnb \  
\--enable-libopencore-amrwb \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libmp3lame \  
\--enable-libopus \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libxvid \  
\--enable-postproc \  
\--enable-libopenjpeg \  
\--enable-avresample \  
\--enable-small \  
\--enable-libvpx \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-libvidstab \  
\--enable-version3 \  
\--enable-nonfree && \  
make ${MAKEFLAGS} && \  
make install && \  
make distclean && \  
hash -r && \  
cd tools && \  
make qt-faststart && \  
cp qt-faststart ${PREFIX}/bin  
  
RUN LD_LIBRARY_PATH=/usr/lib ffmpeg -buildconf  
  
RUN rm -Rf /tmp/*  
  
RUN pip install \  
requests \  
requests[security] \  
requests-cache \  
"stevedore==1.19.1" \  
babelfish \  
"guessit<2" \  
"subliminal<2" \  
qtfaststart \  
deluge-client \  
Twisted  
  
#RUN \  
# git clone -b server https://github.com/phtagn/sickbeard_mp4_automator.git/
/automator  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
RUN \  
apk add --no-cache shadow && \  
groupmod -g ${PGID} users && \  
useradd -u ${PUID} -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
mkdir -p /config && \  
mkdir /automator  
  
COPY rootfs/ /  
  
RUN \  
rm -Rf /tmp/*  
  
RUN apk del \  
autoconf \  
automake \  
binutils \  
cmake \  
g++ \  
gcc \  
gperf \  
make \  
openssl-dev \  
yasm \  
texinfo \  
diffutils \  
mercurial  
  
WORKDIR /automator  
EXPOSE 7080  
ENTRYPOINT ["/init"]  

