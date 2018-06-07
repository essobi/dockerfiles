FROM debian:stretch  
MAINTAINER Christian Simon  
  
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y \  
curl \  
git \  
python3 \  
python3-pip \  
vim \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /etc/dehydrated \  
&& cd /etc/dehydrated \  
&& mkdir certs accounts hooks \  
&& mkdir /dehydrated \  
&& cd /opt \  
&& git clone https://github.com/lukas2511/dehydrated.git \  
&& cd /opt/dehydrated \  
&& cp docs/examples/config /etc/dehydrated/ \  
&& cp docs/examples/domains.txt /etc/dehydrated/ \  
&& ln -s /opt/dehydrated/dehydrated /usr/local/bin/ \  
&& cd /opt \  
&& git clone https://github.com/rembik/dehydrated-hetzner-hook.git \  
&& ln -s /opt/dehydrated-hetzner-hook/ /etc/dehydrated/hooks/hetzner \  
&& pip3 install -r dehydrated-hetzner-hook/requirements.txt \  
&& sed -i -e 's@#!/usr/bin/env python@#!/usr/bin/env python3@'
/opt/dehydrated-hetzner-hook/hook.py  
  
ENTRYPOINT ["/opt/dehydrated/dehydrated"]  

