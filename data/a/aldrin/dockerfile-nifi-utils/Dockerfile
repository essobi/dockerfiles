# FROM apachenifi:1.1.1  
#  
# ADD ./sh/ /opt/nifi/sh  
# ADD nifi-toolkit-1.1.1-bin.tar.gz /opt/nifi/  
#  
# USER root  
# RUN apt-get update && \  
# apt-get install jq && \  
# chown -R nifi:nifi /opt/nifi  
#  
# USER nifi  
#  
# CMD ["/opt/nifi/sh/start.sh"]  
FROM java:8  
MAINTAINER Apache NiFi <dev@nifi.apache.org>  
  
ARG UID=500  
ARG GID=1000  
ARG NIFI_VERSION=1.3.0  
ENV NIFI_BASE_DIR /opt/nifi  
ENV NIFI_HOME $NIFI_BASE_DIR/nifi-${NIFI_VERSION}  
ENV NIFI_BINARY_URL
https://archive.apache.org/dist/nifi/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
# Setup NiFi user  
RUN groupadd -g $GID nifi || groupmod -n nifi `getent group $GID | cut -d:
-f1`  
RUN useradd --shell /bin/bash -u $UID -g $GID -m nifi  
RUN mkdir -p $NIFI_HOME  
  
ADD https://archive.apache.org/dist/nifi/${NIFI_VERSION}/nifi-
toolkit-${NIFI_VERSION}-bin.tar.gz /opt/nifi/  
RUN tar -xf /opt/nifi/nifi-toolkit-${NIFI_VERSION}-bin.tar.gz -C
${NIFI_BASE_DIR}  
  
# Download, validate, and expand Apache NiFi binary.  
RUN curl -fSL $NIFI_BINARY_URL -o
$NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz \  
&& echo "$(curl $NIFI_BINARY_URL.sha256)
*$NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz" | sha256sum -c - \  
&& tar -xvzf $NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz -C $NIFI_BASE_DIR
\  
&& rm $NIFI_BASE_DIR/nifi-${NIFI_VERSION}-bin.tar.gz \  
&& apt-get update \  
&& apt-get install jq  
  
RUN wget
https://github.com/outbrain/zookeepercli/releases/download/v1.0.10/zookeepercli_1.0.10_amd64.deb
\  
&& dpkg -i zookeepercli_1.0.10_amd64.deb  
  
# Web HTTP Port  
EXPOSE 8080 8443  
# Remote Site-To-Site Port  
EXPOSE 8181  
ADD ./sh/ /opt/nifi/sh  
  
RUN chown -R nifi:nifi /opt/nifi  
  
USER nifi  
  
# Startup NiFi  
CMD ${NIFI_BASE_DIR}/sh/start.sh  

