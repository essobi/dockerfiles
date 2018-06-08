FROM fedora  
#FROM registry.access.redhat.com/rhel7.1  
MAINTAINER Luigi Fugaro <lfugaro@redhat.com>  
  
RUN dnf -y update && dnf clean all  
  
RUN dnf install -y wget telnet findutils zip tar unzip mlocate  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.rpm  
  
RUN dnf -y install findutils  
  
RUN rpm -ivh jdk-8u92-linux-x64.rpm  
RUN rm -rf jdk-8u92-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/jdk1.8.0_92  
ENV JAVA_OPTS $JAVA_OPTS -Xms512m -Xmx1024m  
  
RUN mkdir /opt/rh  
  
WORKDIR /opt/rh  
  
ADD jboss-eap-6.4.0.zip /opt/rh/  
  
RUN unzip jboss-eap-6.4.0.zip  
  
RUN rm -rf jboss-eap-6.4.0.zip  
  
WORKDIR /opt/rh/jboss-eap-6.4  
  
RUN chmod -R 777 *  
  
ADD jboss-spring-resteasy.war /opt/rh/jboss-eap-6.4/standalone/deployments/  
  
### Open Ports  
EXPOSE 8080 9990 9999  
RUN ./bin/add-user.sh --silent=true admin admin123!  
  
ENTRYPOINT ["./bin/standalone.sh"]  
  
CMD ["-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]

