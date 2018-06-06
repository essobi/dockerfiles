FROM opensuse:42.1  
MAINTAINER Yan Dongpeng <yandongpeng@qq.com>  
  
RUN zypper -n update \  
&& zypper -n install -y wget ca-certificates tar unzip\  
&& rm -rf /var/lib/apt/lists/*  
  
# Install IBM jre8  
ENV JAVA_VERSION=1.8.0_sr3fp12  
  
RUN ESUM="5248e1ece213033ffc3f80702736a1bb2ec2fcfc8e82f4c38322e8c5cf42bfe8" \  
&&
BASE_URL="https://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/meta/"
\  
&& YML_FILE="jre/linux/x86_64/index.yml" \  
&& wget -q -U UA_IBM_JAVA_Docker -O /tmp/index.yml $BASE_URL/$YML_FILE \  
&& JAVA_URL=$(cat /tmp/index.yml | sed -n '/'$JAVA_VERSION'/{n;p}' | sed -n
's/\s*uri:\s//p' | tr -d '\r') \  
&& wget -q -U UA_IBM_JAVA_Docker -O /tmp/ibm-java.bin $JAVA_URL \  
&& echo "$ESUM /tmp/ibm-java.bin" | sha256sum -c - \  
&& echo "INSTALLER_UI=silent" > /tmp/response.properties \  
&& echo "USER_INSTALL_DIR=/opt/ibm/java" >> /tmp/response.properties \  
&& echo "LICENSE_ACCEPTED=TRUE" >> /tmp/response.properties \  
&& mkdir -p /opt/ibm \  
&& chmod +x /tmp/ibm-java.bin \  
&& /tmp/ibm-java.bin -i silent -f /tmp/response.properties \  
&& rm -f /tmp/response.properties \  
&& rm -f /tmp/index.yml \  
&& rm -f /tmp/ibm-java.bin  
  
ENV JAVA_HOME=/opt/ibm/java/jre \  
PATH=/opt/ibm/java/jre/bin:$PATH  
  
# Install WebSphere Liberty  
ENV LIBERTY_VERSION=16.0.0_03  
ARG LIBERTY_URL  
ARG DOWNLOAD_OPTIONS=""  
RUN LIBERTY_URL=${LIBERTY_URL:-$(wget -q -O -
https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/wasdev/downloads/wlp/index.yml
| grep $LIBERTY_VERSION -A 6 | sed -n 's/\s*kernel:\s//p' | tr -d '\r' )} \  
&& wget $DOWNLOAD_OPTIONS $LIBERTY_URL -U UA-IBM-WebSphere-Liberty-Docker -O
/tmp/wlp.zip \  
&& unzip -q /tmp/wlp.zip -d /opt/ibm \  
&& rm /tmp/wlp.zip  
ENV PATH=/opt/ibm/wlp/bin:$PATH  
  
# Set Path Shortcuts  
ENV LOG_DIR=/logs \  
WLP_OUTPUT_DIR=/opt/ibm/wlp/output  
RUN mkdir /logs \  
&& ln -s $WLP_OUTPUT_DIR/defaultServer /output \  
&& ln -s /opt/ibm/wlp/usr/servers/defaultServer /config  
  
# Configure WebSphere Liberty  
RUN /opt/ibm/wlp/bin/server create \  
&& rm -rf $WLP_OUTPUT_DIR/.classCache /output/workarea  
COPY docker-server /opt/ibm/docker/  
EXPOSE 9080 9443  
CMD ["/opt/ibm/docker/docker-server", "run", "defaultServer"]  
  
#Profile7  
ARG REPOSITORIES_PROPERTIES=""  
COPY server.xml /config/  
  
RUN if [ ! -z $REPOSITORIES_PROPERTIES ]; then mkdir /opt/ibm/wlp/etc/ \  
&& echo $REPOSITORIES_PROPERTIES > /opt/ibm/wlp/etc/repositories.properties;
fi \  
&& installUtility install --acceptLicense webProfile-7.0 \  
&& if [ ! -z $REPOSITORIES_PROPERTIES ]; then rm
/opt/ibm/wlp/etc/repositories.properties; fi \  
&& rm -rf /output/workarea /output/logs  

