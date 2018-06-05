FROM ubuntu:latest  
MAINTAINER docker@ekito.fr  
  
RUN apt-get update -y && apt-get dist-upgrade -y  
  
RUN apt-get install -y calibre xvfb ImageMagick  
RUN apt-get -y install rsyslog  
  
RUN apt-get clean  
  
RUN rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*rack*.com* && rm -rf
/var/lib/apt/lists/security.ubuntu.com_ubuntu_dists_precise-security_*  
  
EXPOSE 8080  
# Create directory for library  
RUN mkdir -p /opt/calibre/library  
  
# Create directory to import files  
RUN mkdir -p /opt/calibre/import  
VOLUME ["/opt/calibre/import“]  
  
# Add crontab job to import books in the library  
ADD crontab /etc/cron.d/calibre-update  
RUN chmod 0644 /etc/cron.d/calibre-update  
RUN touch /var/log/cron.log  
  
# Run cron job and start calibre server  
CMD cron && /usr/bin/calibre-server --with-library=/opt/calibre/library  
  

