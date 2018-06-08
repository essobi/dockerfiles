FROM ubuntu:trusty  
MAINTAINER Tomas Markauskas <tomas@markauskas.lt>  
  
RUN apt-get -y update && apt-get -y install syslog-ng syslog-ng-core  
  
ADD syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
  
RUN mkdir -p /srv/syslog  
  
CMD ["syslog-ng", "--foreground", "--stderr", "--no-caps"]  

