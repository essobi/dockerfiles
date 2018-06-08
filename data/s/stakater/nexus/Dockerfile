FROM stakater/java8-alpine:1.8.0_121  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
  
ARG NEXUS_VERSION=2.14.4-03  
ARG
NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/oss/nexus-${NEXUS_VERSION}-bundle.tar.gz  
  
ENV NEXUS_PATH=/opt/sonatype/nexus  
# Install Nexus  
RUN apk -Uuv add curl && \  
mkdir -p ${NEXUS_PATH} \  
&& curl --fail --location --retry 3 ${NEXUS_DOWNLOAD_URL} \  
| gunzip \  
| tar x -C /tmp nexus-${NEXUS_VERSION} \  
&& mv /tmp/nexus-${NEXUS_VERSION}/* ${NEXUS_PATH}/ \  
&& rm -rf /tmp/nexus-${NEXUS_VERSION}  
  
ENV SONATYPE_WORK /sonatype-work  
ENV CONTEXT_PATH /nexus  
ENV MAX_HEAP 768m  
ENV MIN_HEAP 256m  
ENV JAVA_OPTS -server -Djava.net.preferIPv4Stack=true  
ENV LAUNCHER_CONF ./conf/jetty.xml ./conf/jetty-requestlog.xml  
  
# Make daemon service dir for nexus and place file  
# It will be started and maintained by the base image  
RUN mkdir -p /etc/service/nexus  
ADD start.sh /etc/service/nexus/run  
  
EXPOSE 8081  
WORKDIR ${NEXUS_PATH}  
VOLUME ${SONATYPE_WORK}

