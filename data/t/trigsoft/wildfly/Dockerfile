FROM jboss/wildfly:10.0.0.Final  
MAINTAINER ijazfx <ijazfx@gmail.com>  
  
USER root  
  
RUN yum -y update  
  
USER jboss  
  
ADD driver/*.jar /tmp/  
ADD add-users.sh /tmp/  
RUN /tmp/add-users.sh  
  
ADD config.sh /tmp/  
ADD batch.cli /tmp/  
RUN /tmp/config.sh  
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history  
  
EXPOSE 8080 9990  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-c", "standalone-full.xml",
"-b", "0.0.0.0"]  

