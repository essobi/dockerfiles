FROM ubuntu:trusty  
  
MAINTAINER Splunk Dev <devinfo@splunk.com>  
  
ENV SPLUNK_PRODUCT splunk  
ENV SPLUNK_VERSION 7.0.4  
ENV SPLUNK_BUILD 68ba48f99743  
ENV SPLUNK_FILENAME splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-Linux-x86_64.tgz  
ENV SPLUNK_SDK_APP_COLLECTION_NAME sdk-app-collection  
ENV SPLUNK_SDK_APP_COLLECTION_VERSION 1.0.0  
ENV SPLUNK_SDK_APP_COLLECTION_URL https://github.com/splunk/sdk-app-
collection/archive/${SPLUNK_SDK_APP_COLLECTION_VERSION}.tar.gz  
ENV SPLUNK_SDK_APP_COLLECTION_FILENAME
${SPLUNK_SDK_APP_COLLECTION_NAME}.tar.gz  
  
ENV SPLUNK_HOME /opt/splunk  
ENV SPLUNK_GROUP splunk  
ENV SPLUNK_USER splunk  
ENV SPLUNK_BACKUP_DEFAULT_ETC /var/opt/splunk  
  
# add splunk:splunk user  
RUN groupadd -r ${SPLUNK_GROUP} \  
&& useradd -r -m -g ${SPLUNK_GROUP} ${SPLUNK_USER}  
  
# make the "en_US.UTF-8" locale so splunk will be utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# pdfgen dependency  
RUN apt-get install -y libgssapi-krb5-2  
  
# Download official Splunk release, verify checksum and unzip in /opt/splunk  
# Also backup etc folder, so it will be later copied to the linked volume  
RUN apt-get install -y wget \  
&& mkdir -p ${SPLUNK_HOME} \  
&& wget -qO /tmp/${SPLUNK_FILENAME}
https://download.splunk.com/products/splunk/releases/${SPLUNK_VERSION}/${SPLUNK_PRODUCT}/linux/${SPLUNK_FILENAME}
\  
&& wget -qO /tmp/${SPLUNK_FILENAME}.md5
https://download.splunk.com/products/splunk/releases/${SPLUNK_VERSION}/${SPLUNK_PRODUCT}/linux/${SPLUNK_FILENAME}.md5
\  
&& (cd /tmp && md5sum -c ${SPLUNK_FILENAME}.md5) \  
&& tar xzf /tmp/${SPLUNK_FILENAME} \--strip 1 -C ${SPLUNK_HOME} \  
&& rm /tmp/${SPLUNK_FILENAME} \  
&& rm /tmp/${SPLUNK_FILENAME}.md5 \  
&& wget -qO /tmp/${SPLUNK_SDK_APP_COLLECTION_FILENAME}
${SPLUNK_SDK_APP_COLLECTION_URL}\  
&& apt-get purge -y --auto-remove wget \  
&& mkdir -p /var/opt/splunk \  
&& cp -R ${SPLUNK_HOME}/etc ${SPLUNK_BACKUP_DEFAULT_ETC} \  
&& tar -xf /tmp/${SPLUNK_SDK_APP_COLLECTION_FILENAME} \  
&& mv ${SPLUNK_SDK_APP_COLLECTION_NAME}-${SPLUNK_SDK_APP_COLLECTION_VERSION}
${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/${SPLUNK_SDK_APP_COLLECTION_NAME} \  
&& rm /tmp/${SPLUNK_SDK_APP_COLLECTION_FILENAME} \  
&& rm -fR ${SPLUNK_HOME}/etc \  
&& chown -R ${SPLUNK_USER}:${SPLUNK_GROUP} ${SPLUNK_HOME} \  
&& chown -R ${SPLUNK_USER}:${SPLUNK_GROUP} ${SPLUNK_BACKUP_DEFAULT_ETC} \  
&& rm -rf /var/lib/apt/lists/*  
  
# We need to enable remote login for the SDKs  
RUN mkdir -p ${SPLUNK_BACKUP_DEFAULT_ETC}/etc/system/local/  
RUN echo "[general]\nallowRemoteLogin=always" >>
${SPLUNK_BACKUP_DEFAULT_ETC}/etc/system/local/server.conf  
RUN echo "[sslConfig]\ncipherSuite = AES256-SHA" >>
${SPLUNK_BACKUP_DEFAULT_ETC}/etc/system/local/server.conf  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod +x /sbin/entrypoint.sh  
  
# Ports Splunk Web, Splunk Daemon, KVStore, Splunk Indexing Port, Network
Input, HTTP Event Collector  
# Also expose some ports for unit test  
EXPOSE 8000/tcp 8089/tcp 8191/tcp 9997/tcp 1514 8088/tcp 10666/tcp 10667/tcp
10668/tcp 10669/tcp 10666/udp 10667/udp 10668/udp 10669/udp  
  
WORKDIR /opt/splunk  
  
# Configurations folder, var folder for everyting (indexes, logs, kvstore)  
VOLUME [ "/opt/splunk/etc", "/opt/splunk/var" ]  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["start-service"]  

