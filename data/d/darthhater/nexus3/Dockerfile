FROM ubuntu:yakkety  
  
MAINTAINER Jeffry Hesse <jeffryxtron+docker@gmail.com>  
  
ARG NEXUS_VERSION=3.3.0-01  
ARG
NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz  
ARG BUILD_DEPENDENCIES="curl tar"  
RUN apt-get update && apt-get install -y \  
${BUILD_DEPENDENCIES} \  
&& apt-get clean ${BUILD_DEPENDENCIES}  
  
# configure java runtime  
ENV JAVA_HOME=/opt/java \  
JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=112 \  
JAVA_VERSION_BUILD=15  
# configure nexus runtime  
ENV SONATYPE_DIR=/opt/sonatype  
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus \  
NEXUS_DATA=/nexus-data \  
NEXUS_CONTEXT='' \  
SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work  
  
# install Oracle JRE  
RUN mkdir -p /opt \  
&& curl --fail --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie; " \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/server-
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
| gunzip \  
| tar -x -C /opt \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}  
  
# install nexus  
RUN mkdir -p ${NEXUS_HOME} \  
&& curl --fail --silent --location --retry 3 \  
${NEXUS_DOWNLOAD_URL} \  
| gunzip \  
| tar x -C ${NEXUS_HOME} \--strip-components=1 nexus-${NEXUS_VERSION} \  
&& chown -R root:root ${NEXUS_HOME}  
  
# configure nexus  
RUN sed \  
-e '/^nexus-context/ s:$:${NEXUS_CONTEXT}:' \  
-i ${NEXUS_HOME}/etc/nexus-default.properties \  
&& sed \  
-e '/^-Xms/d' \  
-e '/^-Xmx/d' \  
-i ${NEXUS_HOME}/bin/nexus.vmoptions  
  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${NEXUS_DATA} -s
/bin/false nexus \  
&& mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp
${SONATYPE_WORK} \  
&& ln -s ${NEXUS_DATA} ${SONATYPE_WORK}/nexus3 \  
&& chown -R nexus:nexus ${NEXUS_DATA}  
  
VOLUME ${NEXUS_DATA}  
  
EXPOSE 8081  
USER nexus  
WORKDIR ${NEXUS_HOME}  
  
CMD ["bin/nexus", "run"]  

