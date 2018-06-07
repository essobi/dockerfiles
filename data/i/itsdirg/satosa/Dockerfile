FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
python3-dev \  
build-essential \  
python3-pip \  
libffi-dev \  
libssl-dev \  
xmlsec1 \  
libyaml-dev  
  
COPY SATOSA-3.3.1-py3-none-any.whl /SATOSA-3.3.1-py3-none-any.whl  
RUN pip3 install /SATOSA-3.3.1-py3-none-any.whl  
  
COPY start.sh /tmp/satosa/start.sh  
ENTRYPOINT ["/tmp/satosa/start.sh"]  

