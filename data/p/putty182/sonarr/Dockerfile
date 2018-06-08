FROM putty182/ubuntu-base  
MAINTAINER putty182  
  
# set build arg  
ARG DEBIAN_FRONTEND=noninteractive  
  
# install  
RUN curl -s -o /tmp/sonarr.tar.gz -L
"http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz" && \  
tar ixzf /tmp/sonarr.tar.gz -C /app --strip-components=1 && \  
# clean up  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 8989  
VOLUME ["/config", "/data"]  
  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD curl -f 'http://localhost:8989/sonarr/' || exit 1  

