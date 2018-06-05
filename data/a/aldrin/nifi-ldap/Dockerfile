FROM java:8-jre  
MAINTAINER Apache NiFi <dev@nifi.apache.org>  
  
ARG UID=1000  
ARG GID=1000  
ARG NIFI_VERSION=1.3.0  
ENV NIFI_BASE_DIR /opt/nifi  
ENV NIFI_HOME $NIFI_BASE_DIR/nifi-${NIFI_VERSION}  
ENV NIFI_BINARY_URL
https://archive.apache.org/dist/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
  
# Setup NiFi user  
RUN groupadd -g $GID nifi || groupmod -n nifi `getent group $GID | cut -d:
-f1` \  
&& useradd --shell /bin/bash -u $UID -g $GID -m nifi \  
&& mkdir -p $NIFI_HOME/conf/templates \  
&& chown -R nifi:nifi $NIFI_BASE_DIR  
  
ADD resources/nifi-toolkit-${NIFI_VERSION}-bin.tar.gz /opt/nifi/  
  
# Download, validate, and expand Apache NiFi binary.  
RUN curl -fSL $NIFI_BINARY_URL -o
$NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz \  
&& echo "$(curl $NIFI_BINARY_URL.sha256)
*$NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz" | sha256sum -c - \  
&& tar -xvzf $NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz -C $NIFI_BASE_DIR
\  
&& rm $NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz \  
&& chown -R nifi:nifi ${NIFI_BASE_DIR} \  
&& apt-get update \  
&& apt-get install -y jq xmlstarlet  
  
USER nifi  
  
# Web HTTP, HTTPS, and Remote Site-To-Site Ports  
EXPOSE 8080 8181 8443  
ADD ./sh/ /opt/nifi/sh  
  
# Startup NiFi  
CMD ${NIFI_BASE_DIR}/sh/start.sh  

