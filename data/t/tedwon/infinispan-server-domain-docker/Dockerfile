# Use latest jboss/base-jdk:8 image as the base  
FROM jboss/base-jdk:8  
# Set the INFINISPAN_SERVER_HOME env variable  
ENV INFINISPAN_SERVER_HOME /opt/jboss/infinispan-server  
  
# Set the INFINISPAN_VERSION env variable  
ENV INFINISPAN_VERSION 8.2.1.Final  
  
ENV DOMAIN_USER admin  
ENV DOMAIN_PASS admin  
  
# Download and unzip Infinispan server  
RUN cd $HOME && curl
"https://repo1.maven.org/maven2/org/infinispan/server/infinispan-server-
build/$INFINISPAN_VERSION/infinispan-server-build-$INFINISPAN_VERSION.zip" |
bsdtar -xf - && mv $HOME/infinispan-server-$INFINISPAN_VERSION
$HOME/infinispan-server && chmod +x /opt/jboss/infinispan-server/bin/*.sh  
  
COPY start.sh /opt/jboss/infinispan-server/bin/  
  
USER root  
  
RUN yum -y install telnet iproute && yum clean all  
  
RUN sed -i '/other-server-group/,+6d' /opt/jboss/infinispan-
server/domain/configuration/host.xml  
RUN sed -i '/other-server-group/,+6d' /opt/jboss/infinispan-
server/domain/configuration/host-slave.xml  
RUN sed -i '/server-two/,+6d' /opt/jboss/infinispan-
server/domain/configuration/host.xml  
  
# Expose Infinispan server ports  
EXPOSE 57600 7600 8080 8181 9990 11211 11222  
CMD ["/opt/jboss/infinispan-server/bin/start.sh"]  

