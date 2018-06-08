FROM ubuntu:16.04  
MAINTAINER FBLGIT@GitHub  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -qy
python-dev python-pip hhvm supervisor cron screen bzip2 mysql-client vim dstat
sysstat  
COPY start.sh /scripts/start.sh  
COPY SuperVisor/cron.conf /etc/supervisord/conf.d/cron.conf  
COPY Crontabs/root /var/spool/cron/crontabs/root  
CMD ["/scripts/start.sh"]  

