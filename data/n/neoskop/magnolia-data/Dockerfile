FROM busybox  
MAINTAINER Neoskop DevOps "devops@neoskop.de"  
RUN mkdir -p /home/tomcat/magnolia_tmp/repositories && chown 100
/home/tomcat/magnolia_tmp/repositories  
VOLUME ["/home/tomcat/magnolia_tmp/repositories"]  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["mkdir -p /home/tomcat/magnolia_tmp/repositories; chown -R 100
/home/tomcat/magnolia_tmp/repositories"]  

