FROM debian:jessie  
MAINTAINER Alois <alois@astronomer.io>  
  
RUN apt-get update \  
&& apt-get install -yyq --no-install-recommends dnsutils \  
&& apt-get install -y wget \  
apt-transport-https && \  
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add \-
&& \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a
/etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && apt-get install filebeat  
  
# Add filebeat config file  
ADD config/filebeat.yml /etc/filebeat  
  
CMD ["filebeat.sh", "-e"]  

