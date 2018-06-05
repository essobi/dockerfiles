FROM amazonlinux:2017.03  
LABEL maintainer="mobingi,Inc."  
  
RUN yum update -y && yum install -y \  
awslogs \  
cronie \  
epel-release \  
logrotate \  
&& yum update -y --enablerepo=epel \  
&& yum install -y --enablerepo=epel inotify-tools \  
&& yum clean all --enablerepo=epel \  
&& easy_install supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
# awslogs  
COPY awslogs.conf /etc/awslogs/awslogs.conf  
COPY logging.conf /etc/awslogs/logging.conf  
COPY restart-awslogs.sh /restart-awslogs.sh  
RUN chmod 755 /restart-awslogs.sh  
  
# logrotate  
RUN rm -f /etc/logrotate.d/awslogs  
COPY alm-logrotate /etc/logrotate.d/alm-logrotate  
  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
  
HEALTHCHECK \--start-period=3m --interval=1m --timeout=5s \  
CMD supervisorctl status | grep -v RUNNING && exit 1 || exit 0  
  
CMD ["/run.sh"]  

