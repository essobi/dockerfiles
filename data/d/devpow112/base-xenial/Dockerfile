FROM ubuntu:16.04  
LABEL maintainer devpow112  
  
# set input arguments to defaults  
ARG S6_OVERLAY_VERSION="1.21.4.0"  
ARG S6_OVERLAY_ARCH="amd64"  
ARG LOCALE="en_US.UTF-8"  
# set environment variables  
ENV HOME="/root" \  
TERM="xterm"  
# download s6 overlays  
ADD "https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz"
/tmp  
  
# setup packages and users  
RUN export DEBIAN_FRONTEND="noninteractive" && \  
apt-get update && \  
apt-get install -y \  
apt-utils \  
locales \  
tzdata && \  
locale-gen ${LOCALE} && \  
update-locale --reset \  
LANG=${LOCALE} \  
LANGUAGE=${LOCALE} \  
LC_ALL=${LOCALE} && \  
tar xfz \  
/tmp/s6-overlay-${S6_OVERLAY_ARCH}.tar.gz \  
-C / && \  
mkdir /config && \  
useradd -U -d /config -s /bin/false primary-user && \  
usermod -a -G users primary-user && \  
apt-get clean && \  
apt-get autoremove -y --purge && \  
rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/*  
  
# set locale environment variables  
ENV LANG=${LOCALE} \  
LANGUAGE=${LOCALE} \  
LC_ALL=${LOCALE}  
  
# add local files  
COPY root/ /  
  
# volumes and entry point  
VOLUME /config  
ENTRYPOINT ["/init"]  

