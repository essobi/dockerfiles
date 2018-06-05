FROM debian:jessie  
MAINTAINER Oscar Rocha <orocha@healthefilings.com>  
  
ENV BARMAN_VERSION 2.1-1  
RUN echo "deb http://ftp.us.debian.org/debian/ stretch main contrib non-free"
\  
>> /etc/apt/sources.list  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-jessie main" | \  
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
  
RUN apt-get update  
  
RUN apt-get install -y curl  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \  
apt-key add -  
RUN apt-get install -y --force-yes barman=$BARMAN_VERSION google-cloud-sdk  
  
RUN rm /etc/barman.d/*  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY post_backup_retry_script.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/post_backup_retry_script.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["barman"]  

