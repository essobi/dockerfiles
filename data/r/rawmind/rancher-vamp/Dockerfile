FROM rawmind/rancher-jvm8:0.0.2-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV VAMP_VERSION=0.8.4 \  
VAMP_HOME=/opt/vamp \  
DOCKER_VERSION=1.9.1  
ENV VAMP_RELEASE=vamp-${VAMP_VERSION}.jar  
  
RUN mkdir -p ${VAMP_HOME}/log ${VAMP_HOME}/conf ${VAMP_HOME}/jar
${VAMP_HOME}/scripts && cd ${VAMP_HOME}/jar \  
&& wget https://bintray.com/artifact/download/magnetic-
io/downloads/vamp/${VAMP_RELEASE} \  
&& cd /tmp && curl
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION} -O \  
&& mv /tmp/docker-${DOCKER_VERSION} /usr/bin/docker && chmod 755
/usr/bin/docker  
  
# Add config files  
ADD root /  
RUN chmod +x ${VAMP_HOME}/scripts/*.sh  
  
WORKDIR /opt/vamp  
  
ENTRYPOINT ${VAMP_HOME}/scripts/start.sh  

