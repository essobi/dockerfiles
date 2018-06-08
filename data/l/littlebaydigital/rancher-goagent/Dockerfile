FROM rawmind/rancher-jvm8:0.0.2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV GOCD_VERSION=16.7.0 \  
GOCD_RELEASE=go-agent \  
GOCD_REVISION=3819 \  
GOCD_HOME=/opt/go-agent \  
PATH=$GOCD_HOME:$PATH  
ENV
GOCD_REPO=https://download.go.cd/binaries/${GOCD_VERSION}-${GOCD_REVISION}/generic
\  
GOCD_RELEASE_ARCHIVE=${GOCD_RELEASE}-${GOCD_VERSION}-${GOCD_REVISION}.zip \  
SERVER_WORK_DIR=${GOCD_HOME}/work  
  
# Install and configure gocd  
RUN apk add --update git && rm -rf /var/cache/apk/* \  
&& mkdir /var/log/go-agent /var/run/go-agent \  
&& cd /opt && curl -sSL ${GOCD_REPO}/${GOCD_RELEASE_ARCHIVE} -O && unzip
${GOCD_RELEASE_ARCHIVE} && rm ${GOCD_RELEASE_ARCHIVE} \  
&& mv /opt/${GOCD_RELEASE}-${GOCD_VERSION} ${GOCD_HOME} \  
&& chmod 774 ${GOCD_HOME}/*.sh \  
&& mkdir -p ${GOCD_HOME}/work  
  
# Add start script  
ADD start.sh /usr/bin/start.sh  
RUN chmod +x /usr/bin/start.sh  
  
WORKDIR ${GOCD_HOME}  
  
ENTRYPOINT ["/usr/bin/start.sh"]  

