from apache/nifi:1.4.0  
FROM openjdk:8-jre  
LABEL maintainer "Apache NiFi <dev@nifi.apache.org>"  
  
ARG UID=1000  
ARG GID=1000  
ARG NIFI_VERSION=1.4.0  
ARG MIRROR=https://archive.apache.org/dist  
  
ENV NIFI_BASE_DIR /opt/nifi  
ENV NIFI_HOME=$NIFI_BASE_DIR/nifi-$NIFI_VERSION \  
NIFI_BINARY_URL=/nifi/$NIFI_VERSION/nifi-$NIFI_VERSION-bin.tar.gz \  
NIFI_DATA_DIR=/opt/data  
  
# Setup NiFi user  
RUN groupadd -g $GID nifi || groupmod -n nifi `getent group $GID | cut -d:
-f1` \  
&& useradd --shell /bin/bash -u $UID -g $GID -m nifi \  
&& mkdir -p $NIFI_HOME/conf \  
&& chown -R nifi:nifi $NIFI_BASE_DIR  
  
#Create data dirs  
RUN mkdir -p ${NIFI_DATA_DIR}/data/templates \  
&& mkdir -p ${NIFI_DATA_DIR}/database_repository \  
&& mkdir -p ${NIFI_DATA_DIR}/flowfile_repository \  
&& mkdir -p ${NIFI_DATA_DIR}/content_repository \  
&& mkdir -p ${NIFI_DATA_DIR}/provenance_repository \  
&& mkdir -p ${NIFI_DATA_DIR}/logs \  
&& chown -R nifi:nifi ${NIFI_DATA_DIR}  
  
USER nifi  
  
# Download, validate, and expand Apache NiFi binary.  
RUN curl -fSL $MIRROR/$NIFI_BINARY_URL -o $NIFI_BASE_DIR/nifi-$NIFI_VERSION-
bin.tar.gz \  
&& echo "$(curl https://archive.apache.org/dist/$NIFI_BINARY_URL.sha256)
*$NIFI_BASE_DIR/nifi-$NIFI_VERSION-bin.tar.gz" | sha256sum -c - \  
&& tar -xvzf $NIFI_BASE_DIR/nifi-$NIFI_VERSION-bin.tar.gz -C $NIFI_BASE_DIR \  
&& rm $NIFI_BASE_DIR/nifi-$NIFI_VERSION-bin.tar.gz \  
&& chown -R nifi:nifi $NIFI_HOME  
  
COPY lib/* ${NIFI_HOME}/lib/  
  
COPY conf/* ${NIFI_HOME}/conf/  
  
#RUN chown -R nifi:nifi ${NIFI_HOME}/lib/*  
# Web HTTP Port & Remote Site-to-Site Ports  
EXPOSE 8080 8181  
WORKDIR $NIFI_HOME  
  
# Startup NiFi  
ENTRYPOINT ["bin/nifi.sh"]  
CMD ["run"]  
  

