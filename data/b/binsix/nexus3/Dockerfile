FROM binsix/openjdk:latest  
MAINTAINER LiuBin  
LABEL name="nexus3" license="MIT" build-date="20170813"  
  
ENV SONATYPE_DIR=/data/softs  
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus  
ENV NEXUS_DATA=/data/env/nexus  
ENV NEXUS_CONTEXT=''  
ENV SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work  
  
ENV NEXUS_VERSION=3.5.0-02  
ENV
NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz  
  
RUN yum update -y && mkdir -p ${NEXUS_HOME} && curl --fail --silent --location
--retry 3 ${NEXUS_DOWNLOAD_URL} | gunzip | tar x -C ${NEXUS_HOME} \--strip-
components=1 nexus-${NEXUS_VERSION} && chown -R root:root ${NEXUS_HOME} && sed
-e '/^nexus-context/ s:$:${NEXUS_CONTEXT}:' -i ${NEXUS_HOME}/etc/nexus-
default.properties && sed -e '/^-Xms/d' -e '/^-Xmx/d' -i
${NEXUS_HOME}/bin/nexus.vmoptions && useradd -r -u 200 -m -c "account of nexus
role" -d ${NEXUS_DATA} -s /bin/false nexus && mkdir -p ${NEXUS_DATA}/etc
${NEXUS_DATA}/log ${NEXUS_DATA}/tmp ${SONATYPE_WORK} && ln -s ${NEXUS_DATA}
${SONATYPE_WORK}/nexus3 && chown -R nexus:nexus ${NEXUS_DATA}  
  
VOLUME ${NEXUS_DATA}  
  
EXPOSE 8081  
USER nexus  
  
WORKDIR ${NEXUS_HOME}  
  
ENV INSTALL4J_ADD_VM_PARAMS="-Xms1200m -Xmx1200m"  
CMD ["bin/nexus", "run"]

