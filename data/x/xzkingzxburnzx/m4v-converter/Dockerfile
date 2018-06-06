FROM alpine:3.7 AS build  
MAINTAINER xzkingzxburnzx  
  
ARG PREFIX="/tmp/ffmpeg"  
ARG BINDIR="${PREFIX}/bin"  
ARG SOURCES="${PREFIX}/sources"  
ARG LD_LIBRARY_PATH="${PREFIX}/lib"  
ARG PKG_CONFIG_PATH="${LD_LIBRARY_PATH}/pkgconfig"  
ARG MAKEFLAGS="-j2"  
ARG DEPENDS="autoconf \  
automake \  
binutils \  
bzip2 \  
make \  
cmake \  
coreutils \  
file \  
g++ \  
gcc \  
gperf \  
libtool \  
zlib-dev \  
expat-dev \  
itstool \  
util-linux-dev"  
RUN \  
apk add --no-cache --update ${DEPENDS} && \  
mkdir -p "${SOURCES}"  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://www.nasm.us/pub/nasm/releasebuilds/2.13.01/nasm-2.13.01.tar.gz &&
\  
tar xzvf nasm-2.13.01.tar.gz && \  
cd nasm-2.13.01 && \  
./autogen.sh && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../nasm-2.13.01*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O yasm-1.3.0.tar.gz https://github.com/yasm/yasm/archive/v1.3.0.tar.gz
&& \  
tar xzvf yasm-1.3.0.tar.gz && \  
cd yasm-1.3.0 && \  
autoreconf -fiv && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../yasm-1.3.0*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget https://sourceforge.net/projects/opencore-amr/files/opencore-
amr/opencore-amr-0.1.5.tar.gz && \  
tar xzvf opencore-amr-0.1.5.tar.gz && \  
cd opencore-amr-0.1.5 && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../opencore-amr-0.1.5*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget https://downloads.xvid.com/downloads/xvidcore-1.3.5.tar.gz && \  
tar xzvf xvidcore-1.3.5.tar.gz && \  
cd xvidcore/build/generic && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../../../xvidcore*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O openjpeg-2.3.0.tar.gz
https://github.com/uclouvain/openjpeg/archive/v2.3.0.tar.gz && \  
tar xzvf openjpeg-2.3.0.tar.gz && \  
cd openjpeg-2.3.0 && \  
cmake -DBUILD_THIRDPARTY:BOOL=ON -DCMAKE_INSTALL_PREFIX="${PREFIX}" . && \  
make && \  
make install && \  
rm -rf ../openjpeg-2.3.0*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O vid.stab-1.1.0.tar.gz
https://github.com/georgmartius/vid.stab/archive/v1.1.0.tar.gz && \  
tar xzvf vid.stab-1.1.0.tar.gz && \  
cd vid.stab-1.1.0 && \  
cmake -DCMAKE_INSTALL_PREFIX="${PREFIX}" . && \  
make && \  
make install && \  
rm -rf ../vid.stab-1.1.0*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://www.namesdir.com/mirrors/nongnu/freetype/freetype-2.8.1.tar.gz &&
\  
tar xzvf freetype-2.8.1.tar.gz && \  
cd freetype-2.8.1 && \  
./configure --prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ../freetype-2.8.1*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O fribidi-0.19.7.tar.gz
https://github.com/fribidi/fribidi/archive/0.19.7.tar.gz && \  
tar xzvf fribidi-0.19.7.tar.gz && \  
cd fribidi-0.19.7 && \  
sed -i 's/^SUBDIRS =.*/SUBDIRS=gen.tab charset lib/' Makefile.am && \  
./bootstrap --no-config && \  
./configure --prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ../fribidi-0.19.7*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget
https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.12.91.tar.gz
&& \  
tar xzvf fontconfig-2.12.91.tar.gz && \  
cd fontconfig-2.12.91 && \  
./configure -prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ../fontconfig-2.12.91*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget
https://github.com/libass/libass/releases/download/0.13.6/libass-0.13.6.tar.gz
&& \  
tar xzvf libass-0.13.6.tar.gz && \  
cd libass-0.13.6 && \  
./configure --prefix="${PREFIX}" \--disable-static --enable-shared && \  
make && \  
make install && \  
rm -rf ../libass-0.13.6*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O fdk-aac-0.1.5.tar.gz https://github.com/mstorsjo/fdk-
aac/archive/v0.1.5.tar.gz && \  
tar xzvf fdk-aac-0.1.5.tar.gz && \  
cd fdk-aac-0.1.5 && \  
autoreconf -fiv && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../fdk-aac-0.1.5*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget
http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz &&
\  
tar xzvf lame-3.99.5.tar.gz && \  
cd lame-3.99.5 && \  
./configure --prefix="${PREFIX}" \--enable-shared --enable-nasm --enable-pic
--disable-frontend && \  
make && \  
make install && \  
rm -rf ../lame-3.99.5*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://downloads.xiph.org/releases/opus/opus-1.1.3.tar.gz && \  
tar xzvf opus-1.1.3.tar.gz && \  
cd opus-1.1.3 && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../opus-1.1.3*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz && \  
tar xzvf libogg-1.3.2.tar.gz && \  
cd libogg-1.3.2 && \  
./configure --prefix="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../libogg-1.3.2*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.gz && \  
tar xzvf libtheora-1.1.1.tar.gz && \  
cd libtheora-1.1.1 && \  
./configure --prefix="${PREFIX}" \--with-ogg="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../libtheora-1.1.1*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.4.tar.gz && \  
tar xzvf libvorbis-1.3.4.tar.gz && \  
cd libvorbis-1.3.4 && \  
./configure --prefix="${PREFIX}" \--with-ogg="${PREFIX}" \--enable-shared && \  
make && \  
make install && \  
rm -rf ../libvorbis-1.3.4*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget -O libvpx-1.6.0.tar.gz
https://github.com/webmproject/libvpx/archive/v1.6.0.tar.gz && \  
tar xzvf libvpx-1.6.0.tar.gz && \  
cd libvpx-1.6.0 && \  
./configure --prefix="${PREFIX}" \--enable-vp8 --enable-vp9 --enable-pic
--enable-shared \  
\--disable-debug --disable-examples --disable-docs --disable-install-bins && \  
make && \  
make install && \  
rm -rf ../libvpx-1.6.0*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget
http://download.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20171226-2245-stable.tar.bz2
&& \  
tar xjvf x264-snapshot-20171226-2245-stable.tar.bz2 && \  
cd x264-snapshot-20171226-2245-stable && \  
./configure --prefix="${PREFIX}" \--enable-shared --enable-pic --disable-cli
&& \  
make && \  
make install && \  
rm -rf ../x264-snapshot-20171226-2245-stable*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://download.videolan.org/pub/videolan/x265/x265_2.6.tar.gz && \  
tar xzvf x265_2.6.tar.gz && \  
cd x265_v2.6/build/linux && \  
sed -i "/-DEXTRA_LIB/ s/$/ -DCMAKE_INSTALL_PREFIX=\${PREFIX}/" multilib.sh &&
\  
sed -i "/^cmake/ s/$/ -DENABLE_CLI=OFF/" multilib.sh && \  
./multilib.sh && \  
make -C 8bit install && \  
rm -rf ../../../x265_v2.6*  
  
