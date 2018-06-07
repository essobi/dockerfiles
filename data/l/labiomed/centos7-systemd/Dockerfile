FROM labiomed/centos7-systemd:base  
MAINTAINER Nicholas Alipaz <nalipaz@labiomed.org>  
  
RUN yum -y install\  
rsyslog &&\  
yum clean all &&\  
rm -rf /tmp/yum*  
  
RUN systemctl enable rsyslog.service  
  
EXPOSE 514

