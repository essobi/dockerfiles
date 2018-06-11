FROM gitlab/gitlab-ce  
MAINTAINER Daniel Miller <watermelonpizza@melonstudios.net>  
  
RUN apt-get update && \  
apt-get install -y cron && \  
rm -rf /var/cache/apt/*  
  
RUN (crontab -l; echo "0 2 * * * /opt/gitlab/bin/gitlab-rake
gitlab:backup:create CRON=1") | crontab -  

