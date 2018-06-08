FROM ubuntu:trusty  
MAINTAINER sohrab  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \  
echo "deb http://apt.sonarr.tv/ master main" | tee
/etc/apt/sources.list.d/sonarr.list && \  
apt-get update && \  
apt-get install -y nzbdrone && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /volumes/config  
VOLUME /volumes/completed  
VOLUME /volumes/media  
  
EXPOSE 8989  
COPY start.sh /  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

