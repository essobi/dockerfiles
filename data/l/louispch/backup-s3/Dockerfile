FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get install -y \  
cron \  
tzdata \  
python-pip \  
python-dev \  
build-essential  
  
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && dpkg-reconfigure
-f noninteractive tzdata  
  
RUN pip install --upgrade pip && pip install --upgrade virtualenv  
  
RUN pip install awscli  
  
ADD scripts/ /scripts/  
  
ADD crontab /etc/cron.d/daily-cron  
  
RUN chmod 0644 /etc/cron.d/daily-cron  
  
RUN touch /var/log/cron.log  
  
WORKDIR backups/  
  
RUN chmod +x /scripts/init.sh  
  
CMD bash /scripts/init.sh

