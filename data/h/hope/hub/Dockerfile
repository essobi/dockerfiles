FROM hope/java:8  
  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV \  
# https://www.jetbrains.com/hub/download/#section=linux-version  
HUB_VERSION=2017.2 \  
HUB_BUILD=5734 \  
HUB_PORT=8080 \  
HUB_INSTALL=/usr/local/hub  
  
RUN \  
apk add --no-cache --virtual=build-dependencies wget ca-certificates && \  
cd "/tmp" && \  
  
# Install  
wget https://download.jetbrains.com/hub/${HUB_VERSION}/hub-ring-
bundle-${HUB_VERSION}.${HUB_BUILD}.zip && \  
  
unzip hub-ring-bundle-${HUB_VERSION}.${HUB_BUILD}.zip && \  
rm -rf hub-ring-bundle-${HUB_VERSION}.${HUB_BUILD}/internal/java && \  
mv hub-ring-bundle-${HUB_VERSION}.${HUB_BUILD} ${HUB_INSTALL} && \  
  
# Configure  
${HUB_INSTALL}/bin/hub.sh configure \  
\--backups-dir=/data/backups \  
\--temp-dir=/data/temp \  
\--data-dir=/data/app \  
\--logs-dir=/data/logs \  
\--listen-port=${HUB_PORT} && \  
  
# Cleanup  
apk del build-dependencies && \  
rm -rf "/tmp/"*  
  
VOLUME /data  
VOLUME ${HUB_INSTALL}/conf  
  
EXPOSE ${HUB_PORT}  
  
ENTRYPOINT ["/usr/local/hub/bin/hub.sh"]  
CMD ["run", "--no-browser"]  

