FROM nukesz/java:latest  
MAINTAINER Norbert Benczur, norbert.benczur@gmail.com  
ENV WILDFLY_VERSION 10.0.0.Final  
ENV WILDFLY_HOME /opt/wildfly-${WILDFLY_VERSION}  
RUN wget
http://download.jboss.org/wildfly/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz  
RUN tar -zxvf wildfly-${WILDFLY_VERSION}.tar.gz -C /opt && rm
wildfly-${WILDFLY_VERSION}.tar.gz  
ENTRYPOINT ${WILDFLY_HOME}/bin/standalone.sh -b=0.0.0.0  
EXPOSE 8080

