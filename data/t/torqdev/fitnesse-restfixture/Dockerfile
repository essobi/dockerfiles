FROM openjdk:8-jdk-alpine  
MAINTAINER Christopher Guckes <christopher.guckes@torq-dev.de>  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN echo http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories  
RUN apk add --no-cache dos2unix  
  
RUN mkdir -p /opt/fitnesse  
RUN mkdir -p /opt/fitnesse-initial  
ADD . /opt/fitnesse  
ADD ./src/main/resources /opt/fitnesse-initial  
RUN chmod o+x /opt/fitnesse/start.sh  
RUN chmod o+x /opt/fitnesse/mvnw  
RUN dos2unix /opt/fitnesse/start.sh  
  
VOLUME /opt/fitnesse/src/main/resources  
VOLUME /opt/fitnesse/src/test/java  
WORKDIR /opt/fitnesse  
  
RUN ./mvnw clean install  
  
ENTRYPOINT ["/opt/fitnesse/start.sh"]

