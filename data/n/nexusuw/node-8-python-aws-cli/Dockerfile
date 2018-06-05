  
FROM node:8  
RUN apt-get update \  
&& apt-get install -y python-dev zip jq \  
&& cd /tmp \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli \--upgrade \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

