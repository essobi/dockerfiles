#  
# Build image  
#  
ARG DEBIAN_IMAGE=debian:stretch-slim  
FROM debian:stretch-slim as unpack  
  
ENV LANG 'C.UTF-8'  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY \--from=olfway/qemu-user-static /qemu-arm-static /usr/bin/  
COPY \--from=olfway/qemu-user-static /qemu-aarch64-static /usr/bin/  
  
RUN set -x \  
&& echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/zz-force-ipv4 \  
&& echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/zz-no-install-
recommends  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
ca-certificates \  
curl \  
xz-utils  
  
WORKDIR /usr/src  
  
ARG FREESWITCH_RELEASE=1.6.20  
ARG FREESWITCH_URL=https://files.freeswitch.org/freeswitch-releases  
  
COPY build/freeswitch-${FREESWITCH_RELEASE}.tar.xz.sha256 .  
RUN set -x \  
&& curl --ipv4 -O "${FREESWITCH_URL}/freeswitch-${FREESWITCH_RELEASE}.tar.xz"
\  
&& sha256sum -c "freeswitch-${FREESWITCH_RELEASE}.tar.xz.sha256" \  
&& tar -Jxf "freeswitch-${FREESWITCH_RELEASE}.tar.xz"  
  
RUN set -x \  
&& apt-get install -y \  
file \  
yasm  
  
ARG ARCH_DEBIAN=amd64  
ENV ARCH_DEBIAN=$ARCH_DEBIAN  
  
RUN set -x \  
&& dpkg --add-architecture $ARCH_DEBIAN \  
&& apt-get update \  
&& apt-get install -y \  
libasound2-dev:$ARCH_DEBIAN \  
libcurl4-openssl-dev:$ARCH_DEBIAN \  
libedit-dev:$ARCH_DEBIAN \  
libjpeg-dev:$ARCH_DEBIAN \  
liblua5.2-dev:$ARCH_DEBIAN \  
libopus-dev:$ARCH_DEBIAN \  
libpcre3-dev:$ARCH_DEBIAN \  
libsndfile1-dev:$ARCH_DEBIAN \  
libspeex-dev:$ARCH_DEBIAN \  
libspeexdsp-dev:$ARCH_DEBIAN \  
libsqlite3-dev:$ARCH_DEBIAN \  
libssl1.0-dev:$ARCH_DEBIAN \  
libyaml-dev:$ARCH_DEBIAN \  
pkg-config:$ARCH_DEBIAN \  
uuid-dev:$ARCH_DEBIAN \  
zlib1g-dev:$ARCH_DEBIAN  
  
ARG TOOLCHAIN=x86_64-linux-gnu  
ENV TOOLCHAIN=$TOOLCHAIN  
  
RUN set -x \  
&& if [ "$(dpkg --print-architecture)" = "$ARCH_DEBIAN" ]; then \  
apt-get install -y build-essential ; \  
else \  
apt-get install -y crossbuild-essential-$ARCH_DEBIAN \  
&& ln -v -s /usr/bin/$TOOLCHAIN-gcc /usr/$TOOLCHAIN/bin/gcc ; \  
fi  
  
ENV
PATH=/usr/local/freeswitch:/usr/$TOOLCHAIN/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
WORKDIR /usr/src/freeswitch-${FREESWITCH_RELEASE}  
  
COPY build/modules.conf ./  
  
CMD [ "/bin/bash" ]  
  
#  
# Build image  
#  
FROM unpack as build  
  
RUN set -x \  
&& ./configure --host=$TOOLCHAIN \--disable-libvpx --disable-libyuv --disable-
srtp --disable-static  
  
RUN set -x \  
&& make \  
&& make install  
  
RUN set -x \  
&& rm -rf /usr/local/freeswitch/include \  
&& mv /usr/local/freeswitch/conf /usr/local/freeswitch/conf.sample \  
&& mv /usr/local/freeswitch/htdocs /usr/local/freeswitch/htdocs.sample  
  
RUN set -x \  
&& file /usr/local/freeswitch/bin/freeswitch  
  
CMD [ "/bin/bash" ]  
  
#  
# Run image  
#  
FROM ${DEBIAN_IMAGE}  
LABEL maintainer="Pavel Volkovitskiy <olfway@olfway.net>"  
  
ENV LANG 'C.UTF-8'  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY \--from=olfway/qemu-user-static /qemu-arm-static /usr/bin/  
COPY \--from=olfway/qemu-user-static /qemu-aarch64-static /usr/bin/  
  
RUN set -x \  
&& echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/zz-force-ipv4 \  
&& echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/zz-no-install-
recommends  
  
RUN set -x \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
libcurl3 \  
libedit2 \  
libjpeg62-turbo \  
liblua5.2-0 \  
libopus0 \  
libsndfile1 \  
libspeex1 \  
libspeexdsp1 \  
libsqlite3-0 \  
&& apt-get clean  
  
COPY \--from=build /usr/local/freeswitch/ /usr/local/freeswitch/  
  
ENV PATH=/usr/local/freeswitch/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
WORKDIR "/usr/local/freeswitch"  
  
COPY conf/ conf/  
  
RUN set -x \  
&& freeswitch -version \  
&& freeswitch -nonat -nonatmap -nort -ncwait \  
&& fs_cli -x 'version' \  
&& freeswitch -stop  
  
CMD [ "/usr/local/freeswitch/bin/freeswitch", "-nf", "-nonat" ]  

