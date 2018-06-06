FROM ubuntu:16.04  
MAINTAINER : g6nuk  
COPY curator.cron /var/  
RUN apt-get update && \  
apt-get install -y wget cron && \  
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -
&& \  
echo deb http://packages.elastic.co/curator/4/debian stable main >
/etc/apt/sources.list.d/curator.list && \  
apt-get update && \  
apt-get install -y elasticsearch-curator && \  
apt-get clean && \  
touch /var/log/cron.log  
COPY config.yaml /tmp/  
COPY action.yaml /tmp/  
CMD crontab /var/curator.cron && service cron start && tail -f
/var/log/cron.log  

