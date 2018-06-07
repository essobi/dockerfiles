FROM lsiobase/mono  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION="v0.7.1609"  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_DATA_HOME="/config" \  
XDG_CONFIG_HOME="/config"  
# install jackett  
RUN \  
apt-get update && \  
apt-get install -y \  
wget git && \  
jack_tag=$(cd /tmp && git clone https://github.com/Jackett/Jackett.git && cd
/tmp/Jackett/ && git describe --abbrev=0 --tags) && \  
mkdir -p \  
/app/Jackett && \  
curl -o \  
/tmp/jacket.tar.gz -L \  
https://github.com/Jackett/Jackett/releases/download/$jack_tag/Jackett.Binaries.Mono.tar.gz
&& \  
tar xf \  
/tmp/jacket.tar.gz -C \  
/app/Jackett --strip-components=1 && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads  
EXPOSE 9117  

