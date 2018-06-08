FROM mysql:5.7.18  
MAINTAINER Bruce McCleave <bruce@thinkiq.com>  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN apt-get update && \  
apt-get install -y sudo curl tar sudo openssh-server openssh-client rsync
netcat && \  
chmod 777 /usr/local/bin/docker-entrypoint.sh && \  
cd /tmp && \  
curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.5.2-amd64.deb
&& \  
dpkg -i filebeat-5.5.2-amd64.deb && \  
apt-get upgrade -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
COPY filebeat.yml /etc/filebeat/filebeat.yml  
COPY thinkiq.cnf /etc/mysql/conf.d/thinkiq.cnf

