FROM alpine:3.2  
  
MAINTAINER "Aaron Walker" <a.walker@base2services.com>  
  
RUN adduser -h /var/maven -u 1000 -D -s /bin/bash maven && mkdir -p
/var/maven/.m2/repository && chown -R maven:maven /var/maven/  
  
USER maven  
  
VOLUME ["/var/maven"]  
  
CMD ["true"]  

