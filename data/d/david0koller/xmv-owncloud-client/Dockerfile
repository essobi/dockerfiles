FROM alpine:edge  
  
MAINTAINER David Koller <david.koller@xmv-solutions.com>  
  
# Install ownCloud-client  
RUN echo -e '@edge http://dl-cdn.alpinelinux.org/alpine/edge/main\n@testing
http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories &&
\  
apk add --no-cache owncloud-client@testing  
  
# All in One Volume  
VOLUME /ownCloudVolume  
  
# Start Sync  
ADD constants.sh /constants.sh  
ADD config.startup.ini /config.startup.ini  
ADD testconfig.sh /testconfig.sh  
ADD readConfig.sh /readConfig.sh  
ADD sync.sh /sync.sh  
ADD sync-exclude.lst /sync-exclude.lst  
RUN chmod 755 /*.sh  
RUN chmod 755 /*.ini  
CMD /readConfig.sh  

