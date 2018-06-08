# tcloud/packetbeat  
# VERSION 0.1  
FROM tcloud/base  
MAINTAINER tcloud  
  
USER root  
  
ENV BASE_DIR /usr/local/packetbeat  
ENV PACKETBEAT_HOME ${BASE_DIR}/current  
ENV PATH ${PACKETBEAT_HOME}:$PATH  
  
ENV VERSION 1.0.0-rc2  
ENV TARBALL_DIR packetbeat-${VERSION}-x86_64  
ENV TARBALL ${TARBALL_DIR}.tar.gz  
  
RUN mkdir -p ${BASE_DIR} && \  
cd ${BASE_DIR} && \  
curl -O --silent https://download.elastic.co/beats/packetbeat/${TARBALL} && \  
sleep 200  
  
RUN tar xzf ${BASE_DIR}/${TARBALL} -C ${BASE_DIR} && \  
ln -s ${BASE_DIR}/${TARBALL_DIR} ${BASE_DIR}/current && \  
rm -f ${BASE_DIR}/${TARBALL}  
  
WORKDIR /usr/local/packetbeat/current  
  
VOLUME ["/data","/log"]  
  
# We use the "sh -c" to turn around
https://github.com/docker/docker/issues/5509 - variable not expanded  
# ENTRYPOINT ["sh", "-c"]  
CMD ["/usr/local/packetbeat/current/packetbeat -c
/data/config/packetbeat.yml"]

