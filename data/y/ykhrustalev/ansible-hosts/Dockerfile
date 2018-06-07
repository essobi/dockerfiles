FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
python-pip \  
build-essential \  
python-dev \  
libssl-dev \  
libffi-dev \  
&& pip install -U \  
`# common ansible` \  
pycrypto \  
cryptography \  
jinja2 \  
paramiko \  
PyYAML \  
&& rm -rf /var/lib/apt/lists/* /root/.cache  

