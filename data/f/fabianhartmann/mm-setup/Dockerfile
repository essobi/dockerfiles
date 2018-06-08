FROM ubuntu:14.04  
MAINTAINER fabian.hartmann@bluewin.ch  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
curl \  
supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GITREPO="https://github.com/MM-
MacManagement/WebTemplates/archive/axonlab.tar.gz"  
## RUN mkdir -p /srv/MMServiceData/MM-
SETUP/{CERT,CONF,LOG,REPORT,SCRIPTS,BACKUPS,DATA}  
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY ./worker.sh /srv/MMServiceData/MM-SETUP/SCRIPTS/worker.sh  
  
VOLUME ["/srv/MMServiceData/MM-SETUP"]  
  
ENV HOME /root  
  
WORKDIR /srv/MMServiceData/MM-SETUP  
  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

