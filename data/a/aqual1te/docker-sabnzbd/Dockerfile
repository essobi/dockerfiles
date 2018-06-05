FROM debian:latest  
MAINTAINER AquaL1te  
  
VOLUME ["/config", "/data"]  
  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install sabnzbdplus git  
RUN apt-get -y autoremove  
RUN apt-get -y clean  
  
RUN git clone https://github.com/CouchPotato/CouchPotatoServer.git
/var/lib/CouchPotatoServer  
RUN touch /config/settings.conf  
  
EXPOSE 8080 9090 5050  
#CMD ["/usr/bin/sabnzbdplus", "--config-file", "/config", "--server",
"0.0.0.0:8080", "--console"]  
#CMD ["/usr/bin/sabnzbdplus", "--config-file", "/config", "--data-dir",
"/data", "--server", "0.0.0.0:8080"]  
CMD ["/var/lib/CouchPotatoServer/CouchPotato.py", "--config_file",
"/config/settings.conf", "--data_dir", "/data", "--console_log"]  

