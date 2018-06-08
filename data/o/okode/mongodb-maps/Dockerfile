# MongoDB Maps - Web Container  
FROM ubuntu:latest  
  
MAINTAINER Okode <support@okode.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TERM linux  
  
RUN apt-get -y update  
  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -y update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get -y -q install oracle-java8-installer  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY source /source  
RUN cd source && \  
./gradlew build  
  
RUN mkdir /mongodb-maps && cp /source/build/libs/mongodb-maps.jar /mongodb-
maps/  
  
EXPOSE 8080  
CMD /mongodb-maps/mongodb-maps.jar \  
\--logging.file=/var/logs/mongodb-maps/mongodb-maps.log \  
\--server.tomcat.accesslog.enabled=true \  
\--server.tomcat.accesslog.directory=/var/logs/mongodb-maps \  
\--server.tomcat.accesslog.prefix=tomcat.access_log  

