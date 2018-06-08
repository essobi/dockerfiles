FROM putty182/ubuntu-base  
MAINTAINER putty182  
  
# set build arg  
ARG DEBIAN_FRONTEND=noninteractive  
  
# install  
RUN curl -s -o /tmp/radarr.tar.gz -L "$(curl -s
https://api.github.com/repos/radarr/radarr/releases | jq -r
.[0].assets[1].browser_download_url)" && \  
tar ixzf /tmp/radarr.tar.gz -C /app --strip-components=1 && \  
# clean up  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 7878  
VOLUME ["/config"]  
  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD curl -f 'http://localhost:7878/radarr/' || exit 1  

