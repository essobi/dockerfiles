FROM beevelop/java  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
ENV DIST_MIRROR="https://archive.apache.org/dist/nifi/" \  
NIFI_HOME="/opt/nifi"\  
NIFI_VERSION=0.4.1  
WORKDIR /opt  
  
COPY init.sh /opt/init.sh  
  
RUN apt-get -qq update && apt-get -qq install -y curl && \  
mkdir -p /opt/nifi && \  
chmod +x init.sh && \  
curl ${DIST_MIRROR}/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz | tar xz
-C ${NIFI_HOME} \--strip-components=1 && \  
sed -i -e "s|^nifi.ui.banner.text=.*$|nifi.ui.banner.text=Docker NiFi
${NIFI_VERSION}|" ${NIFI_HOME}/conf/nifi.properties  
  
EXPOSE 80 443  
VOLUME ["/opt/certs", "${NIFI_HOME}/flowfile_repository",
"${NIFI_HOME}/database_repository", "${NIFI_HOME}/content_repository",
"${NIFI_HOME}/provenance_repository"]  
  
CMD ["./init.sh"]  

