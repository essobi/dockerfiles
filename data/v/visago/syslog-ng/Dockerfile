FROM centos:7  
RUN yum -y install epel-release && yum -y update && \  
yum -y install syslog-ng  
RUN mkdir -p /var/log/syslog  
  
EXPOSE 514/udp  
COPY syslog-ng.conf /etc/syslog-ng  
ENTRYPOINT ["syslog-ng","-F","-f","/etc/syslog-ng/syslog-ng.conf"]  

