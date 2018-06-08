FROM ubuntu:14.04  
RUN \  
apt-get update \  
&& apt-get install -y \  
python \  
python-dev \  
python-distribute \  
python-pip  
  
COPY src/requirements.txt /tmp/requirements.txt  
  
RUN \  
pip install -r /tmp/requirements.txt \  
&& rm /tmp/requirements.txt  
  
COPY src /usr/local/pkgman  
  
RUN \  
cd /usr/local/pkgman \  
&& pip install -e .  

