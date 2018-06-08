FROM riccardoblb/jdk8:amd64  
MAINTAINER Riccardo Balbo <riccardo0blb@gmail.com>  
  
USER root  
ADD init.sh /init.sh  
ADD updater.sh /updater.sh  
ADD reddconomy_updater.sh /reddconomy_updater.sh  
  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN apk add --update curl openssl unzip supervisor bash&&\  
chmod +x /init.sh &&\  
chmod +x /updater.sh &&\  
chmod +x /reddconomy_updater.sh &&\  
mkdir -p /minecraft &&\  
chown java:java /minecraft -Rvf  
  
ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  
  

