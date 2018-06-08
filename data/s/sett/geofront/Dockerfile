FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
python3-pip \  
build-essential \  
libssl-dev \  
libffi-dev \  
python3-dev \  
python3-jinja2 \  
python3-werkzeug \  
&& pip3 install redis Geofront \  
&& pip3 install cryptography \  
&& apt-get clean  
  
WORKDIR /config  
CMD ["geofront-server", "-p", "8080", "--create-master-key",
"geofront.cfg.py"]

