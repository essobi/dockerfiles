# Confluent image  
# github.com/yeasy/docker-kafka  
# CONFLUENT_HOME=/opt/kafka  
# Add $CONFLUENT_HOME/bin to the $PATH.  
# workdir is set to $CONFLUENT_HOME  
FROM anapsix/alpine-java:8  
MAINTAINER <yeasy@github.com>  
  
ENV RELEASE_VERSION=3.3 \  
MAJOR_VERSION=3.3.0 \  
MINOR_VERSION=2.11  
ENV FULL_VERSION=${MAJOR_VERSION}-${MINOR_VERSION}  
  
ENV PKG_NAME=confluent-oss-${FULL_VERSION}.tar.gz  
  
ENV CONFLUENT_HOME=/opt/confluent  
  
ENV PATH=$PATH:${CONFLUENT_HOME}/bin  
  
# Download and install confluent  
RUN cd /tmp && \  
wget http://packages.confluent.io/archive/${RELEASE_VERSION}/${PKG_NAME} && \  
tar xzf ${PKG_NAME} -C /opt && \  
rm ${PKG_NAME} && \  
mv /opt/confluent-${MAJOR_VERSION} ${CONFLUENT_HOME}  
  
# Install necessary tools  
RUN set -ex && \  
apk upgrade --update && \  
apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
COPY scripts/* /tmp/  
  
WORKDIR $CONFLUENT_HOME  
  
# Start service  
CMD ["bash", "/tmp/start.sh"]  

