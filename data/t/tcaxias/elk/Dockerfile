FROM tcaxias/debian  
  
RUN \  
apt update \  
&& $APT install wget apt-transport-https ca-certificates \  
&& wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch \  
| apt-key add \- \  
&& echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" \  
| tee -a /etc/apt/sources.list.d/elastic-5.x.list \  
&& apt update  

