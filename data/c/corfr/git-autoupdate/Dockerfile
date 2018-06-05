# gerrit  
FROM debian:latest  
  
MAINTAINER Bertrand Roussel <broussel@sierrawireless.com>  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y sudo vim-tiny git cron
rsyslog procps netcat  
  
ADD entrypoint.sh /  
ADD update.sh /  
  
ENV VOLUME_PATH /git  
VOLUME ["/git"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 10000  

