FROM centos:7  
MAINTAINER Frank Ritchie <fritchie@book.com>  
RUN yum install -y --nogpgcheck cronie logrotate rsyslog  
COPY script.rpm.sh /tmp  
RUN bash /tmp/script.rpm.sh && yum install -y --nogpgcheck \  
runit-2.1.1-7.el7.centos.x86_64  
ADD runit /etc/runit  
ADD rsyslogd /etc/service/rsyslogd  
ADD crond /etc/service/crond  
ADD container_environment /etc/container_environment  
ADD sbin/my_init /sbin/my_init  
CMD ["/sbin/my_init"]  

