FROM ubuntu:12.04  
MAINTAINER Rizky Maulana Nugraha<lana.pcfre@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y cron python-dev python-pip python-paramiko build-
essential  
RUN pip install --upgrade paramiko  
ADD backups-cron /etc/cron.d/backups-cron  
RUN touch /var/log/cron.log  
ADD backups.sh /backups.sh  
ADD start.sh /start.sh  
ADD cleanup.sh /cleanup.sh  
ADD cleanup.py /cleanup.py  
ADD sftp_remote.py /sftp_remote.py  
RUN chmod +x /cleanup.sh /cleanup.py  
  
CMD ["/start.sh"]  

