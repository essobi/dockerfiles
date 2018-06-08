FROM centos:centos7  
MAINTAINER quiver  
RUN yum clean all  
RUN yum -y update  
ADD http://rpms.adiscon.com/v8-devel/rsyslog.repo
/etc/yum.repos.d/rsyslog.repo  
RUN yum -y update  
RUN yum -y install rsyslog  
  
# enable UDP/TCP 514  
COPY rsyslog.conf /etc/rsyslog.conf  
  
# Define default command.  
ENTRYPOINT ["rsyslogd", "-i", "/var/run/syslogd.pid", "-f",
"/etc/rsyslog.conf", "-n" ]  
  
# Expose ports.  
EXPOSE 514  

