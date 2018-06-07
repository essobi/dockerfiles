FROM iojs:1.6  
RUN deps='python-yaml python-jinja2 python-httplib2 python-keyczar python-
paramiko python-setuptools python-pkg-resources python-pip software-
properties-common'; \  
set -x \  
&& echo 'Acquire::CompressionTypes::Order::="gz";' >> /etc/apt/apt.conf \  
&& apt-get update && apt-get install -y $deps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install ansible \  
&& mkdir /data  
  
WORKDIR /data  

