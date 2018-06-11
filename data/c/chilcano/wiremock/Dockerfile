# Dockerfile to create a Mock server container for SOAP/REST services using
Wiremock  
#  
# Usage:  
#  
# Previous steps:  
# 1) $ git clone https://github.com/chilcano/docker-wso2-dev-srv.git  
# 2) $ cd docker-wso2-dev-srv  
# 3) Download manually
'https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/${WIREMOCK_VERSION}/${WIREMOCK_BUNDLE}.jar'  
# 4) Copy the JAR file into 'wiremock/<WIREMOCK_VERSION>/assets/_downloads'  
#  
# Build image:  
# $ docker build --rm -t chilcano/wiremock:2.0.6-beta wiremock/2.0.6-beta  
#  
# Run container:  
# $ docker run -d -t --name=wiremock -p 18080:8080 -p 18443:8443
chilcano/wiremock:2.0.6-beta  
#  
# Run container sharing a host folder:  
# $ git clone https://github.com/chilcano/wso2-ei-patterns.git  
# $ docker run -d -t -v $PWD/../wso2-ei-patterns/wiremock-
stubs:/opt/wiremock/stubs --name=wiremock -p 18080:8080 -p 18443:8443
chilcano/wiremock:2.0.6-beta  
#  
# Check the Wiremock server:  
# $ docker exec -i -t wiremock bash  
# root@3031f21fcad3:/opt/wiremock# tail -f logs/wiremock.log  
#  
# $ curl -v http://192.168.99.100:18080/__admin/  
# $ curl -v -k https://192.168.99.100:18443/__admin/  
#  
# Stop and start Wiremock server:  
# $ docker restart wiremock  
# or  
# $ docker exec -i -t wiremock bash  
# root@3031f21fcad3:/opt/wiremock# cd bin  
# root@3031f21fcad3:/opt/wiremock/bin# ./wiremock.sh stop  
#  
# Base image with Java  
FROM java:openjdk-7  
MAINTAINER Roger CARHUATOCTO <chilcano at intix dot info>  
  
ENV WIREMOCK_VERSION=2.0.6-beta  
ENV WIREMOCK_BUNDLE=wiremock-standalone-${WIREMOCK_VERSION}  
ENV WIREMOCK_FOLDER=/opt/wiremock  
ENV WIREMOCK_PORT_HTTP=8080  
ENV WIREMOCK_PORT_HTTPS=8443  
ENV WIREMOCK_ARGS="--root-dir ${WIREMOCK_FOLDER}/stubs --port
${WIREMOCK_PORT_HTTP} --https-port ${WIREMOCK_PORT_HTTPS} --verbose"  
ENV JAVA_HOME=/usr  
  
RUN mkdir -p ${WIREMOCK_FOLDER}/bin  
RUN mkdir -p ${WIREMOCK_FOLDER}/stubs  
RUN mkdir -p ${WIREMOCK_FOLDER}/logs  
  
RUN wget -q -P ${WIREMOCK_FOLDER}/bin
https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/${WIREMOCK_VERSION}/${WIREMOCK_BUNDLE}.jar  
COPY assets/_files/wiremock.sh ${WIREMOCK_FOLDER}/bin/wiremock.sh  
RUN chmod 755 ${WIREMOCK_FOLDER}/bin/wiremock.sh  
  
# Ports HTTP and HTTPS  
EXPOSE ${WIREMOCK_PORT_HTTP} ${WIREMOCK_PORT_HTTPS}  
  
# Expose stubs folder ('__files' and 'mappings') to Host  
VOLUME ["${WIREMOCK_FOLDER}/stubs"]  
  
# Working Directory in Container  
WORKDIR ${WIREMOCK_FOLDER}  
  
# Start Wiremock  
CMD java -jar bin/${WIREMOCK_BUNDLE}.jar ${WIREMOCK_ARGS} > logs/wiremock.log

