FROM alpine:latest  
  
ENTRYPOINT ["/run.sh"]  
  
ENV CLEAN_PERIOD=**None** \  
DELAY_TIME=**None** \  
KEEP_IMAGES=**None** \  
KEEP_CONTAINERS=**None** \  
LOOP=true \  
DEBUG=0  
# run.sh script uses some bash specific syntax  
RUN apk add --update bash grep curl  
  
ENV VERSION=1.7.1  
RUN curl -sS https://get.docker.com/builds/Linux/x86_64/docker-$VERSION >
/usr/bin/docker-$VERSION && \  
curl -sS https://get.docker.com/builds/Linux/x86_64/docker-$VERSION.sha256 >
/usr/bin/docker-$VERSION.sha256 && \  
cd /usr/bin/ && sha256sum -c /usr/bin/docker-$VERSION.sha256 && \  
chmod u+x /usr/bin/docker-$VERSION && \  
ln -s /usr/bin/docker-$VERSION /usr/bin/docker  
  
# Install cleanup script  
ADD docker-cleanup-volumes.sh /docker-cleanup-volumes.sh  
ADD run.sh /run.sh  
  

