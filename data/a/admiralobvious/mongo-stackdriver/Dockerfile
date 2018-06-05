FROM mongo  
  
MAINTAINER Alexandre Ferland <aferlandqc@gmail.com>  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
ca-certificates \  
curl \  
lsb-release \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -O "https://repo.stackdriver.com/stack-install.sh" \  
&& bash stack-install.sh \--write-gcm \  
&& (cd /opt/stackdriver/collectd/etc/collectd.d/ && curl -O
https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-
configs/master/etc/collectd.d/mongodb.conf)  
  

