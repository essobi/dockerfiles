FROM anapsix/alpine-java:8  
  
ENV NEXUS_VERSION=3.2.0-01 \  
PATH=$PATH:/opt/nexus/bin  
  
RUN apk add \--no-cache curl tar && \  
mkdir -p /opt/nexus && \  
curl -sL
"http://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz" |
tar xz -C /opt/nexus \--strip-components=1  
  
EXPOSE 8081  
  
VOLUME /opt/nexus/data  
  
CMD nexus run  

