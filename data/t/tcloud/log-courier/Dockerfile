# tcloud/log-courier  
# VERSION 0.1  
FROM tcloud/base  
MAINTAINER tcloud  
  
USER root  
  
ADD driskell-log-courier-epel-7.repo /etc/yum.repos.d/driskell-log-courier-
epel-7.repo  
  
RUN yum install -y log-courier  
  
VOLUME ["/etc/log-courier","/data","/log"]  
  
# We use the "sh -c" to turn around
https://github.com/docker/docker/issues/5509 - variable not expanded  
ENTRYPOINT ["sh", "-c"]  
  
CMD ["/usr/sbin/log-courier"]

