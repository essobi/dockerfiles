FROM ubuntu:14.04.3  
RUN apt-get -y update  
RUN apt-get install software-properties-common python-software-properties -y  
RUN add-apt-repository ppa:openjdk-r/ppa -y  
RUN apt-get -y update  
RUN apt-get install openjdk-8-jdk -y  
RUN apt-get install curl -y  
RUN apt-get install wget -y  
  
RUN wget
https://oss.sonatype.org/content/repositories/snapshots/com/github/toto-
castaldi/tap-the-mole/server/1.0-SNAPSHOT/server-1.0-20160420.190314-4.jar &&
cp /*.jar /server.jar  
  
COPY docker-entrypoint.sh /  
  
WORKDIR /data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8888  
ENV REST_PORT 8888  
CMD ["java"]  

