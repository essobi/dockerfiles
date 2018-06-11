  
# Dockerfile spring-boot  
# VERSION 1.1  
  
FROM jeanblanchard/busybox-java:8  
  
MAINTAINER Vadim Bauer <hello@z-rechnung.de>  
  
# the spring boot version  
ENV SPRING_BOOT_VERSION 1.2.0.RELEASE  
  
RUN \  
mkdir /opt/spring-boot && \  
cd /opt/spring-boot && \  
wget http://repo1.maven.org/maven2/org/springframework/boot/spring-boot-
cli/${SPRING_BOOT_VERSION}/spring-boot-cli-${SPRING_BOOT_VERSION}-full.jar &&
\  
ln -s spring-boot-cli-${SPRING_BOOT_VERSION}-full.jar spring-boot && \  
echo -e '#!/bin/sh \njava -jar /opt/spring-boot/spring-boot "$@"' >
/usr/bin/spring-boot && \  
chmod 751 /usr/bin/spring-boot;  
  
ENTRYPOINT ["spring-boot"]  
  
  

