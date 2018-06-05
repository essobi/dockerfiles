FROM node:9.3.0-stretch  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends build-essential jq g++ python-
dev python-pip python-setuptools python-wheel \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --upgrade awscli \  

