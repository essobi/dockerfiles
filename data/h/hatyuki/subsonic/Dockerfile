# Pull base image  
FROM java:8-jre-alpine  
  
# Set default arguments  
ARG SUBSONIC_HOME="/var/subsonic"  
ARG SUBSONIC_VERSION="6.0"  
ARG SUBSONIC_TRANSCODERS="flac lame"  
ARG SUBSONIC_HOME  
ARG SUBSONIC_DATA  
  
# Set environment variables  
ENV SUBSONIC_DATA=${SUBSONIC_DATA:-"${SUBSONIC_HOME}/data"}  
  
# Copy startup script  
COPY start.sh /tmp/start.sh  
  
# Install subsonic  
RUN apk --no-cache add tzdata $SUBSONIC_TRANSCODERS && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
addgroup -S -g 1000 subsonic && \  
adduser -S -h ${SUBSONIC_HOME} -G subsonic -u 1000 subsonic && \  
wget
http://subsonic.org/download/subsonic-${SUBSONIC_VERSION}-standalone.tar.gz -O
- | tar zxf - -C /tmp && \  
install -o subsonic -g subsonic -m 0640 /tmp/* ${SUBSONIC_HOME} && \  
sed -i 's! > ${LOG} 2>&1 &!!' $SUBSONIC_HOME/subsonic.sh && \  
install -o subsonic -g subsonic -m 0750 -d ${SUBSONIC_HOME}/transcode && \  
for transcoder in $SUBSONIC_TRANSCODERS; do ln -s "$(which $transcoder)"
$SUBSONIC_HOME/transcode; done && \  
chmod 0750 ${SUBSONIC_HOME}/*.sh && \  
rm -rf /tmp/* && \  
apk del tzdata  
  
# Define default user  
USER subsonic  
  
# Define working directory  
WORKDIR $SUBSONIC_HOME  
  
# Define default command  
CMD ["/bin/sh", "start.sh"]  
  
# Expose ports  
EXPOSE 4040  

