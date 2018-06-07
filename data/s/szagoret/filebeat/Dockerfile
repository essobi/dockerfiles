FROM debian:jessie  
  
#default LOGSTASH_HOST variable  
ENV LOGSTASH_HOST localhost  
  
#install nano && dos2unix to  
#convert line lndings during build  
#this will fix error:  
#standard_init_linux.go:175: exec user process caused 'no such file or
directory'  
RUN apt-get update && apt-get install nano && \  
apt-get install -y dos2unix  
  
#create folder to mount logs location on host  
RUN mkdir -p /filebeat-logs  
#mount point for host logs  
VOLUME ["/filebeat-logs/"]  
  
#copy and extract filebeat  
ADD ["filebeat-5.0.0-linux-x86_64.tar.gz", "/"]  
  
#copy filebeat configuration file  
COPY ["filebeat.yml", "/filebeat.yml"]  
  
#add entrypoint script  
ADD ["docker-entrypoint.sh", "/entrypoint.sh"]  
  
#change line engings and remove dos2unix  
RUN dos2unix /entrypoint.sh && apt-get --purge remove -y dos2unix && \  
rm -rf /var/lib/apt/lists/*  
  
#make the file executable  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/filebeat-5.0.0-linux-x86_64/filebeat", "-c", "/filebeat.yml"]

