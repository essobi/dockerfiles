FROM openjdk:8  
MAINTAINER Stephen Price <stephen@stp5.net>  
  
ENV RDECK_VER=2.7.1 \  
RDECK_SHA=0c75c648e3f7bdf8e3a822fb6986f688674ebd1a \  
RDECK_BASE=/rundeck \  
PATH=/rundeck/tools/bin:${PATH} \  
RDECK_HOSTNAME=127.0.0.1 \  
RDECK_UID=350 \  
RDECK_GID=350  
RUN groupadd -r -g ${RDECK_GID} rundeck \  
&& useradd -r -g rundeck -u ${RDECK_UID} -m -d ${RDECK_BASE} rundeck \  
&& cd ${RDECK_BASE} \  
&& mkdir -p ${RDECK_BASE}/etc \  
&& mkdir -p ${RDECK_BASE}/var \  
&& mkdir -p ${RDECK_BASE}/projects \  
&& mkdir -p ${RDECK_BASE}/server/config \  
&& mkdir -p ${RDECK_BASE}/server/data \  
&& chown -R rundeck.rundeck ${RDECK_BASE} \  
&& curl -sL -o ${RDECK_BASE}/rundeck.jar \  
https://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-${RDECK_VER}.jar
\  
&& echo "${RDECK_SHA} rundeck.jar" > ${RDECK_BASE}/rundeck.sig \  
&& shasum -c ${RDECK_BASE}/rundeck.sig \  
&& rm -f ${RDECK_BASE}/rundeck.sig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER rundeck  
  
WORKDIR ${RDECK_BASE}  
  
EXPOSE 4440  
CMD ["java", "-Dserver.hostname=${RDECK_HOSTNAME}", "-jar", "rundeck.jar"]  

