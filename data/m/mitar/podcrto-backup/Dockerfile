FROM tozd/cron:ubuntu-xenial  
  
RUN apt-get update -q -q && \  
apt-get --yes --force-yes install python3 ca-certificates && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache ~/.npm  
  
COPY ./code /code  
  
COPY ./etc /etc  

