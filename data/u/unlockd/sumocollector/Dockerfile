FROM openjdk:8-jre-slim  
  
MAINTAINER Unlockd SRE <sre@unlockd.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl gpg
dirmngr && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sLo /tmp/sumo.tar https://collectors.sumologic.com/rest/download/tar &&
\  
curl -sLo /tini https://github.com/krallin/tini/releases/download/v0.16.1/tini
&& \  
curl -sLo /tini.asc
https://github.com/krallin/tini/releases/download/v0.16.1/tini.asc && \  
gpg --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 && \  
gpg --verify /tini.asc && \  
chmod +x /tini && \  
tar xvf /tmp/sumo.tar && \  
rm -f /tmp/sumo.tar  
  
ENTRYPOINT ["/tini", "--", "/docker-entrypoint.sh"]  
CMD ["start"]  
  
COPY ["docker-entrypoint.sh", "/"]  