RUN \  
PATH="${BINDIR}:${PATH}" && \  
cd "${SOURCES}" && \  
wget http://www.ffmpeg.org/releases/ffmpeg-3.4.tar.gz && \  
tar xzvf ffmpeg-3.4.tar.gz && \  
cd ffmpeg-3.4 && \  
# Fixes multiple audio streams being default  
# http://trac.ffmpeg.org/ticket/3622  
# https://gist.github.com/outlyer/4a88f1adb7f895b93fd9  
# https://gist.github.com/xzKinGzxBuRnzx/da6406c854d18afdd76ab1ce7d4762c8  
wget
https://gist.githubusercontent.com/xzKinGzxBuRnzx/da6406c854d18afdd76ab1ce7d4762c8/raw/a3571e6cc3c051dd449cff89244b5bbd40b0c183/ffmpeg-3.4-defaultstreams.patch
&& \  
patch libavformat/movenc.c < ffmpeg-3.4-defaultstreams.patch && \  
./configure \  
\--prefix="${PREFIX}" \  
\--extra-cflags="-I${PREFIX}/include" \  
\--extra-ldflags="-L${PREFIX}/lib" \  
\--extra-libs=-ldl \  
\--disable-debug \  
\--disable-doc \  
\--disable-ffplay \  
\--enable-shared \  
\--enable-gpl \  
\--enable-libopencore-amrnb \  
\--enable-libopencore-amrwb \  
\--enable-libxvid \  
\--enable-libopenjpeg \  
\--enable-libvidstab \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libmp3lame \  
\--enable-libopus \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libvpx \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-nonfree \  
\--enable-postproc \  
\--enable-version3 && \  
make && \  
make install && \  
make distclean && \  
hash -r && \  
cd tools && \  
make qt-faststart && \  
cp qt-faststart ${BINDIR}  
  
RUN \  
cp $(ldd ${BINDIR}/ffmpeg | cut -d ' ' -f 3) /usr/local/lib/ && \  
cp ${BINDIR}/* /usr/local/bin/ && \  
cp -r ${PREFIX}/share/ffmpeg /usr/local/share/ && \  
LD_LIBRARY_PATH=/usr/local/lib ffmpeg -buildconf && \  
rm -rf ${PREFIX} && \  
apk del --purge ${DEPENDS}  
  
FROM linuxserver/nzbget AS release  
MAINTAINER xzKinGzxBuRnzx  
  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
RUN \  
mkdir -p /app/M4V-Converter && \  
cd /tmp && \  
wget -O M4V-Converter.tar.gz
https://github.com/Digiex/M4V-Converter/archive/master.tar.gz && \  
tar xzvf M4V-Converter.tar.gz && \  
cp \  
M4V-Converter-master/M4V-Converter.sh \  
M4V-Converter-master/default.conf \  
M4V-Converter-master/LICENSE \  
/app/M4V-Converter/ && \  
ln -s /app/M4V-Converter /app/nzbget/scripts/M4V-Converter && \  
rm -rf M4V-Converter* && \  
sed -i -e "s#\\(ScriptDir=\\).*#\1$\\{AppDir\\}/scripts#g"
/defaults/nzbget.conf  
  
COPY root /  
COPY \--from=build /usr/local /usr/local  

