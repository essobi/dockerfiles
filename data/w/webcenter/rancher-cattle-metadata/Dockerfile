FROM alpine:3.5  
MAINTAINER Sebastien LANGOUREAUX (linuxworkgroup@hotmail.com)  
  
# Set environment  
ENV SCHEDULER_VOLUME=/opt/scheduler \  
SCHEDULER_ARCHIVE=/opt/scheduler.tgz  
  
  
# Install confd  
ENV CONFD_VERSION="0.11.0" \  
CONFD_HOME="/opt/confd"  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 ${SCHEDULER_VOLUME}/confd/bin/confd  
RUN \  
mkdir -p "${SCHEDULER_VOLUME}/confd/etc/conf.d"
"${SCHEDULER_VOLUME}/confd/etc/templates" &&\  
chmod +x "${SCHEDULER_VOLUME}/confd/bin/confd"  
  
# Add files  
ADD root /  
RUN \  
cd ${SCHEDULER_VOLUME} && \  
mkdir -p ${SCHEDULER_VOLUME}/conf && \  
tar czvf ${SCHEDULER_ARCHIVE} * && \  
rm -rf ${SCHEDULER_VOLUME}/* && \  
chmod +x /docker-entrypoint.sh  
  
VOLUME ["${SCHEDULER_VOLUME}"]  
ENTRYPOINT "/docker-entrypoint.sh"  

