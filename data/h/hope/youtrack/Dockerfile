FROM hope/java:8  
  
ENV \  
# https://www.jetbrains.com/youtrack/download/get_youtrack.html  
YOUTRACK_VERSION=2017.2 \  
YOUTRACK_BUILD=33154 \  
YOUTRACK_PORT=8080 \  
YOUTRACK_INSTALL=/usr/local/youtrack  
  
RUN \  
apk add --no-cache --virtual=build-dependencies wget ca-certificates && \  
cd "/tmp" && \  
  
# Youtrack install  
wget
https://download.jetbrains.com/charisma/youtrack-${YOUTRACK_VERSION}.${YOUTRACK_BUILD}.zip
&& \  
  
unzip youtrack-${YOUTRACK_VERSION}.${YOUTRACK_BUILD}.zip && \  
rm -rf youtrack-${YOUTRACK_VERSION}.${YOUTRACK_BUILD}/internal/java && \  
mv youtrack-${YOUTRACK_VERSION}.${YOUTRACK_BUILD} ${YOUTRACK_INSTALL} && \  
  
# Configure  
${YOUTRACK_INSTALL}/bin/youtrack.sh configure \  
\--backups-dir=/data/backups \  
\--temp-dir=/data/temp \  
\--data-dir=/data/app \  
\--logs-dir=/data/logs \  
\--listen-port=${YOUTRACK_PORT} && \  
  
# Cleanup  
apk del build-dependencies && \  
rm -rf "/tmp/"*  
  
VOLUME /data  
VOLUME ${YOUTRACK_INSTALL}/conf  
  
EXPOSE ${YOUTRACK_PORT}  
  
ENTRYPOINT ["/usr/local/youtrack/bin/youtrack.sh"]  
CMD ["run", "--no-browser"]  

