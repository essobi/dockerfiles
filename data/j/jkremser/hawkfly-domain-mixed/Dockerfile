FROM hawkular/wildfly-hawkular-agent-domain:latest  
  
MAINTAINER Jirka Kremser <jkremser@redhat.com>  
  
USER root  
RUN echo "* hard nofile 64000" >> /etc/security/limits.conf  
USER jboss  
  
EXPOSE 8080 8180 18080 18180 9990  

