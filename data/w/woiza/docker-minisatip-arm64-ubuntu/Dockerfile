FROM lsiobase/xenial.arm64  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
LABEL maintainer="sparklyballs"  
  
# package version  
ARG SATIP_VER="master"  
  
# environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
  
# adding qemu for crossbuilding on DockerHub  
#COPY \--from=resin/aarch64-alpine:latest /usr/bin/qemu* /usr/bin/  
#COPY --from=resin/aarch64-alpine:latest /usr/bin/resin-xbuild* /usr/bin/  
#COPY \--from=resin/aarch64-alpine:latest /usr/bin/cross-build* /usr/bin/  
  
COPY --from=resin/aarch64-alpine:latest ["/usr/bin/qemu*", "/usr/bin/resin-
xbuild*", "/usr/bin/cross-build*", "/usr/bin/"]  
  
RUN [ "cross-build-start" ]  
  
RUN \  
echo "**** install packages ****" && \  
apt-get update && \  
apt-get install -y \  
build-essential \  
# mercurial \  
libssl-dev \  
libdvbcsa-dev \  
git \  
perl \  
openssl \  
dvb-apps && \  
  
# echo "**** build dvb-apps ****" && \  
# hg clone http://linuxtv.org/hg/dvb-apps /tmp/dvb-apps && \  
# cd /tmp/dvb-apps && \  
# make -C lib && \  
# make -C lib install && \  
  
echo "***** compile satip ****" && \  
git clone https://github.com/catalinii/minisatip \  
/app/satip && \  
cd /app/satip && \  
git checkout "${SATIP_VER}" && \  
./configure && \  
make && \  
  
echo "**** cleanup ****" && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
  
RUN [ "cross-build-end" ]  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8875 554 1900/udp  

