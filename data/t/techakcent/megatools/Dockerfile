FROM debian:latest  
  
RUN echo "deb http://http.us.debian.org/debian unstable main non-free contrib"
>> /etc/apt/sources.list  
RUN echo "deb-src http://http.us.debian.org/debian unstable main non-free
contrib" >> /etc/apt/sources.list  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y \  
megatools \  
wget \  
cron \  
vim \  
curl && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY jobs.txt /etc/cron.d/hello-cron  
RUN crontab /etc/cron.d/hello-cron  
COPY /entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

