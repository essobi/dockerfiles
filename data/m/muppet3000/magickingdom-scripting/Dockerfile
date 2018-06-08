FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
#EPEL and NUX provide what is needed for unrar  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm && \  
yum install -y rsync cronie unrar msmtp && \  
yum clean all  
  
#Email config  
ADD msmtprc /etc/msmtprc  
ADD email_template.mail /opt/email_template.mail  
  
#Backups  
ADD backups-cron /etc/cron.d/backups-cron  
  
#Extractions  
ADD extract-cron /etc/cron.d/extract-cron  
  
#Touch  
ADD touch-cron /etc/cron.d/touch-cron  
  
#Status Check  
ADD status-check-cron /etc/cron.d/status-check-cron  
  
#Set correct perms for cron jobs  
RUN chmod 0644 /etc/cron.d/*  
  
#Scripts  
COPY scripts /opt/scripts  
  
VOLUME ["/media/storage", "/media/docker_runtime_volumes", "/media/backups"]  
  
RUN touch /var/log/cron  
  
CMD crond && tail -f /var/log/cron  
  

