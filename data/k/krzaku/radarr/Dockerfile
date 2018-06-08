FROM lsiobase/mono  
MAINTAINER sparklyballs  
  
# environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_CONFIG_HOME="/config/xdg"  
# set env variables needed for subliminal to run  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
python3 \  
python3-pip \  
nodejs \  
at && \  
  
# install radarr  
radarr_tag=$(curl -sX GET
"https://api.github.com/repos/Radarr/Radarr/releases" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') && \  
mkdir -p \  
/opt/radarr && \  
curl -o \  
/tmp/radar.tar.gz -L \  
"https://github.com/galli-
leo/Radarr/releases/download/${radarr_tag}/Radarr.develop.${radarr_tag#v}.linux.tar.gz"
&& \  
tar ixzf \  
/tmp/radar.tar.gz -C \  
/opt/radarr --strip-components=1 && \  
  
# install subliminal  
pip3 install subliminal && \  
  
# clean up  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# add local files  
COPY /root /  
  
# set run-subliminal permissions  
RUN chmod +x /opt/run-subliminal  
  
# ports and volumes  
EXPOSE 7878  
VOLUME /config /downloads /movies  

