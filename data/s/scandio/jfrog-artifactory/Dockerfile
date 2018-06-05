FROM docker.bintray.io/jfrog/artifactory-pro:5.0.1  
MAINTAINER Scandio GmbH  
  
ENV IMPORTCERT false  
ENV IMPORTPATH /var/certificates  
  
COPY configure-and-start.sh /tmp/  
RUN chown 500 /tmp/configure-and-start.sh  
RUN mkdir ${IMPORTPATH}  
  
VOLUME ["/var/opt/jfrog/artifactory/access"]  
VOLUME ["/var/opt/jfrog/artifactory/backup"]  
VOLUME ["/var/opt/jfrog/artifactory/data"]  
VOLUME ["/var/opt/jfrog/artifactory/etc"]  
VOLUME ["/var/opt/jfrog/artifactory/logs"]  
  
# HTTP Port  
EXPOSE 80  
EXPOSE 443  
EXPOSE 5000  
EXPOSE 5001  
EXPOSE 5002  
EXPOSE 8081  
CMD ["/tmp/configure-and-start.sh"]

