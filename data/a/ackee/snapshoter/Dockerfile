FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get -y install lsb-release curl cron  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update  
RUN apt-get -y install google-cloud-sdk  
RUN mkdir -p /opt/  
COPY snapshoter.sh /opt/  
RUN chmod +x /opt/snapshoter.sh  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Prague
/etc/localtime  
  
ENTRYPOINT ["/entrypoint.sh"]  

