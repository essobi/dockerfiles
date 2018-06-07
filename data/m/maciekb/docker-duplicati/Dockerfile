FROM lsiobase/mono  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
LABEL maintainer="sparklyballs"  
  
# environment settings  
ENV HOME="/config"  
RUN \  
echo "**** install duplicati ****" && \  
mkdir -p \  
/app/duplicati && \  
duplicati_tag=$(curl -sX GET
"https://api.github.com/repos/duplicati/duplicati/releases" \  
| awk '/tag_name.*(canary|beta|release)/{print $4;exit}' FS='[""]') && \  
duplicati_zip="duplicati-${duplicati_tag#*-}.zip" && \  
curl -o \  
/tmp/duplicati.zip -L \  
"https://github.com/duplicati/duplicati/releases/download/${duplicati_tag}/${duplicati_zip}"
&& \  
unzip -q /tmp/duplicati.zip -d /app/duplicati && \  
echo "**** install docker ****" && \  
apt-get update && \  
apt-get install --quiet --yes --no-install-recommends \  
docker.io && \  
echo "**** cleanup ****" && \  
rm -rf \  
/tmp/*  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8200  
VOLUME /data /config  

