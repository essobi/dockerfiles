# ffmpeg build - simply change versions to compile  
# This Dockerfile is based on docker image rottenberg/ffmpeg  
# The purpose behind this is to build ffmpeg inside a debian container.  
# Then the next step is to export the compiled binaries into an untouched base
debian image  
# This results in a ~50% images size reduction.  
# FYI: this image is useable....I just like having a smaller base image to
download.  
# Some of these options I don't use, so I commented them out.  
# My builds include only FFMPEG + libfdk_aac + latest x264 +
Decklink(Blackmagic)  
# I am including Decklink(Blackmagic) so I can utilize those devices  
# I don't need anything else. If you need anything included, email me and I
can make alternative builds.  
# I will be tracking the 'stable' rolling release of Debian  
FROM debian:stable  
MAINTAINER Nachochip <blockchaincolony@gmail.com>  
  
ENV FFMPEG_VERSION 3.2.4  
# monitor releases at https://github.com/FFmpeg/FFmpeg/releases  
ENV YASM_VERSION 1.3.0  
# monitor releases at https://github.com/yasm/yasm/releases  
ENV FDKAAC_VERSION 0.1.5  
# monitor releases at https://github.com/mstorsjo/fdk-aac/releases  
#ENV x264  
# this project does not use release versions at this time  
# monitor project at http://git.videolan.org/?p=x264.git;a=shortlog  
#ENV LAME_VERSION 3.99.5  
#ENV FAAC_VERSION 1.28  
#ENV XVID_VERSION 1.3.3  
#ENV MPLAYER_VERSION 1.1.1  
ENV BLACKMAGIC_SDK_VERSION 10.8.3  
# monitor my own releases at https://github.com/nachochip/Blackmagic-
SDK/releases  
# the origin of the drivers comes from
https://www.blackmagicdesign.com/support/family/capture-and-playback  
# I roll them into github to track it better, and condense to only linux-
drivers  
ENV SRC /usr/local  
ENV LD_LIBRARY_PATH ${SRC}/lib  
ENV PKG_CONFIG_PATH ${SRC}/lib/pkgconfig  
  
RUN bash -c 'set -euo pipefail'  
RUN apt-get update  
RUN apt-get install -y autoconf automake gcc build-essential git libtool make
nasm zlib1g-dev tar curl  
  
# YASM  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os
http://www.tortall.net/projects/yasm/releases/yasm-${YASM_VERSION}.tar.gz && \  
tar xzvf yasm-${YASM_VERSION}.tar.gz && \  
cd yasm-${YASM_VERSION} && \  
./configure --prefix="$SRC" \--bindir="${SRC}/bin" && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR}  
  
# x264  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
git clone \--depth 1 git://git.videolan.org/x264 && \  
cd x264 && \  
./configure --prefix="$SRC" \--bindir="${SRC}/bin" \--enable-static && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR}  
  
# LAME  
#RUN DIR=$(mktemp -d) && cd ${DIR} && \  
# curl -L -Os
http://downloads.sourceforge.net/project/lame/lame/${LAME_VERSION%.*}/lame-${LAME_VERSION}.tar.gz
&& \  
# tar xzvf lame-${LAME_VERSION}.tar.gz && \  
# cd lame-${LAME_VERSION} && \  
# ./configure --prefix="${SRC}" --bindir="${SRC}/bin" --disable-shared
--enable-nasm && \  
# make && \  
# make install && \  
# make distclean && \  
# rm -rf ${DIR}  
# FAAC  
# This combines faac + http://stackoverflow.com/a/4320377  
#RUN DIR=$(mktemp -d) && cd ${DIR} && \  
# curl -L -Os
http://downloads.sourceforge.net/faac/faac-${FAAC_VERSION}.tar.gz && \  
# tar xzvf faac-${FAAC_VERSION}.tar.gz && \  
# cd faac-${FAAC_VERSION} && \  
# sed -i '126d' common/mp4v2/mpeg4ip.h && \  
# ./bootstrap && \  
# ./configure --prefix="${SRC}" --bindir="${SRC}/bin" && \  
# make && \  
# make install &&\  
# rm -rf ${DIR}  
# XVID  
#RUN DIR=$(mktemp -d) && cd ${DIR} && \  
# curl -L -Os
http://downloads.xvid.org/downloads/xvidcore-${XVID_VERSION}.tar.gz && \  
# tar xzvf xvidcore-${XVID_VERSION}.tar.gz && \  
# cd xvidcore/build/generic && \  
# ./configure --prefix="${SRC}" --bindir="${SRC}/bin" && \  
# make && \  
# make install && \  
# rm -rf ${DIR}  
# FDK_AAC  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -s https://codeload.github.com/mstorsjo/fdk-aac/tar.gz/v${FDKAAC_VERSION}
| tar zxvf - && \  
cd fdk-aac-${FDKAAC_VERSION} && \  
autoreconf -fiv && \  
./configure --prefix="${SRC}" \--disable-shared && \  
make && \  
make install && \  
make distclean && \  
rm -rf ${DIR}  
  
# Blackmagic SDK  
RUN cd /usr/src/ && \  
curl -s https://codeload.github.com/nachochip/Blackmagic-
SDK/tar.gz/${BLACKMAGIC_SDK_VERSION} | tar xzvf -  
  
# FFMPEG  
# I removed these flags from configure: --enable-libfaac --enable-libmp3lame
--enable-libxvid  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -Os http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
tar xzvf ffmpeg-${FFMPEG_VERSION}.tar.gz && \  
cd ffmpeg-${FFMPEG_VERSION} && \  
./configure --prefix="${SRC}" \--extra-cflags="-I${SRC}/include" \--extra-
ldflags="-L${SRC}/lib" \--bindir="${SRC}/bin" \  
\--extra-libs=-ldl --enable-version3 --enable-libx264 --enable-gpl \  
\--enable-postproc --enable-nonfree --enable-avresample --enable-libfdk_aac
--disable-debug --enable-small \  
\--enable-decklink --extra-cflags=-I/usr/src/Blackmagic-
SDK-${BLACKMAGIC_SDK_VERSION}/Linux/include/ \  
\--extra-ldflags=-L/usr/src/Blackmagic-
SDK-${BLACKMAGIC_SDK_VERSION}/Linux/include/ && \  
make && \  
make install && \  
make distclean && \  
hash -r && \  
rm -rf ${DIR}  
  
# MPLAYER  
#RUN DIR=$(mktemp -d) && cd ${DIR} && \  
# curl -Os
http://mplayerhq.hu/MPlayer/releases/MPlayer-${MPLAYER_VERSION}.tar.xz && \  
# tar xvf MPlayer-${MPLAYER_VERSION}.tar.xz && \  
# cd MPlayer-${MPLAYER_VERSION} && \  
# ./configure --prefix="${SRC}" --extra-cflags="-I${SRC}/include" --extra-
ldflags="-L${SRC}/lib" --bindir="${SRC}/bin" && \  
# make && \  
# make install && \  
# rm -rf ${DIR}  
RUN apt-get purge -y autoconf automake gcc build-essential git libtool make
nasm zlib1g-dev curl  
RUN apt-get clean  
RUN apt-get autoclean  
  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/libc.conf  
  
CMD ["--help"]  
ENTRYPOINT ["ffmpeg"]  

