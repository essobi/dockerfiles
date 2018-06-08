FROM rawmind/rancher-jvm8:0.0.2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV GOCD_VERSION=16.7.0 \  
GOCD_RELEASE=go-server \  
GOCD_REVISION=3819 \  
GOCD_HOME=/opt/go-server \  
PATH=$GOCD_HOME:$PATH  
ENV
GOCD_REPO=https://download.go.cd/binaries/${GOCD_VERSION}-${GOCD_REVISION}/generic
\  
GOCD_RELEASE_ARCHIVE=${GOCD_RELEASE}-${GOCD_VERSION}-${GOCD_REVISION}.zip \  
SERVER_WORK_DIR=${GOCD_HOME}/work \  
GOCD_USER_FILE=${SERVER_WORK_DIR}/users.htpasswd  
  
# Install and configure gocd  
RUN apk add --update git apache2-utils && rm -rf /var/cache/apk/* \  
&& mkdir /var/log/go-server /var/run/go-server \  
&& cd /opt && curl -sSL ${GOCD_REPO}/${GOCD_RELEASE_ARCHIVE} -O && unzip
${GOCD_RELEASE_ARCHIVE} && rm ${GOCD_RELEASE_ARCHIVE} \  
&& mv /opt/${GOCD_RELEASE}-${GOCD_VERSION} ${GOCD_HOME} \  
&& chmod 774 ${GOCD_HOME}/*.sh  
  
# Add start script  
ADD start.sh /usr/bin/start.sh  
RUN chmod +x /usr/bin/start.sh  
  
WORKDIR ${GOCD_HOME}  
  
ENTRYPOINT ["/usr/bin/start.sh"]  

