FROM debian:jessie-slim  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
ENV PYTHONIOENCODING=UTF-8  
RUN apt-get install -y \  
cron \  
python \  
python-pip \  
python-virtualenv \  
vim \  
jq && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install --upgrade awscli  
  
COPY bin/* /usr/local/bin/  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

