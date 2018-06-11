FROM ubuntu:16.04  
  
MAINTAINER winter0mute <winter0mute@noreply.net>  
  
COPY files/preseed.txt /install/preseed.txt  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:certbot/certbot && \  
apt-get update && \  
export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && \  
debconf-set-selections /install/preseed.txt && \  
apt-get install -y certbot python3-pip && \  
pip3 install --upgrade pip && \  
pip3 install certbot-dns-cloudflare && \  
certbot plugins && \  
rm -rf /var/log/letsencrypt/*  

