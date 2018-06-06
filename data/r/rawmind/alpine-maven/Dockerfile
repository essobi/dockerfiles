FROM rawmind/alpine-jdk8:1.8.112-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV MAVEN_MAJOR=3 \  
MAVEN_VERSION=3.3.9 \  
MAVEN_HOME=/opt/apache-maven  
ENV MAVEN_URI=maven/maven-${MAVEN_MAJOR}/${MAVEN_VERSION}/binaries \  
MAVEN_FILE=apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
PATH=${PATH}:${MAVEN_HOME}/bin  
  
# Download and install Maven  
RUN cd /tmp && \  
apk add --no-cache git jq gnupg && \  
eval $(gpg-agent --daemon) && \  
MIRROR=`curl -sS https://www.apache.org/dyn/closer.cgi\?as_json\=1 | jq -r
'.preferred'` && \  
curl -sSLO "${MIRROR}${MAVEN_URI}/${MAVEN_FILE}" && \  
curl -sSLO "https://www.apache.org/dist/${MAVEN_URI}/${MAVEN_FILE}.asc" && \  
curl -sSL https://dist.apache.org/repos/dist/release/maven/KEYS | gpg -v
--import - && \  
gpg -v --verify ${MAVEN_FILE}.asc && \  
mkdir -p ${MAVEN_HOME} && \  
tar -zx -C ${MAVEN_HOME} \--strip-components=1 \--no-same-owner -f
${MAVEN_FILE} && \  
apk del jq gnupg && \  
rm -rf \  
/tmp/* \  
/root/.gnupg  

