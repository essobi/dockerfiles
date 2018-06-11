FROM frolvlad/alpine-glibc  
  
USER root  
  
ENV JAVA_HOME /usr/local/java  
ENV JRE ${JAVA_HOME}/jre  
ENV JAVA_OPTS=-Djava.awt.headless=true
PATH=${PATH}:${JRE}/bin:${JAVA_HOME}/bin  
  
RUN \  
echo ipv6 >> /etc/modules && \  
apk add --update ca-certificates curl && \  
mkdir -p /tmp/java && cd /tmp/java && \  
curl -Lo zre.txz https://github.com/delitescere/docker-
zulu/blob/master/jre/zre1.8.0_60-8.9.0.4-compact3-x86lx64.txz\?raw\=true && \  
tar -xJf zre.txz && rm zre.txz && \  
mkdir -p $(dirname ${JRE}) && \  
mv * ${JRE} && \  
cd / && \  
apk del ca-certificates curl && \  
rm -rf /tmp/* /var/cache/apk/* && \  
java -version  
  

