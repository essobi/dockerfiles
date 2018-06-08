FROM debian:stable  
  
MAINTAINER Luca Pasquale  
  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >
/etc/apt/sources.list.d/backports.list  
RUN apt-get update && apt-get -y install cron certbot -t stretch-backports  
  
# Disable log rotation, so that we can tail one logfile in init.sh  
RUN mkdir -p /root/.config/letsencrypt  
RUN echo "max-log-backups = 0" > /root/.config/letsencrypt/cli.ini  
  
ADD init.sh /init.sh  
RUN chmod 0755 /init.sh  
  
EXPOSE 80  
ENTRYPOINT ["/init.sh"]  
CMD ["--help"]  
  

