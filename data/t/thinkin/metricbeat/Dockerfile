FROM debian:stretch-slim  
ENV DEBIAN_FRONTEND=nointeractive  
RUN apt-get update && apt-get install -y gnupg2 curl apt-transport-https && \  
(curl -qs https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -)
&&\  
(echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" >>
/etc/apt/sources.list.d/elastic-5.x.list) &&\  
apt-get update && apt-get install -y metricbeat  
  
ADD run.sh /  
ADD metricbeat.yml /etc/metricbeat/  
CMD /run.sh  

