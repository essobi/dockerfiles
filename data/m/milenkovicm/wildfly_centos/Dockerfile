FROM centos:7.1.1503  
MAINTAINER Marko Milenkovic  
  
USER root  
  
RUN yum -y install tar java-1.8.0-openjdk java-1.8.0-openjdk-headless && yum
clean all  
RUN useradd -ms /bin/bash jboss  
  
ENV WILDFLY_VERSION 8.2.0.Final  
ENV JAVA_HOME /usr/lib/jvm/jre/  
ENV JBOSS_HOME /opt/wildfly-$WILDFLY_VERSION  
ENV DEPLOYMENTS $JBOSS_HOME/standalone/deployments/  
  
RUN mkdir $JBOSS_HOME  
RUN chown jboss $JBOSS_HOME  
  
USER jboss  
  
RUN cd /opt/ && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx  
  
EXPOSE 8080  
WORKDIR $JBOSS_HOME/bin/  
CMD ["./standalone.sh", "-b", "0.0.0.0", "-c", "standalone-full.xml"]  
  

