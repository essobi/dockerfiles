FROM blacklabelops/java:server-jre.8  
  
ENV MAVEN3_VERSION 3.3.9  
  
RUN apk add \--update curl ca-certificates openssh-client git && \  
curl \--silent
https://archive.apache.org/dist/maven/maven-3/${MAVEN3_VERSION}/binaries/apache-
maven-${MAVEN3_VERSION}-bin.tar.gz | tar -xz -C /opt && \  
ln -s /opt/apache-maven-${MAVEN3_VERSION}/bin/mvn /usr/local/bin && \  
apk del curl ca-certificates && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*  
  

