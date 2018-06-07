FROM indigo/centos-jdk8:latest  
MAINTAINER Ronny Trommer <ronny@no42.org>  
  
ENV HAWTIO_VERSION 1.4.65  
ENV HAWTIO_HOME /opt/hawtio  
ENV HAWTIO_PORT 8090  
RUN mkdir -p ${HAWTIO_HOME} && \  
curl https://oss.sonatype.org/content/repositories/public/io/hawt/hawtio-
app/${HAWTIO_VERSION}/hawtio-app-${HAWTIO_VERSION}.jar -o
${HAWTIO_HOME}/hawtio-app.jar  
  
WORKDIR ${HAWTIO_HOME}  
  
CMD /usr/bin/java -jar hawtio-app.jar --port ${HAWTIO_PORT}  
  
EXPOSE 8090  

