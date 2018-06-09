FROM ubuntu:14.04.3  
ENV TOMCAT_VERSION 7.0.39  
RUN apt-get -y update  
RUN apt-get install software-properties-common python-software-properties -y  
RUN add-apt-repository ppa:openjdk-r/ppa -y  
RUN apt-get -y update  
RUN apt-get install openjdk-8-jdk -y  
RUN apt-get install curl -y  
RUN apt-get install wget -y  
  
RUN curl --insecure -fsSL
https://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz | tar xzf - -C /  
RUN wget http://repo1.maven.org/maven2/com/github/toto-
castaldi/services/simple-smtp-server/1.0/simple-smtp-server-1.0.war && cp
/simple-smtp-server-1.0.war /smtp.war  
  
#COPY config/tomcat/lib/*.jar /  
COPY config/tomcat-$TOMCAT_VERSION/server.xml /  
#COPY target/*.war /  
COPY docker-entrypoint.sh /  
  
WORKDIR /data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8080 2525  
ENV REST_PORT 8080  
ENV SMTP_PORT 25  
CMD ["tomcat"]  

