FROM amazonlinux:2017.03  
LABEL maintainer="mobingi,Inc."  
  
RUN yum update -y && yum install -y \  
awslogs \  
cronie \  
logrotate \  
&& yum clean all \  
&& easy_install supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
# awslogs  
COPY awslogs.conf /etc/awslogs/awslogs.conf  
COPY logging.conf /etc/awslogs/logging.conf  
COPY restart-awslogs /etc/cron.d/restart-awslogs  
COPY restart-awslogs.sh /restart-awslogs.sh  
RUN chmod 644 /etc/cron.d/restart-awslogs  
RUN chmod 755 /restart-awslogs.sh  
  
# logrotate  
RUN rm -f /etc/logrotate.d/awslogs  
COPY mo-logrotate /etc/logrotate.d/mo-logrotate  
  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  

