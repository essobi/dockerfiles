FROM java:8u92-jdk-alpine  
  
RUN \  
apk add --update bash git && rm -rf /var/cache/apk/* && \  
wget http://ftp.fau.de/apache/maven/maven-3/3.3.1/binaries/apache-
maven-3.3.1-bin.tar.gz && \  
tar -zxvf apache-maven-3.3.1-bin.tar.gz && \  
rm apache-maven-3.3.1-bin.tar.gz && \  
mv apache-maven-3.3.1 /usr/lib/mvn  
  
# RUNTIME  
ADD docker-entrypoint /docker-entrypoint  
ADD docker-entrypoint.d /docker-entrypoint.d  
ENTRYPOINT ["/docker-entrypoint"]  

