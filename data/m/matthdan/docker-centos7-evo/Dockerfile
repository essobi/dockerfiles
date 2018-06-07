# Centos 7  
# BASE Image with SSH+rsyslog  
#  
# Matthieu DANIEL <matthieu.daniel@gmail.com>  
#  
# VERSION 0.0.1  
FROM centos:latest  
MAINTAINER Matthieu DANIEL "matth.daniel@gmail.com"  
# Add epel 7 repo  
RUN rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
  
# Set root passwd  
RUN echo "root:root"|chpasswd  
  
# Supervisord dependencies  
RUN yum -y install supervisor  
RUN sed -i -e 's/nodaemon=false/nodaemon=true/' /etc/supervisord.conf  
  
# SSHD  
RUN yum install -y openssh-server  
RUN mkdir -p /var/run/sshd  
ADD supervisord/bin/startup-sshd /usr/local/bin/startup-sshd  
RUN chmod u+x /usr/local/bin/startup-sshd  
RUN sed -i -e 's/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config  
ADD supervisord/services/sshd.ini /etc/supervisord.d/sshd.ini  
  
# We do not care about the known_hosts-file and all the security  
RUN echo " StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
RUN echo " UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config  
RUN echo " AddressFamily inet" >> /etc/ssh/ssh_config  
  
# Rsyslog Install  
RUN yum install -y rsyslog  
# Rsyslog configuration  
ADD rsyslog/rsyslog.conf /etc/rsyslog.conf  
# Delete file to enable rsyslog running in docker container  
# [user@srv]# rpm -qf /etc/rsyslog.d/listen.conf  
# systemd-219-19.el7_2.7.x86_64  
RUN rm /etc/rsyslog.d/listen.conf  
ADD supervisord/bin/startup-rsyslog /usr/local/bin/startup-rsyslog  
RUN chmod u+x /usr/local/bin/startup-rsyslog  
ADD supervisord/services/rsyslog.ini /etc/supervisord.d/  
  
CMD /bin/supervisord -c /etc/supervisord.conf  

